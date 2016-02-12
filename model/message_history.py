# -*- coding: UTF-8 -*-
from lib.request_manager import SuperRequestHandler
from applib.user_lib import UserLib
from applib.message_lib import MessageLib

from tornado import gen

class MessageHistory(SuperRequestHandler):
    """ Renders the index file """
    @gen.coroutine
    def get(self):
        uid = self.post_data.get('uid', '')
        password = self.post_data.get('password', '')
        last_msg_id = self.post_data.get('last_msg_id', '')

        res = yield UserLib.check_user(uid, password)
        if res:
            message_history = yield MessageLib.get_message_history(uid, last_msg_id)
            self.writeS({"data": message_history, "code": 0})
        else:
            self.writeS({"data": "Error login info !!", "code": 1})
            return
