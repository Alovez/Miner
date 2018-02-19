# -*- coding: utf-8 -*-

import hashlib
import reply
import receive
import web
from game import GameInfo
import command_state
import pickle

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "aloveztoken"

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                # content = self.process_game(ToUserName, recMsg.Content)
                # import pdb;pdb.set_trace()
                content = self.process_game(fromUser, recMsg.Content)
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "pass"
                return "success"
        except Exception, Argment:
            return Argment
    
    def process_game(self, user_id, content):
        print '*' * 80
        print 'user_id = %s' % user_id
        print 'content = %s' % content
        print '*' * 80
        game = None
        if content.lower() == 'help':
            return "***********\n1.start: Start New Game\n2.state: Get the state\n3.loan: Loan From Bank\n4.land: Choose land\n5.prob: Choose Probing Equipment\n*.next: Get Next Step\n***********"
        try:
            with open('game_info_%s' % user_id, 'r') as f:
                game = pickle.load(f)
        except:
            game = GameInfo(user_id)
            with open('game_info_%s' % user_id, 'w') as f:
                picklestring = pickle.dump(game, f)
            return "There's no game running. New Game Started."
        content_text = self.get_content(game, content)
        with open('game_info_%s' % user_id, 'w') as f:
            picklestring = pickle.dump(game, f)
        return content_text

    def get_content(self, game, content):
        if content.lower() == 'yes':
            return game.process_yes()
        elif content.lower() == 'no':
            return game.process_no()
        elif content.lower() in '1234567890':
            return game.process_num(content.lower())
        elif content.lower() == 'start':
            game.set_state(command_state.WAITING_START_NEW_GAME)
            return "Last game is still running. \n\nDo you want to *terminal* the last game and start new game?\n\n('yes' to start new game, 'no' to return last game)"
        elif content.lower() == 'state':
            return game.get_state()
        elif content.lower()[:4] == 'loan':
            try:
                number = float(content.lower()[5:])
                game.set_loan(number)
                game.set_state(command_state.FINISH_SET_LOAN)
            except:
                return "command 'loan' must with a number parameter"
            return game.get_state()
        elif content.lower() == 'land':
            if game.land == 'n/a':
                game.set_state(command_state.WAITING_CHOOSE_LAND)
                return 'Plaese choose land in: \n 1 - SandLand1 \n 2 - SandLand2 \n 3 - GrassLand1 \n 4 - GrassLand2 \n 5 - WetLand \n 6 - GobiLand \n 7 - Mountain\n'
            else:
                return '%s is chosen.\n\n(DEBUG: Ore info: %s)' % (game.land.name, game.land.metal_info)
        elif content.lower() == 'prob':
            if game.probing_equipment == 'n/a':
                game.set_state(command_state.WAITING_CHOOSE_PROBING_EQUIPMENT)
                return 'Plaese choose Probing Equipment in: \n 1 - Level 1 \n 2 - Level 2 \n 3 - Level 3 \n'
            else:
                return 'Level %s is chosen. Heath is: %s' % (game.probing_equipment.level, game.probing_equipment.health)
        elif content.lower() == 'next':
            return game.process_next()
        else:
            print 'Enter unkown'
            return 'Unkonw\ncommand'


# handle = Handle()
# while True:
#     content = raw_input('command: ')
#     print handle.process_game(1,content)