import pycinema
import pycinema.filters
import pycinema.theater
import pycinema.theater.views

# pycinema settings
PYCINEMA = { 'VERSION' : '3.0.0'}

# filters
CinemaDatabaseReader_0 = pycinema.filters.CinemaDatabaseReader()
TableQuery_0 = pycinema.filters.TableQuery()
ImageReader_0 = pycinema.filters.ImageReader()
ImageView_0 = pycinema.filters.ImageView()
TableView_0 = pycinema.filters.TableView()
ImageAnnotation_0 = pycinema.filters.ImageAnnotation()

# properties
CinemaDatabaseReader_0.inputs.path.set("./data/scalar-images.cdb", False)
CinemaDatabaseReader_0.inputs.file_column.set("FILE", False)
TableQuery_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
TableQuery_0.inputs.sql.set("SELECT * FROM input LIMIT 10", False)
ImageReader_0.inputs.table.set(TableQuery_0.outputs.table, False)
ImageReader_0.inputs.file_column.set("FILE", False)
ImageReader_0.inputs.cache.set(True, False)
ImageView_0.inputs.images.set(ImageAnnotation_0.outputs.images, False)
ImageView_0.inputs.selection.set([1, 2, 3, 4, 6], False)
TableView_0.inputs.table.set(ImageReader_0.outputs.images, False)
TableView_0.inputs.selection.set(ImageView_0.inputs.selection, False)
ImageAnnotation_0.inputs.images.set(ImageReader_0.outputs.images, False)
ImageAnnotation_0.inputs.xy.set((20, 20), False)
ImageAnnotation_0.inputs.size.set(20, False)
ImageAnnotation_0.inputs.spacing.set(0, False)
ImageAnnotation_0.inputs.color.set((255, 255, 255), False)
ImageAnnotation_0.inputs.ignore.set(['^file'], False)

# layout
tabFrame1 = pycinema.theater.TabFrame()
splitFrame1 = pycinema.theater.SplitFrame()
splitFrame1.setHorizontalOrientation()
view1 = pycinema.theater.views.NodeEditorView()
splitFrame1.insertView( 0, view1 )
splitFrame2 = pycinema.theater.SplitFrame()
splitFrame2.setVerticalOrientation()
view2 = pycinema.theater.views.FilterView( ImageView_0 )
splitFrame2.insertView( 0, view2 )
view3 = pycinema.theater.views.FilterView( TableView_0 )
splitFrame2.insertView( 1, view3 )
splitFrame2.setSizes([409, 409])
splitFrame1.insertView( 1, splitFrame2 )
splitFrame1.setSizes([508, 508])
tabFrame1.insertTab(0, splitFrame1)
tabFrame1.setTabText(0, 'Layout 1')
tabFrame1.setCurrentIndex(0)
pycinema.theater.Theater.instance.setCentralWidget(tabFrame1)

# execute pipeline
CinemaDatabaseReader_0.update()
