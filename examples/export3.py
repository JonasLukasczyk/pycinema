
import pycinema
import pycinema.filters
import pycinema.explorer

        
# layout
vf0 = pycinema.explorer.Explorer.window.centralWidget()
vf0.s_splitH()
vf1 = vf0.widget(0)
vf2 = vf0.widget(1)
vf2.s_splitV()
vf3 = vf2.widget(0)
vf3.s_splitH()
vf5 = vf3.widget(0)
TableViewer_0 = vf5.convert( pycinema.explorer.TableViewer )
vf6 = vf3.widget(1)
TableViewer_1 = vf6.convert( pycinema.explorer.TableViewer )
vf4 = vf2.widget(1)
vf4.s_splitV()
vf7 = vf4.widget(0)
ParameterViewer_0 = vf7.convert( pycinema.explorer.ParameterViewer )
vf8 = vf4.widget(1)
vf8.s_splitH()
vf9 = vf8.widget(0)
ImageViewer_0 = vf9.convert( pycinema.explorer.ImageViewer )
vf10 = vf8.widget(1)
ImageViewer_1 = vf10.convert( pycinema.explorer.ImageViewer )

# filters
CinemaDatabaseReader_0 = pycinema.filters.CinemaDatabaseReader()
TableQuery_0 = pycinema.filters.TableQuery()
ImageReader_0 = pycinema.filters.ImageReader()
DepthCompositing_0 = pycinema.filters.DepthCompositing()
ShaderSSAO_0 = pycinema.filters.ShaderSSAO()
ShaderFXAA_0 = pycinema.filters.ShaderFXAA()

# properties
TableViewer_0.inputs.table.set(TableQuery_0.outputs.table, False)
TableViewer_1.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
ParameterViewer_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
ParameterViewer_0.inputs.ignore.set(['file', 'id', 'object_id_name'], False)
ParameterViewer_0.inputs.state.set({'time': {'C': False, 'T': 'S', 'S': 1, 'O': [0]}, 'phi': {'C': False, 'T': 'S', 'S': 2, 'O': [0]}, 'theta': {'C': False, 'T': 'S', 'S': 1, 'O': [0]}, 'object_id': {'C': True, 'T': 'O', 'S': 0, 'O': [0, 1, 2]}}, False)
ImageViewer_0.inputs.images.set(ShaderFXAA_0.outputs.images, False)
ImageViewer_1.inputs.images.set(DepthCompositing_0.outputs.images, False)
CinemaDatabaseReader_0.inputs.path.set("/home/jones/external/projects/cinema-lib/pycinema/data/ScalarImages.cdb/", False)
CinemaDatabaseReader_0.inputs.file_column.set("file", False)
TableQuery_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
TableQuery_0.inputs.sql.set(ParameterViewer_0.outputs.sql, False)
ImageReader_0.inputs.table.set(TableQuery_0.outputs.table, False)
ImageReader_0.inputs.file_column.set("FILE", False)
ImageReader_0.inputs.cache.set(True, False)
DepthCompositing_0.inputs.images_a.set(ImageReader_0.outputs.images, False)
DepthCompositing_0.inputs.images_b.set([], False)
DepthCompositing_0.inputs.depth_channel.set("depth", False)
DepthCompositing_0.inputs.composite_by_meta.set(ParameterViewer_0.outputs.composite_by_meta, False)
ShaderSSAO_0.inputs.images.set(DepthCompositing_0.outputs.images, False)
ShaderSSAO_0.inputs.radius.set(0.03, False)
ShaderSSAO_0.inputs.samples.set(128, False)
ShaderSSAO_0.inputs.diff.set(0.5, False)
ShaderFXAA_0.inputs.images.set(ShaderSSAO_0.outputs.images, False)

# execute pipeline
TableViewer_0.update()
