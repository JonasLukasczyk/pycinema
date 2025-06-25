import pycinema
import pycinema.filters
import pycinema.theater
import pycinema.theater.views

# pycinema settings
PYCINEMA = { 'VERSION' : '3.0.0'}

# filters
MeshRenderer_0 = pycinema.filters.MeshRenderer()
ColorMapping_0 = pycinema.filters.ColorMapping()
RenderView_0 = pycinema.filters.RenderView()

# properties
MeshRenderer_0.inputs.data.set(None, False)
MeshRenderer_0.inputs.cameras.set(RenderView_0.inputs.camera, False)
MeshRenderer_0.inputs.resolution.set((256, 256), False)
ColorMapping_0.inputs.map.set("plasma", False)
ColorMapping_0.inputs.nan.set((1, 1, 1, 1), False)
ColorMapping_0.inputs.range.set(RenderView_0.inputs.camera, False)
ColorMapping_0.inputs.channel.set("depth", False)
ColorMapping_0.inputs.images.set(MeshRenderer_0.outputs.images, False)
ColorMapping_0.inputs.composition_id.set(-1, False)
RenderView_0.inputs.images.set(ColorMapping_0.outputs.images, False)
RenderView_0.inputs.camera.set([-0.9, 0.3], False)

# layout
tabFrame1 = pycinema.theater.TabFrame()
splitFrame1 = pycinema.theater.SplitFrame()
splitFrame1.setHorizontalOrientation()
view1 = pycinema.theater.views.NodeEditorView()
splitFrame1.insertView( 0, view1 )
view2 = pycinema.theater.views.FilterView( RenderView_0 )
splitFrame1.insertView( 1, view2 )
splitFrame1.setSizes([508, 508])
tabFrame1.insertTab(0, splitFrame1)
tabFrame1.setTabText(0, 'Layout 1')
tabFrame1.setCurrentIndex(0)
pycinema.theater.Theater.instance.setCentralWidget(tabFrame1)

# execute pipeline
MeshRenderer_0.update()
