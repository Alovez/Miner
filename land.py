import constants
import numpy

class BaseLand(object):
    def __init__(self):
        self.deep = 0
        self.metal_delta = {}
        self.dimond_scale = 0
        # metal num
        self.metal_num = {}
        self.metal_info = {}
        self.loss = {}

    def explore(self, deep):
        info = None
        for i in range(deep + 1):
            if self.metal_info.get(self.deep - i, None) is not None:
                info = self.metal_info.get(self.deep - i, None)
        self.deep -= deep
        return info

    def get_ore_num(self, metal):
        num = 0
        for _ in range(5):
            if numpy.random.random_sample() < (constants.METAL_SCALE[metal] + self.metal_delta[metal]):
                num += 1
            else:
                break
        self.metal_num[metal] = num

    def get_metal_element(self):
        for metal in constants.METAL_LIST:
            self.get_ore_num(metal)
            center = constants.METAL_DEEP[metal]
            width = constants.METAL_DEEP_WIDTH[metal]
            if self.metal_num[metal] != 0:
                ore_info = numpy.round(numpy.random.normal(center, width, self.metal_num[metal]), 0)
                for pos in ore_info:
                    self.metal_info[pos] = metal


class SandLand1(BaseLand):
    def __init__(self):
        super(SandLand1, self).__init__()
        self.metal_delta[constants.AL] = 0.005
        self.metal_delta[constants.FE] = 0.001
        self.metal_delta[constants.CU] = 0.001
        self.metal_delta[constants.AG] = 0.003
        self.metal_delta[constants.AU] = 0.003
        self.metal_delta[constants.DIMOND] = 0.003
        self.loss[1] = 1.5
        self.loss[2] = 2.5
        self.loss[3] = 3.5


class SandLand2(BaseLand):
    def __init__(self):
        super(SandLand2, self).__init__()
        self.metal_delta[constants.AL] = 0.008
        self.metal_delta[constants.FE] = 0.001
        self.metal_delta[constants.CU] = 0.001
        self.metal_delta[constants.AG] = 0.003
        self.metal_delta[constants.AU] = 0.003
        self.metal_delta[constants.DIMOND] = 0.003
        self.loss[1] = 1.5
        self.loss[2] = 2.5
        self.loss[3] = 3.5


class GrassLand1(BaseLand):
    def __init__(self):
        super(GrassLand1, self).__init__()
        self.metal_delta[constants.AL] = - 0.005	
        self.metal_delta[constants.FE] = 0.002
        self.metal_delta[constants.CU] = 0.002
        self.metal_delta[constants.AG] = 0.001
        self.metal_delta[constants.AU] = 0.001	
        self.metal_delta[constants.DIMOND] = 0.001
        self.loss[1] = 1
        self.loss[2] = 2
        self.loss[3] = 3


class GrassLand2(BaseLand):
    def __init__(self):
        super(GrassLand2, self).__init__()
        self.metal_delta[constants.AL] = - 0.008
        self.metal_delta[constants.FE] = 0.005
        self.metal_delta[constants.CU] = 0.001
        self.metal_delta[constants.AG] = 0.001
        self.metal_delta[constants.AU] = 0.001	
        self.metal_delta[constants.DIMOND] = 0.001
        self.loss[1] = 1
        self.loss[2] = 2
        self.loss[3] = 3


class WetLand(BaseLand):
    def __init__(self):
        super(WetLand, self).__init__()
        self.metal_delta[constants.AL] = -0.01
        self.metal_delta[constants.FE] = -0.01
        self.metal_delta[constants.CU] = -0.01
        self.metal_delta[constants.AG] = -0.01
        self.metal_delta[constants.AU] = -0.01
        self.metal_delta[constants.DIMOND] = 0.005
        self.loss[1] = 2
        self.loss[2] = 2.5
        self.loss[3] = 3.5


class GobiLand(BaseLand):
    def __init__(self):
        super(GobiLand, self).__init__()
        self.metal_delta[constants.AL] = 0.008
        self.metal_delta[constants.FE] = 0.008
        self.metal_delta[constants.CU] = 0.01
        self.metal_delta[constants.AG] = 0.01
        self.metal_delta[constants.AU] = 0.008
        self.metal_delta[constants.DIMOND] = 0.005
        self.loss[1] = 3
        self.loss[2] = 6
        self.loss[3] = 12


class Mountain(BaseLand):
     def __init__(self):
        super(Mountain, self).__init__()
        self.metal_delta[constants.AL] = 0.005
        self.metal_delta[constants.FE] = 0.008
        self.metal_delta[constants.CU] = 0.001
        self.metal_delta[constants.AG] = 0.002
        self.metal_delta[constants.AU] = 0.005
        self.metal_delta[constants.DIMOND] = 0.002
        self.loss[1] = 1.5
        self.loss[2] = 3
        self.loss[3] = 3.5
        self.deep = 500


land_list = [SandLand1, SandLand2, GrassLand1, GrassLand2, WetLand, GobiLand, Mountain]