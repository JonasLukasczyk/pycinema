from .Shader import *

import pycinema

import numpy as np
import moderngl
import PIL

class ShaderPointCloud(Shader):
    def __init__(self):

        super().__init__(
          inputs={
            'points': [],
            'resolution': (256,256),
            'camera_up': (0,1,0),
            'camera_pos': (0,0,1),
            'camera_dir': (0,0,-1)
          },
          outputs={
            'images': []
          },
          varyings=[],
          quad=False
        )

    def getVertexShaderCode(self):
        return """
#version 330
in vec3 position;

uniform mat4 projection;
uniform mat4 model_view;

void main() {
    gl_PointSize = 10.0;
    gl_Position = projection * model_view * vec4(position, 1.0);
}


"""

    def getFragmentShaderCode(self):
        return """
#version 330
layout(location=0) out vec4 outColor;
void main() {
    outColor = vec4(1.0, 0.0, 0.0, 1.0);
}
        """

    def render(self):

        Shader.fbo.clear(0.0, 0.0, 0.0, 1.0)

        # render
        # self.vao.render(moderngl.TRIANGLE_STRIP)
        self.vao.render(moderngl.POINTS)

        # create output image
        return pycinema.Image(
            {
                'rgba': self.readFramebuffer(0,4,np.uint8)
            },
            {
            }
        )

    def getRange(self,bounds,mod=0):
        if np.isscalar(bounds):
            return [bounds]

        array = np.arange(bounds[0],bounds[1]+bounds[2],bounds[2])
        if mod != 0:
            array = list(map(lambda x: x % mod, array))
            array = np.unique(array)

        return array

    def normalize(vec):
        return vec / np.sqrt(np.sum(vec**2))

    def getProjectionMatrix(znear,zfar,fovy,ratio):
        zmul = (-2.0 * znear * zfar) / (zfar - znear)
        ymul = 1.0 / np.tan(fovy * 3.14159265 / 360)
        xmul = ymul / ratio

        return np.array([
            xmul, 0.0, 0.0, 0.0,
            0.0, ymul, 0.0, 0.0,
            0.0, 0.0, -1.0, -1.0,
            0.0, 0.0, zmul, 0.0
        ]).astype('f4').tobytes()

    def getModelViewMatrix(camera_pos, camera_dir, camera_up):
        right = ShaderPointCloud.normalize(np.cross(camera_dir, camera_up))
        up_true = np.cross(right, camera_dir)

        return np.array([
            right[0], up_true[0], -camera_dir[0], 0,
            right[1], up_true[1], -camera_dir[1], 0,
            right[2], up_true[2], -camera_dir[2], 0,
            -np.dot(camera_pos, right), -np.dot(camera_pos, up_true), np.dot(camera_pos, camera_dir), 1
        ]).astype('f4').tobytes()

    def _update(self):

        points = self.inputs.points.get()
        if type(points) != np.ndarray:
            points = np.array(points)

        buffer = Shader.ctx.buffer(points.tobytes())

        self.vao = Shader.ctx.simple_vertex_array(self.program, buffer, 'position')

        # create framebuffer
        res = self.inputs.resolution.get()
        self.initFramebuffer(res,[4],['f1'])

        results = []

        # scale = [1,1,1]*10
        self.program['projection'].write(ShaderPointCloud.getProjectionMatrix(0.1,10.0,60,res[0]/res[1]))
        self.program['model_view'].write(ShaderPointCloud.getModelViewMatrix(
          [0,0,6],
          [0,0,-1],
          [0,1,0]
        ))
        results.append(
            self.render()
        )

        self.outputs.images.set(results);

        return 1;
