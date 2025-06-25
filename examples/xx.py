
import pycinema
import pycinema.filters
import pycinema.theater
import pycinema.theater.views

# layout
vf0 = pycinema.theater.Theater.instance.centralWidget()
vf0.setHorizontalOrientation()
vf1 = vf0.insertFrame(0)
vf1.setVerticalOrientation()
ParameterView_0 = vf1.insertView( 0, pycinema.theater.views.ParameterView() )
TableView_0 = vf1.insertView( 1, pycinema.theater.views.TableView() )
ColorMappingView_0 = vf1.insertView( 2, pycinema.theater.views.ColorMappingView() )
vf1.setSizes([563, 122, 174])
ImageView_0 = vf0.insertView( 1, pycinema.theater.views.ImageView() )
vf0.setSizes([340, 680])

# filters
CinemaDatabaseReader_0 = pycinema.filters.CinemaDatabaseReader()
ImageReader_0 = pycinema.filters.ImageReader()
DepthCompositing_0 = pycinema.filters.DepthCompositing()
ShaderSSAO_0 = pycinema.filters.ShaderSSAO()
ImageAnnotation_0 = pycinema.filters.ImageAnnotation()

# properties
ParameterView_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
ParameterView_0.inputs.ignore.set(['file', 'id'], False)
ParameterView_0.inputs.state.set({'Phi': {'C': False, 'T': 'S', 'S': 0, 'O': [0]}, 'Theta': {'C': False, 'T': 'S', 'S': 0, 'O': [0]}}, False)
TableView_0.inputs.table.set(ParameterView_0.outputs.table, False)
ColorMappingView_0.inputs.images.set(DepthCompositing_0.outputs.images, False)
ColorMappingView_0.inputs.channel.set("Depth", False)
ColorMappingView_0.inputs.map.set("plasma", False)
ColorMappingView_0.inputs.range.set((0, 1), False)
ColorMappingView_0.inputs.nan.set((1, 1, 1, 1), False)
ColorMappingView_0.inputs.composition_id.set(-1, False)
ImageView_0.inputs.images.set(ImageAnnotation_0.outputs.images, False)
CinemaDatabaseReader_0.inputs.path.set("/home/jones/external/projects/cinema-lib/pycinema-data/Brain.cdb/", False)
CinemaDatabaseReader_0.inputs.file_column.set("FILE", False)
ImageReader_0.inputs.table.set(ParameterView_0.outputs.table, False)
ImageReader_0.inputs.file_column.set("FILE", False)
ImageReader_0.inputs.cache.set(True, False)
DepthCompositing_0.inputs.images_a.set(ImageReader_0.outputs.images, False)
DepthCompositing_0.inputs.images_b.set([], False)
DepthCompositing_0.inputs.depth_channel.set("depth", False)
DepthCompositing_0.inputs.compose.set(ParameterView_0.outputs.compose, False)
ShaderSSAO_0.inputs.images.set(ColorMappingView_0.outputs.images, False)
ShaderSSAO_0.inputs.radius.set(0.03, False)
ShaderSSAO_0.inputs.samples.set(128, False)
ShaderSSAO_0.inputs.diff.set(0.5, False)
ImageAnnotation_0.inputs.images.set(ShaderSSAO_0.outputs.images, False)
ImageAnnotation_0.inputs.xy.set((20, 20), False)
ImageAnnotation_0.inputs.size.set(20, False)
ImageAnnotation_0.inputs.spacing.set(0, False)
ImageAnnotation_0.inputs.color.set((), False)
ImageAnnotation_0.inputs.ignore.set(['file', 'id'], False)

# execute pipeline
ParameterView_0.update()
