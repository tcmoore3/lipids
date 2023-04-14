import mbuild as mb
import numpy as np

class Cer1(mb.Compound):
    def __init__(self):
        """Returns a CG uCER1 with the head-to-tail vector pointing in -z.
        """
        super(Cer1, self).__init__()
        mb.load('cer1_mapping2.hoomdxml', compound=self, relative_to_module=self.__module__)
        xx = list(self.particles())
        mb.coordinate_transform.z_axis_transform(self,
                new_origin=xx[18], point_on_z_axis=xx[24])
        self.translate([-self.center[0], -self.center[1], 0])  # center in xy plane
        masses = [
                    0.403639, 0.584458, 0.584458, 0.584458, 0.584458,
                    0.584458, 0.610727, 0.584458, 0.584458, 0.584458,
                    0.584458, 0.584458, 0.584458, 0.584458, 0.584458,
                    0.584458, 0.584458, 0.597575, 0.556458, 0.584458,
                    0.584458, 0.584458, 0.584458, 0.584458, 0.236214,
                    0.236214, 0.208819
                    ]
                        
        for p, m in zip(self.particles(), masses):
            p.mass = m
        #self.mass = np.sum(self.masses)
        self.rotate(np.pi, [1, 0, 0])
