import mbuild as mb
import numpy as np

class FFAC27(mb.Compound):
    def __init__(self):
        """Returns a CG FFA C27 with the head-to-tail vector pointing in -z.
        """
        super(FFAC27, self).__init__()
        mb.load('ffac27.hoomdxml', compound=self, relative_to_module=self.__module__)
        self.periodicity = [0, 0, 0]
        xx = list(self.particles())
        mb.coordinate_transform.z_axis_transform(self,
                new_origin=xx[9], point_on_z_axis=xx[0])
        self.masses = [0.403639, 0.584458, 0.584458, 0.584458, 0.584458, 0.584458, 0.584458,
                  0.584458, 0.584458, 0.625247]
        self.mass = np.sum(self.masses)
        self.spin(np.pi, [1, 0, 0])
