
import pycinema
import pycinema.filters
import pycinema.designer
import pycinema.designer.views

# layout
pycinema.designer.Designer.instance.nodeView.setVisible(True)
vf0 = pycinema.designer.Designer.instance.centralWidget()
vf0.setHorizontalOrientation()
vf1 = vf0.insertFrame(0)
vf1.setVerticalOrientation()
TableView_0 = vf1.insertView( 1, pycinema.designer.views.TableView() )
vf1.setSizes([432, 431])
ImageView_0 = vf0.insertView( 1, pycinema.designer.views.ImageView() )
vf0.setSizes([510, 510])

# filters

# properties
TableView_0.inputs.table.set([[]], False)
ImageView_0.inputs.images.set([], False)

# execute pipeline
TableView_0.update()
