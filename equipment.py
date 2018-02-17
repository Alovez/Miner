class BaseEquipment(object):
    def __init__(self):
        self.level = 0
        self.health = 0


class BaseProbingEquipment(BaseEquipment):
    def __init__(self):
        super(BaseProbingEquipment, self).__init__()
        self.loss = 0
        self.level = 0
        self.deep = 0
        self.cost = 0
        self.health = 400
    
    def lost(self, loss_scale):
        if self.health >= 800:
            self.health -= 1.02 * loss_scale[self.level]
        elif self.health >= 500:
            self.health -= 1.03 * loss_scale[self.level]
        elif self.health >= 100:
            self.health -= 1.05 * loss_scale[self.level]
        else:
            self.health -= 1.06 * loss_scale[self.level]


class ProbingEquipmentLevel1(BaseProbingEquipment):
    def __init__(self):
        super(ProbingEquipmentLevel1, self).__init__()
        self.deep = 10
        self.level = 1
        self.cost = 50


class ProbingEquipmentLevel2(BaseProbingEquipment):
    def __init__(self):
        super(ProbingEquipmentLevel2, self).__init__()
        self.deep = 15
        self.level = 2
        self.cost = 100


class ProbingEquipmentLevel3(BaseProbingEquipment):
    def __init__(self):
        super(ProbingEquipmentLevel3, self).__init__()
        self.deep = 25
        self.level = 3
        self.cost = 80

probing_equipment_list = [ProbingEquipmentLevel1, ProbingEquipmentLevel2, ProbingEquipmentLevel3]


class BaseDigEquipment(BaseEquipment):
    def __init__(self):
        super(BaseDigEquipment, self).__init__()
        