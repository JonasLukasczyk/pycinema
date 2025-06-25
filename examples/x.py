
import pycinema
import pycinema.filters
import pycinema.designer
import pycinema.designer.views

# layout
vf1 = pycinema.designer.Designer.instance.centralWidget()
vf1.setVerticalOrientation()
vf2 = vf1.insertFrame(0)
vf2.setHorizontalOrientation()
vf2.insertView( 0, pycinema.designer.views.NodeView() )
ImageView_0 = vf2.insertView( 1, pycinema.designer.views.ImageView() )
vf2.setSizes([510, 510])
vf3 = vf1.insertFrame(1)
vf3.setHorizontalOrientation()
TableView_0 = vf3.insertView( 0, pycinema.designer.views.TableView() )
vf3.insertView( 1, pycinema.designer.views.NodeView() )
vf3.setSizes([510, 510])
vf1.setSizes([432, 431])

# filters
CinemaDatabaseReader_0 = pycinema.filters.CinemaDatabaseReader()

# properties
ImageView_0.inputs.images.set([], False)
TableView_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
CinemaDatabaseReader_0.inputs.path.set("", False)
CinemaDatabaseReader_0.inputs.file_column.set("file", False)

# execute pipeline
ImageView_0.update()
