# -*- coding: UTF-8 -*-
import json
import os, sys

import tornado.ioloop
import tornado.web
from model.websocket_handler import ChatWebSocket
from model.login import login, register
from model.message_history import MessageHistory

app = tornado.web.Application([
    (r"/chat", ChatWebSocket),
    (r"/login.do", login),
    (r"/register.do", register),
    (r"/message_history.do", MessageHistory),


])

if __name__ == '__main__':
    print os.path.join(os.path.dirname(__file__), 'js')
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
