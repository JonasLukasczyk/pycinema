
import pycinema
import pycinema.filters
import pycinema.designer
import pycinema.designer.views

# layout
pycinema.designer.Designer.instance.nodeView.setVisible(True)
vf0 = pycinema.designer.Designer.instance.centralWidget()
vf0.setVerticalOrientation()
ImageView_0 = vf0.insertView( 1, pycinema.designer.views.ImageView() )
vf0.setSizes([432, 431])

# filters

# properties
ImageView_0.inputs.images.set([], False)

# execute pipeline
ImageView_0.update()
