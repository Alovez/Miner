# -*- coding: utf-8 -*-

import hashlib
import reply
import receive
import web
from game import GameInfo
import command_state

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

        game = GameInfo()
        game.set_user_id(user_id)
        game.read_from_file()

        if content.lower() == 'help':
            return "***********\n1.start: Start New Game\n2.state: Get the state\n***********"
        elif content.lower() == 'yes':
            return game.process_yes()
        elif content.lower() == 'no':
            return game.process_no()
        elif content.lower() == 'start':
            if game.read_from_file():
                game.set_state(command_state.WAITING_START_NEW_GAME)
                return "Last game is still running. \n\nDo you want to *terminal* the last game and start new game?\n\n('yes' to start new game, 'no' to return last game)"
            else:
                return 'Game start'
        elif content.lower() == 'state':
            game.get_state()
        elif content.lower() == 'loan':
            game = GameInfo()
            game.set_uer_id(user_id)
            game.read_from_file()
            return game.get_state()
        else:
            print 'enter unkown'
            return 'Unkonw\ncommand'
