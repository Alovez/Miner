from time import sleep
from land import land_list

class GameInfo(object):
    def __init__(self):
        self.loan_flag = False
        self.land_flag = False
        self.probing_equipment_flag = False
        self.probing_cost_flag = False
        self.dig_equipment_flag = False
        self.dig_cost_flag = False
        self.sell_flag = False
        self.account = 0
        self.cash = 0

    def set_loan(self, loan):
        self.account -= loan
        self.cash += loan
        self.loan_flag = True





game = GameInfo()

while True:
    if not game.loan_flag:
        game.loan = int(raw_input("Plaese input the loan: "))
        game.set_loan(game.loan)
    if not game.land_flag:
        game.land = int(raw_input("Plaese choose land in: \n 1 - SandLand1 \n 2 - SandLand2 \n 3 - GrassLand1 \n 4 - GrassLand2 \n 5 - WetLand \n 6 - GobiLand \n 7 - Mountain : \n"))
        game.new_land = land_list[game.land]()
        game.new_land.get_metal_element()
        print game.new_land.metal_num
        print game.new_land.metal_info
    break