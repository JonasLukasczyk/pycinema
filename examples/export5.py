
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
ImageViewer_0 = vf3.convert( pycinema.explorer.ImageViewer )
vf4 = vf2.widget(1)
ColorMappingView_0 = vf4.convert( pycinema.explorer.ColorMappingView )

# filters
CinemaDatabaseReader_0 = pycinema.filters.CinemaDatabaseReader()
TableQuery_0 = pycinema.filters.TableQuery()
ImageReader_0 = pycinema.filters.ImageReader()
DepthCompositing_0 = pycinema.filters.DepthCompositing()

# properties
ImageViewer_0.inputs.images.set(ColorMappingView_0.outputs.images, False)
ColorMappingView_0.inputs.images.set(DepthCompositing_0.outputs.images, False)
ColorMappingView_0.inputs.channel.set("y", False)
ColorMappingView_0.inputs.map.set("RdGy", False)
ColorMappingView_0.inputs.range.set((0, 1), False)
ColorMappingView_0.inputs.nan.set((1, 1, 1, 1), False)
ColorMappingView_0.inputs.composition_id.set(-1, False)
CinemaDatabaseReader_0.inputs.path.set("/home/jones/external/projects/cinema-lib/pycinema/data/ScalarImages.cdb/", False)
CinemaDatabaseReader_0.inputs.file_column.set("file", False)
TableQuery_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
TableQuery_0.inputs.sql.set("SELECT * FROM input LIMIT 3", False)
ImageReader_0.inputs.table.set(TableQuery_0.outputs.table, False)
ImageReader_0.inputs.file_column.set("FILE", False)
ImageReader_0.inputs.cache.set(True, False)
DepthCompositing_0.inputs.images_a.set(ImageReader_0.outputs.images, False)
DepthCompositing_0.inputs.images_b.set([], False)
DepthCompositing_0.inputs.depth_channel.set("depth", False)
DepthCompositing_0.inputs.composite_by_meta.set((None, {}), False)

# execute pipeline
ImageViewer_0.update()
