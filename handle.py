# -*- coding: utf-8 -*-

import hashlib
import reply
import receive
import web
from game import GameInfo

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

                content = self.process_game(ToUserName, recMsg.Content)
                import pdb;pdb.set_trace()
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "pass"
                return "success"
        except Exception, Argment:
            return Argment
    

    def process_game(self, user_id, content):
        if content.lower() == "miner":
            game = GameInfo()
            game.set_uer_id(user_id)
            if not game.read_from_file():
                return 'Send "help" to get command help'
        else:
            return 'Unkonw command'