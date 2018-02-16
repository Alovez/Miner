import constants
import numpy

class BaseLand(object):
    def __init__():
        self.deep = 0
        self.metal_delta = {}
        self.dimond_scale = 0
        # metal num
        self.metal_num = {}
        self.metal_info = {}

    def dig(deep):
        self.deep -= deep

    def get_ore_num(metal):
        num = 0
        for _ in range(5):
            if numpy.random.random_sample() < (constants.METAL_SCALE[metal] + self.metal_delta[metal]):
                num += 1
            else:
                break
        self.metal_num[metal] = num

    def get_metal_element():
        for metal in constants.METAL_LIST:
            self.get_ore_num(metal)
            center = constants.METAL_DEEP[metal]
            width = constants.METAL_DEEP_WIDTH[metal]
            ore_info = int(numpy.round(numpy.random.normal(center, width, self.metal_num[metal]), 0))
            self.metal_info[ore_info] = metal


class SandLand1(BaseLand):
    def __init__():
        self.metal_delta[constants.AL] = 0.005
        self.metal_delta[constants.FE] = 0.001
        self.metal_delta[constants.CU] = 0.001
        self.metal_delta[constants.AG] = 0.003
        self.metal_delta[constants.AU] = 0.003
        self.metal_delta[constants.DIMOND] = 0.003


class SandLand2(BaseLand):
    def __init__():
        self.metal_delta[constants.AL] = 0.008
        self.metal_delta[constants.FE] = 0.001
        self.metal_delta[constants.CU] = 0.001
        self.metal_delta[constants.AG] = 0.003
        self.metal_delta[constants.AU] = 0.003
        self.metal_delta[constants.DIMOND] = 0.003


class GrassLand1(BaseLand):
    def __init__():
        self.metal_delta[constants.AL] = - 0.005	
        self.metal_delta[constants.FE] = 0.002
        self.metal_delta[constants.CU] = 0.002
        self.metal_delta[constants.AG] = 0.001
        self.metal_delta[constants.AU] = 0.001	
        self.metal_delta[constants.DIMOND] = 0.001