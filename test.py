import pycinema
import pycinema.filters
import pycinema.theater
import pycinema.theater.views

# pycinema settings
PYCINEMA = { 'VERSION' : '3.1.0'}

# filters
CinemaDatabaseReader_0 = pycinema.filters.CinemaDatabaseReader()
TableQuery_0 = pycinema.filters.TableQuery()
TableQuery_1 = pycinema.filters.TableQuery()
ImageReader_0 = pycinema.filters.ImageReader()
ImageReader_1 = pycinema.filters.ImageReader()
ColorMapping_0 = pycinema.filters.ColorMapping()
ColorMapping_1 = pycinema.filters.ColorMapping()
ImageView_0 = pycinema.filters.ImageView()
ImageView_1 = pycinema.filters.ImageView()

# properties
CinemaDatabaseReader_0.inputs.path.set("/home/jones/projects/cinema-lib/pycinema/data/scalar-images.cdb", False)
CinemaDatabaseReader_0.inputs.file_column.set("FILE", False)
TableQuery_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
TableQuery_0.inputs.sql.set("SELECT * FROM input where object_id='s0'", False)
TableQuery_1.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
TableQuery_1.inputs.sql.set("SELECT * FROM input where object_id='s1'", False)
ImageReader_0.inputs.table.set(TableQuery_1.outputs.table, False)
ImageReader_0.inputs.file_column.set("FILE", False)
ImageReader_0.inputs.cache.set(True, False)
ImageReader_1.inputs.table.set(TableQuery_0.outputs.table, False)
ImageReader_1.inputs.file_column.set("FILE", False)
ImageReader_1.inputs.cache.set(True, False)
ColorMapping_0.inputs.map.set("gray", False)
ColorMapping_0.inputs.nan.set((1, 1, 1, 1), False)
ColorMapping_0.inputs.range.set((0, 1), False)
ColorMapping_0.inputs.channel.set("depth", False)
ColorMapping_0.inputs.images.set(ImageReader_0.outputs.images, False)
ColorMapping_0.inputs.composition_id.set(-1, False)
ColorMapping_1.inputs.map.set("plasma", False)
ColorMapping_1.inputs.nan.set((1, 1, 1, 1), False)
ColorMapping_1.inputs.range.set((0, 1), False)
ColorMapping_1.inputs.channel.set("depth", False)
ColorMapping_1.inputs.images.set(ImageReader_1.outputs.images, False)
ColorMapping_1.inputs.composition_id.set(-1, False)
ImageView_0.inputs.images.set(ColorMapping_0.outputs.images, False)
ImageView_0.inputs.selection.set([], False)
ImageView_1.inputs.images.set(ColorMapping_1.outputs.images, False)
ImageView_1.inputs.selection.set([], False)

# layout
tabFrame0 = pycinema.theater.TabFrame()
splitFrame0 = pycinema.theater.SplitFrame()
splitFrame0.setHorizontalOrientation()
view0 = pycinema.theater.views.NodeEditorView()
splitFrame0.insertView( 0, view0 )
splitFrame1 = pycinema.theater.SplitFrame()
splitFrame1.setVerticalOrientation()
view4 = pycinema.theater.views.FilterView( ColorMapping_0 )
splitFrame1.insertView( 0, view4 )
view5 = pycinema.theater.views.FilterView( ColorMapping_1 )
splitFrame1.insertView( 1, view5 )
splitFrame1.setSizes([667, 667])
splitFrame0.insertView( 1, splitFrame1 )
splitFrame2 = pycinema.theater.SplitFrame()
splitFrame2.setVerticalOrientation()
view7 = pycinema.theater.views.FilterView( ImageView_0 )
splitFrame2.insertView( 0, view7 )
view8 = pycinema.theater.views.FilterView( ImageView_1 )
splitFrame2.insertView( 1, view8 )
splitFrame2.setSizes([667, 667])
splitFrame0.insertView( 2, splitFrame2 )
splitFrame0.setSizes([1703, 1702, 1703])
tabFrame0.insertTab(0, splitFrame0)
tabFrame0.setTabText(0, 'Layout 1')
tabFrame0.setCurrentIndex(0)
pycinema.theater.Theater.instance.setCentralWidget(tabFrame0)

# execute pipeline
CinemaDatabaseReader_0.update()
