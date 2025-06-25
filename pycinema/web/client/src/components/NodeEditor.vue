<script setup>
import { ref, onMounted, onUnmounted, reactive, watch } from 'vue';

import Scene from './Scene.js'
import WebSocketCommunicator from './WebSocketCommunicator.js'
import { useQuasar } from 'quasar'
const $q = useQuasar();

const svg_canvas = ref(null);
const filter_browser = ref(null);

const iProps = reactive ({
  communicator: null,
  filter_browser: {
    list: [],
    list_: [],
    selected: null,
    search: (val, update) => {
      if (val === '')
        update(() => {
          iProps.filter_browser.list_ = iProps.filter_browser.list;
        });
      else
        update(() => {
          const needle = val.toLowerCase()
          iProps.filter_browser.list_ = iProps.filter_browser.list.filter(v => v.toLowerCase().indexOf(needle) > -1);
        });
    }
  },
  scene: null
});

const requestCreateFilter = type=>{
  if(!type) return;
  iProps.filter_browser.selected = null;
  WebSocketCommunicator.sendMessage('create_filter',type);
};

const init = async ()=>{
  iProps.scene = new Scene( svg_canvas.value, $q );

  // communicator
  WebSocketCommunicator.on('message', msg=>{
    switch(msg.header){
      case 'filter_list':
        return iProps.filter_browser.list = msg.payload;
    }
  });

  WebSocketCommunicator.on('open', ()=>{
    console.log("Connected to WebSocket server");
    WebSocketCommunicator.sendMessage('get_filter_list');

    // requestCreateFilter('CinemaDatabaseReader');
    // requestCreateFilter('TableQuery');
    // requestCreateFilter('ImageReader');

  });
}

const openFilterBrowserDialog = ()=>{
  filter_browser._value.showPopup();
}

onMounted(init);
onUnmounted(()=>{
  // iProps.filter_browser.watcher();
});

</script>

<template>
  <div class='node_editor_container'>
    <div style='position:absolute;top:20px;left:20px'>
      <q-btn label='+' dense round color="primary" @click='openFilterBrowserDialog'/>
      <!--<q-btn label='L' dense round color="primary" @click='openFilterBrowserDialog'/>-->

      <q-select
        dark
        ref='filter_browser'
        use-input
        v-model="iProps.filter_browser.selected"
        input-debounce="0"
        :options="iProps.filter_browser.list_"
        @filter="iProps.filter_browser.search"
        @update:model-value='requestCreateFilter'
        style="width: 250px;display:none"
        behavior="dialog"
        label-color='white'
        dense
        options-dense
      >
      </q-select>
    </div>

    <svg class='node_editor_canvas' ref='svg_canvas' style="width:100%;height:100%">
      <defs>
        <pattern id="inner-grid" width="10" height="10" patternUnits="userSpaceOnUse">
          <rect width="100%" height="100%" fill="none" stroke="#666" stroke-width="0.5" />
        </pattern>
        <pattern id="grid" width="100" height="100" patternUnits="userSpaceOnUse">
          <rect width="100%" height="100%" fill="url(#inner-grid)" stroke="#666" stroke-width="1.5" />
        </pattern>
      </defs>
    </svg>

  </div>
</template>

<style>
.node_editor_container {
  display: block;
  position: absolute;
  left:0;
  right:0;
  top:0;
  bottom:0;
  overflow: hidden;
  /*background-color: #000;*/
}

.node_content {
  background-color: #555;
  /*background-color: rgba(50,50,50,0.8);*/
  border-radius: 0.75em;
  display: inline-block;
  overflow: hidden;
  /*resize: both;*/
  /*padding: 1em;*/
  padding: 0 0.5em 0.5em 0.5em;
}

.node_content h1 {
  font-size: 1em;
  padding: 0.5em 0 0.3em 0;
  margin: 0;
  font-weight:bold;
  text-align: center;
  cursor:pointer;
}

.selected {
  background-color: #2e5984;
}

.input_port,.output_port  {
  /*border:0.01em solid #f00;*/
  border-radius: 0.2em;
  background-color: #333;
  margin: 0.2em 0;
  display: flex;
  align-items: center;
}

.input_port input:read-only, .output_port input:read-only {
  color:#888;
}

.node_content label {
  /*border:0.01em solid #f00;*/
  padding: 0.2em;
  font-weight: bold;
  flex-shrink: 0;
}

.node_content input {
  border:0;
  background: transparent;
  outline:none;
  width: 100%;
  flex-grow: 1;
}
.node_content input:focus {
  outline:none!important;
}

.input_port_disc, .output_port_disc {
  cursor: pointer;
}

.node_content label {
  cursor: pointer;
}

</style>
