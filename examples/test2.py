
import pycinema
import pycinema.filters
import pycinema.designer
import pycinema.designer.views

# layout
pycinema.designer.Designer.instance.nodeView.setVisible(True)
vf0 = pycinema.designer.Designer.instance.centralWidget()
vf0.setVerticalOrientation()
ParallelCoordinatesView_1 = vf0.insertView( 1, pycinema.designer.views.ParallelCoordinatesView() )
vf0.setSizes([432, 431])

# filters
CinemaDatabaseReader_0 = pycinema.filters.CinemaDatabaseReader()

# properties
CinemaDatabaseReader_0.inputs.path.set("/home/jones/external/projects/cinema-lib/pycinema/data/ScalarImages.cdb", False)
CinemaDatabaseReader_0.inputs.file_column.set("file", False)
ParallelCoordinatesView_1.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
ParallelCoordinatesView_1.inputs.ignore.set(['file', 'id', 'object_id_name'], False)
ParallelCoordinatesView_1.inputs.state.set({}, False)

# execute pipeline
CinemaDatabaseReader_0.update()
