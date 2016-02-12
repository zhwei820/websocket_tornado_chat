# -*- coding: UTF-8 -*-
import datetime, sys
if __name__ == '__main__':
    sys.path.append("../")

from tornado import gen
from lib.sqlite_manager import sqlite_con

class UserLib(object):

    @staticmethod
    @gen.coroutine
    def get_user_by_uid(uid):
        db_con = sqlite_con()
        sql = "SELECT uid, pnum, user_name, password, status, ctime FROM c_user WHERE uid = '%s';" % (uid)
        db_con.Q(sql)
        bean = db_con.fetch_one()
        user_info = {}
        if bean:
            user_info = {'uid': bean[0], 'pnum': bean[1], 'user_name': bean[2], 'password': bean[3], 'status': bean[4], 'ctime': bean[5]}
        raise gen.Return(user_info)

    @staticmethod
    @gen.coroutine
    def get_user_by_pnum(pnum):
        db_con = sqlite_con()
        sql = "SELECT uid, pnum, user_name, password, status, ctime FROM c_user WHERE pnum = '%s';" % (pnum)
        db_con.Q(sql)
        bean = db_con.fetch_one()
        user_info = {}
        if bean:
            user_info = {'uid': bean[0], 'pnum': bean[1], 'user_name': bean[2], 'password': bean[3], 'status': bean[4], 'ctime': bean[5]}
        raise gen.Return(user_info)

    @staticmethod
    @gen.coroutine
    def check_user(uid, password):
        user_info = yield UserLib.get_user_by_uid(uid)
        if user_info and user_info.get('password', 0) == password:
            raise gen.Return(True)
        raise gen.Return(False)

    @staticmethod
    @gen.coroutine
    def create_user(uid, pnum, user_name, password):
        db_con = sqlite_con()
        now = datetime.datetime.now()
        sql = "INSERT INTO c_user (uid, pnum, user_name, password, status, ctime, utime) VALUES ('%s', '%s', '%s', '%s', '1', '%s', '%s')" % (uid, pnum, user_name, password, now, now)
        db_con.Q(sql)
        user_info = {'uid': uid, 'pnum': pnum, 'user_name': user_name, 'password': password, 'status': 1, 'ctime': now}
        raise gen.Return(user_info)
