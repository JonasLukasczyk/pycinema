
import pycinema
import pycinema.filters
import pycinema.designer
import pycinema.designer.views

# layout
vf0 = pycinema.designer.Designer.instance.centralWidget()
vf0.setHorizontalOrientation()
vf0.insertView( 0, pycinema.designer.views.NodeView() )
TableView_0 = vf0.insertView( 1, pycinema.designer.views.TableView() )
vf0.setSizes([510, 510])

# filters
CinemaDatabaseReader_0 = pycinema.filters.CinemaDatabaseReader()
TableQuery_0 = pycinema.filters.TableQuery()

# properties
CinemaDatabaseReader_0.inputs.path.set("", False)
CinemaDatabaseReader_0.inputs.file_column.set("file", False)
TableQuery_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
TableQuery_0.inputs.sql.set("SELECT * FROM input", False)
TableView_0.inputs.table.set(TableQuery_0.outputs.table, False)

# execute pipeline
CinemaDatabaseReader_0.update()
