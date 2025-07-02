import Node from './Node.js';
import Edge from './Edge.js';
import WebSocketCommunicator from './WebSocketCommunicator.js';
import { instance } from "@viz-js/viz";

import PortDialog from './PortDialog.vue';

import * as d3 from 'd3';

const animation_data = {
  nodes: null,
  t0: null,
  duration: null
};

const animate_scene = () => {
  const dt = performance.now() - animation_data.t0;
  const l = Math.min(dt/animation_data.duration,1);
  for(let node of animation_data.nodes)
    node.moveTo(
      l*node.move_target[0] + (1-l)*node.move_origin[0],
      l*node.move_target[1] + (1-l)*node.move_origin[1]
    );
  if(dt<animation_data.duration)
    requestAnimationFrame(animate_scene);
};

class Scene {
  constructor(svg_canvas,quasar){

    this.quasar = quasar;

    instance().then(viz=>{
      this.viz = viz;
    });

    // communicator
    WebSocketCommunicator.on('message', msg=>{
      console.log(msg)
      switch(msg.header){
        case 'filter_created':
          return this.addNode(msg.payload);
        case 'connection_added':
          return this.addEdge(msg.payload);
        case 'filter_status':
          return this.setStatus(msg.payload);
        case 'value_set':
          const port = msg.payload[0];
          const node = this.nodes.get(port.parent);
          const port_ = node.filter[port.is_input?'inputs':'outputs'].find(i=>i.name===port.name);
          for(let key of Object.keys(port))
            port_[key] = port[key];

          port_.input.mute = true;
          port_.input.setAttribute('value',port_.value_str);
          port_.input.mute = false;
          if(port_.is_input)
            if(port_.portRef)
              port_.input.setAttribute('readonly', true);
            else
              port_.input.removeAttribute('readonly');
          return;
      }
    });

    this.svg = d3.select(svg_canvas);
    this.nodes = new Map();
    this.edges = new Map();

    const patternGrid = this.svg.select('#grid');
    const patternInnerGrid = this.svg.select('#inner-grid');

    this.grid = this.svg.append('rect')
      .attr('x',0)
      .attr('y',0)
      .attr('width','100%')
      .attr('height','100%')
      .attr('fill','url(#grid)')
    ;

    this.root = this.svg.append('g');
    this.svg.root = this.root;
    this.edge_layer = this.root.append('g');
    this.node_layer = this.root.append('g');

    this.grid.on('click', ()=>this.selectNode());

    const transformed = ({transform}) => {
      const transform10 = parseInt(transform.k * 10);
      const transform100 = transform10 * 10;

      // Don't move the grid itself, simply change the pattern.
      patternGrid
        .attr('x', parseInt(transform.x % transform100))
        .attr('y', parseInt(transform.y % transform100))
        .attr('width', transform100)
        .attr('height', transform100);
      patternInnerGrid
        .attr('width', transform10)
        .attr('height', transform10);

      // Translate and scale the canvas.
      this.root.attr('transform', transform);
    };
    const zoom = d3.zoom()
        .scaleExtent([0.25, 4])
        .on("zoom", transformed);

    this.svg.call(zoom).call(zoom.transform, d3.zoomIdentity);
  }

  selectNode(node){
    for(let [_,n] of this.nodes)
      n.div._groups[0][0].classList.remove('selected');
    node && node.div._groups[0][0].classList.add('selected');
  }

  autoConnectFilters(n0,n1){
    if(!n0 || !n1) return;
    const f0 = n0.filter;
    const f1 = n1.filter;
    for(let o of f0.outputs)
      for(let i of f1.inputs)
        if(o.name===i.name)
          WebSocketCommunicator.sendMessage(
            'connect_ports',
            [o,i]
          );
  }

  showPort(port){
    this.quasar.dialog({
      component: PortDialog,
      componentProps: {port:port}
    });
  }

  setStatus([id,status]){
    if(id<0){
      this.nodes.forEach(n=>n.setStatus(status));
    } else {
      this.nodes.get(id).setStatus(status);
    }
  }

  addNode(filter){
    console.log(filter)
    const node = new Node(filter,this.svg,this.node_layer);
    node.moveTo(Math.random()*500,Math.random()*500);
    this.nodes.set(filter.id,node);
    this.edges.set(filter.id,[]);

    node.on('clicked',node=>this.selectNode(node));
    node.on('port_clicked',port=>this.showPort(port));
    const selected_node = [...this.nodes.values()].filter(n=>n.div._groups[0][0].classList.contains('selected')).pop();
    this.autoConnectFilters(selected_node,node);

    this.selectNode(node);

    this.computeLayout();
  }

  addEdge(ports){
    const edge = new Edge(
      ports,
      ports.map(p=>this.nodes.get(p.parent)),
      this.svg,
      this.edge_layer
    );
    this.edges.get(ports[0].parent).push(edge);
    this.edges.get(ports[1].parent).push(edge);

    this.computeLayout();
  }

  computeLayout(){

    let node_string = ``;
    let edge_string = ``;
    for(let [id,node] of this.nodes){
      node_string+=`${id}[shape=record,height=${node.xhtml._groups[0][0].clientHeight/100},width=${node.xhtml._groups[0][0].clientWidth/100},label="{ {${node.filter.outputs.map((_,i)=>`<o${i}>`).concat(node.filter.inputs.map((_,i)=>`<i${i}>`)).join('|')}} }"];\n`;

      for(let p0_idx in node.filter.inputs){
        const p0 = node.filter.inputs[p0_idx];
        if(p0.portRef){
          const p1_idx = this.nodes.get(p0.portRef.parent)
            .filter[p0.portRef.is_input?'inputs':'outputs']
            .findIndex(_=>_.name===p0.portRef.name)
          ;
          edge_string += `${p0.portRef.parent}:o${p1_idx}->${p0.parent}:i${p0_idx};\n`;
        }
      }
    }

    let dot = `digraph {rankdir = LR;\n`;
    dot+=node_string;
    dot+=edge_string;
    dot+=`}\n`;

    const layout = this.viz.renderJSON(dot);
    for(let node_layout of layout.objects){
      const node = this.nodes.get(node_layout.name);
      node.move_origin = node.getPos();
      node.move_target = node_layout.pos.split(',').map(i=>parseFloat(i)*1.7)
    }

    animation_data.t0 = performance.now();
    animation_data.duration = 200;
    animation_data.nodes = [...this.nodes.values()];
    requestAnimationFrame(animate_scene);
  }
}
export default Scene;
