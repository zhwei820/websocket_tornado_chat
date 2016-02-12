# -*- coding: UTF-8 -*-
from lib.request_manager import SuperRequestHandler
from applib.user_lib import UserLib
from tornado import gen

class login(SuperRequestHandler):
    """ Renders the index file """
    @gen.coroutine
    def get(self):
        pnum = self.post_data.get('pnum', '')
        password = self.post_data.get('password', '')
        user_info = yield UserLib.get_user_by_pnum(pnum)
        if user_info and user_info.get('password', 0) == self.get_password(password):
            self.writeS({"data": user_info, "code": 0})
            return
        elif user_info:
            self.writeS({"data": "Error login info !!", "code": 1})
            return
        self.writeS({"data": "Phone number not registered", "code": 2})
        return

class register(SuperRequestHandler):
    """ Renders the index file """
    @gen.coroutine
    def post(self):
        pnum = self.post_data.get('pnum', '')
        password = self.post_data.get('password', '')
        uid = self.post_data.get('uid', '')
        user_name = self.post_data.get('user_name', '')
        password = self.get_password(password)

        res = yield UserLib.get_user_by_pnum(pnum)
        if res:
            self.writeS({"data": "This pnum have been registered"})
            return
        user_info = yield UserLib.create_user(uid, pnum, user_name, password)
        if user_info:
            self.writeS({"data": user_info, "code": 0})
            return
        self.writeS({})
        return
