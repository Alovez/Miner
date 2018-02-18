from time import sleep
from land import land_list
from equipment import probing_equipment_list
import csv

class GameInfo(object):
    def __init__(self):
        # flow flag
        self.loan_flag = False
        self.land_flag = False
        self.probing_equipment_flag = False
        self.probing_cost_flag = False
        self.dig_equipment_flag = True
        self.dig_cost_flag = False
        self.sell_flag = False
        self.account = 0
        self.cash = 0
        self.probing_equipment = 0
        self.land = None
        # status flag
        self.exploring_flag = False
        # uer_id
        self.user_id = 0

    def set_uer_id(self, user_id):
        self.user_id = user_id

    def write_into_file(self):
        with open('game_info_%s' % self.user_id, 'w') as f:
            fieldnames = self.__dict__.keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(self.__dict__)

    def read_from_file(self):
        try:
            with open('game_info_%s' % self.user_id, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.__dict__ = row
            return True
        except:
            self.write_into_file()
            return False


    def set_loan(self, loan):
        self.account -= loan
        self.cash += loan
        self.loan_flag = True


game = GameInfo()

import pdb;pdb.set_trace()

while True:
    if not game.loan_flag:
        game.loan = int(raw_input("Plaese input the loan: "))
        game.set_loan(game.loan)
    if not game.land_flag:
        game.land_flag = True
        land = int(raw_input("Plaese choose land in: \n 1 - SandLand1 \n 2 - SandLand2 \n 3 - GrassLand1 \n 4 - GrassLand2 \n 5 - WetLand \n 6 - GobiLand \n 7 - Mountain\n"))
        game.land = land_list[land - 1]()
        game.land.get_metal_element()
        print game.land.metal_info
    if not game.probing_equipment_flag:
        game.probing_equipment_flag = True
        probing_equipment = int(raw_input("Please choose probing land in: \n 1 - Level 1 \n 2 - Level 2 \n 3 - Level 3\n"))
        game.probing_equipment = probing_equipment_list[game.probing_equipment - 1]()
        game.exploring_flag = True
    if game.exploring_flag:
        # Explore
        ore = game.land.explore(game.probing_equipment.deep)
        # Loss
        game.probing_equipment.lost(game.land.loss)
        # Got Ore
        if ore is not None:
            game.exploring_flag = False
            command = int(raw_input("%s is Founded. Should we start to dig(1 - Yes, 2 - No):" % ore))
            if command == 1:
                game.dig_equipment_flag = False
        else:
            print "Explored %sm." % game.land.deep
        # Probing Broken
        if game.probing_equipment.health < 0:
            print "Probing is Broken!"
            game.exploring_flag = False
            break
        else:
            print "Probing Status: \n - Health: %s\n" % game.probing_equipment.health
    
    if not game.dig_equipment_flag:
        print "Game Over"
        break