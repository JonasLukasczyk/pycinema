from pycinema import Filter
import time

class PerformanceTest(Filter):

    def __init__(self):
        Filter.__init__(
          self,
          inputs = {
            'a': 0,
            't': 2
          },
          outputs = {
            'b': 1
          }
        )

    def _update(self):
        a = self.inputs.a.get()
        b = a+1

        time.sleep(self.inputs.t.get())

        if b>1: raise Exception('Result not allowed to be larger 1')

        self.outputs.b.set(b)
        return 1
