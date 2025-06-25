
import pycinema
import pycinema.filters
import pycinema.theater
import pycinema.theater.views

# layout
vf0 = pycinema.theater.Theater.instance.centralWidget()
vf0.setHorizontalOrientation()
vf1 = vf0.insertFrame(0)
vf1.setVerticalOrientation()
ParallelCoordinatesView_0 = vf1.insertView( 0, pycinema.theater.views.ParallelCoordinatesView() )
TableView_0 = vf1.insertView( 1, pycinema.theater.views.TableView() )
ColorMappingView_0 = vf1.insertView( 2, pycinema.theater.views.ColorMappingView() )
vf1.setSizes([296, 630, 439])
vf2 = vf0.insertFrame(1)
vf2.setVerticalOrientation()
ImageView_0 = vf2.insertView( 0, pycinema.theater.views.ImageView() )
vf2.setSizes([1373])
vf0.setSizes([1018, 1528])

# filters
CinemaDatabaseReader_0 = pycinema.filters.CinemaDatabaseReader()
ImageReader_0 = pycinema.filters.ImageReader()
DepthCompositing_0 = pycinema.filters.DepthCompositing()
ShaderSSAO_0 = pycinema.filters.ShaderSSAO()
Annotation_0 = pycinema.filters.Annotation()

# properties
ParallelCoordinatesView_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
ParallelCoordinatesView_0.inputs.ignore.set(['file', 'id', 'object_id_name'], False)
ParallelCoordinatesView_0.inputs.state.set({'object_id': (0, 2, True), 'phi': (2, 2, False), 'theta': (0, 0, False), 'time': (0, 4, False)}, False)
TableView_0.inputs.table.set(ParallelCoordinatesView_0.outputs.table, False)
ColorMappingView_0.inputs.images.set(DepthCompositing_0.outputs.images, False)
ColorMappingView_0.inputs.channel.set("depth", False)
ColorMappingView_0.inputs.map.set("BuGn", False)
ColorMappingView_0.inputs.range.set((0, 1), False)
ColorMappingView_0.inputs.nan.set((1, 1, 1, 1), False)
ColorMappingView_0.inputs.composition_id.set(-1, False)
ImageView_0.inputs.images.set(Annotation_0.outputs.images, False)
CinemaDatabaseReader_0.inputs.path.set("data/ScalarImages.cdb/", False)
CinemaDatabaseReader_0.inputs.file_column.set("file", False)
ImageReader_0.inputs.table.set(ParallelCoordinatesView_0.outputs.table, False)
ImageReader_0.inputs.file_column.set("FILE", False)
ImageReader_0.inputs.cache.set(True, False)
DepthCompositing_0.inputs.images_a.set(ImageReader_0.outputs.images, False)
DepthCompositing_0.inputs.images_b.set([], False)
DepthCompositing_0.inputs.depth_channel.set("depth", False)
DepthCompositing_0.inputs.compose.set(ParallelCoordinatesView_0.outputs.compose, False)
ShaderSSAO_0.inputs.images.set(ColorMappingView_0.outputs.images, False)
ShaderSSAO_0.inputs.radius.set(0.03, False)
ShaderSSAO_0.inputs.samples.set(128, False)
ShaderSSAO_0.inputs.diff.set(0.5, False)
Annotation_0.inputs.images.set(ShaderSSAO_0.outputs.images, False)
Annotation_0.inputs.xy.set((20, 20), False)
Annotation_0.inputs.size.set(20, False)
Annotation_0.inputs.spacing.set(0, False)
Annotation_0.inputs.color.set((), False)
Annotation_0.inputs.ignore.set(['file', 'id'], False)

# execute pipeline
ParallelCoordinatesView_0.update()
