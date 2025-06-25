# from .FilterView import ViewFilter

# import numpy
# # import PIL
# import moderngl
# from PySide6 import QtCore, QtWidgets, QtGui, QtOpenGL, QtOpenGLWidgets
# import time

# from PySide6.QtOpenGL import (QOpenGLBuffer, QOpenGLShader, QOpenGLShaderProgram)


# def getProjectionMatrix(znear,zfar,fovy,ratio):
#     zmul = (-2.0 * znear * zfar) / (zfar - znear)
#     ymul = 1.0 / np.tan(fovy * 3.14159265 / 360)
#     xmul = ymul / ratio

#     return np.array([
#         xmul, 0.0, 0.0, 0.0,
#         0.0, ymul, 0.0, 0.0,
#         0.0, 0.0, -1.0, -1.0,
#         0.0, 0.0, zmul, 0.0
#     ]).astype('f4').tobytes()

# def getModelViewMatrix(camera_pos, camera_dir, camera_up):
#     right = ShaderPointCloud.normalize(np.cross(camera_dir, camera_up))
#     up_true = np.cross(right, camera_dir)

#     return np.array([
#         right[0], up_true[0], -camera_dir[0], 0,
#         right[1], up_true[1], -camera_dir[1], 0,
#         right[2], up_true[2], -camera_dir[2], 0,
#         -np.dot(camera_pos, right), -np.dot(camera_pos, up_true), np.dot(camera_pos, camera_dir), 1
#     ]).astype('f4').tobytes()

# class Canvas( QtOpenGLWidgets.QOpenGLWidget ):
#     def __init__(self,parent):
#         super().__init__(parent=parent)

#         format = QtGui.QSurfaceFormat()
#         format.setVersion(3, 3)
#         format.setProfile(QtGui.QSurfaceFormat.CoreProfile)
#         format.setSamples(0)
#         self.setFormat(format)
#         self.ctx = None
#         self.t0 = time.time()

#     def initializeGL(self):
#         pass

#     def resizeGL(self,w,h):
#         pass
#         # m_projection.setToIdentity()
#         # m_projection.perspective(45.0, w / h, 0.01, 100.0)

#     def paintGL(self):
#         if not self.ctx:
#             self.ctx = moderngl.create_context()
#             self.quad = self.ctx.buffer(
#                 numpy.array([
#                     1.0,  1.0,
#                     -1.0,  1.0,
#                     -1.0, -1.0,
#                     1.0, -1.0,
#                     1.0,  1.0
#                 ]).astype('f4').tobytes()
#             )
#             self.program = self.ctx.program(
#                 vertex_shader='''
#     #version 330
#     in vec2 position;
#     out vec2 uv;
#     void main(){
#     uv = position/2.0+0.5;
#     gl_Position = vec4(position,0,1);
#     }
#                 ''',
#                 fragment_shader='''
#     #version 330

#     in vec2 uv;
#     out vec4 color;

#     void main(){
#     color = vec4(uv,0.0,1.0);
#     }
#                 ''',
#                 varyings=['uv']
#             )
#             self.vao = self.ctx.simple_vertex_array(self.program, self.quad, 'position')

#         # self.ctx.clear(0.0, 1.0, 1.0, 1.0)
#         self.vao.render(moderngl.TRIANGLE_STRIP)


# class OpenGLViewer(ViewFilter):

#     def __init__(self, view):
#         self.canvas = Canvas(view.content)

#         view.content.layout().addWidget(self.canvas,1)
#         # view.content.layout().addWidget(self.canvas)

#         super().__init__(
#           inputs={
#             'geometry': []
#           }
#         )

#     def _update(self):



#         return 1
