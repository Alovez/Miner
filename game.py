from time import sleep
from land import land_list
from equipment import probing_equipment_list
from land import BaseLand
import command_state
import csv
import json
import os
import copy
import pickle

class GameInfo(object):
    def __init__(self, user_id):
        # flow flag
        self.command_state = command_state.WAITING_SET_LOAN
        self.last_state = command_state.WAITING_SET_LOAN
        self.account = 0
        self.cash = 0
        self.probing_equipment = 'n/a'
        self.dig_equipment = 'n/a'
        self.land = 'n/a'
        # uer_id
        self.user_id = user_id

    def process_yes(self):
        print self.command_state
        if self.command_state == command_state.WAITING_START_NEW_GAME:
            self.set_state(command_state.WAITING_SET_LOAN)
            os.system('rm -f game_info_%s' % self.user_id)
            os.system('rm -f land_info_%s' % self.user_id)
            return 'New Game Started.'
        else:
            return 'Not In The Interactive'

    def process_no(self):
        print self.command_state
        if self.command_state == command_state.WAITING_START_NEW_GAME:
            self.set_state(self.last_state)
            return 'Reload Last Game.'
        else:
            return 'Not In The Interactive'
    
    def process_num(self, num):
        print num
        if self.command_state == command_state.WAITING_CHOOSE_LAND:
            self.land = land_list[int(num) - 1](self.user_id)
            self.land.get_metal_element()
            self.set_state(command_state.WAITING_CHOOSE_PROBING_EQUIPMENT)
            return '%s is chosen.\n\n(DEBUG: Ore info: %s)' % (self.land.name, self.land.metal_info)
        else:
            return 'Not In The Interactive'

    def set_state(self, state):
        self.last_state = self.command_state
        self.command_state = state

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_stage(self):
        if self.command_state == command_state.WAITING_SET_LOAN:
            return 'Waiting to set loan...'
        else:
            return 'Game Over'

    def get_state(self):
        return "**********\nAccount: %s\nCash: %s\nLand: %s\nProbing Equipment:%s\nDig Equipment:%s\n**********" % (self.account, self.cash, self.land, self.probing_equipment, self.dig_equipment)

    def set_loan(self, loan):
        self.account -= loan
        self.cash += loan
        self.loan_flag = True


# game = GameInfo()
# game.set_user_id(1)
# game.land = land_list[2](1)
# game.land.get_metal_element()

# print game.land.metal_info
# print type(game.land)

# with open('game_info_%s' % 1, 'w') as f:
#     picklestring = pickle.dump(game, f)

# # import pdb;pdb.set_trace()

# with open('game_info_%s' % 1, 'r') as f:
#     game = pickle.load(f)


# print game.land.metal_info

# print type(game.land)

# while True:
#     if not game.loan_flag:
#         game.loan = int(raw_input("Plaese input the loan: "))
#         game.set_loan(game.loan)
#     if not game.land_flag:
#         game.land_flag = True
#         land = int(raw_input("Plaese choose land in: \n 1 - SandLand1 \n 2 - SandLand2 \n 3 - GrassLand1 \n 4 - GrassLand2 \n 5 - WetLand \n 6 - GobiLand \n 7 - Mountain\n"))
#         game.land = land_list[land - 1]()
#         game.land.get_metal_element()
#         print game.land.metal_info
#     if not game.probing_equipment_flag:
#         game.probing_equipment_flag = True
#         probing_equipment = int(raw_input("Please choose probing land in: \n 1 - Level 1 \n 2 - Level 2 \n 3 - Level 3\n"))
#         game.probing_equipment = probing_equipment_list[game.probing_equipment - 1]()
#         game.exploring_flag = True
#     if game.exploring_flag:
#         # Explore
#         ore = game.land.explore(game.probing_equipment.deep)
#         # Loss
#         game.probing_equipment.lost(game.land.loss)
#         # Got Ore
#         if ore is not None:
#             game.exploring_flag = False
#             command = int(raw_input("%s is Founded. Should we start to dig(1 - Yes, 2 - No):" % ore))
#             if command == 1:
#                 game.dig_equipment_flag = False
#         else:
#             print "Explored %sm." % game.land.deep
#         # Probing Broken
#         if game.probing_equipment.health < 0:
#             print "Probing is Broken!"
#             game.exploring_flag = False
#             break
#         else:
#             print "Probing Status: \n - Health: %s\n" % game.probing_equipment.health
    
#     if not game.dig_equipment_flag:
#         print "Game Over"
#         break