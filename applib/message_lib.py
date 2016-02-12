# -*- coding: UTF-8 -*-
import datetime, sys

from lib.sqlite_manager import sqlite_con
from tornado import gen
from lib.sqlite_manager import sqlite_con

class MessageLib(object):
    con = sqlite_con()

    @staticmethod
    @gen.coroutine
    def get_message_history(uid, last_msg_id):
        db_con = sqlite_con()
        where_str = ''
        if(int(last_msg_id) > 0):
            where_str = " AND id < '%s'" % (last_msg_id)
        sql = "SELECT id, `from_uid`, `to`, message_type, message_body, ctime, `from` FROM c_message WHERE `from_uid` = '%s' OR 'to' = '%s' OR message_type = 0 %s ORDER BY id LIMIT 20" % (uid, uid, where_str)
        db_con.Q(sql)
        res = db_con.fetch_all()
        user_message = []
        if res:
            for bean in res:
                user_message.append({'id': bean[0], 'from_uid': bean[1], 'to': bean[2], 'message_type': bean[3], 'message_body': bean[4], 'time': bean[5], 'from': bean[6]})
        raise gen.Return(user_message)

    @staticmethod
    @gen.coroutine
    def save_message(meesage_pkg):
        db_con = sqlite_con()
        now = datetime.datetime.now()
        sql = "INSERT INTO c_message (`from`, from_uid, `to`, message_type, message_body, ctime, status) VALUES (?, ?, ?, ?, ?, ?, 1)"
        db_con.Q(sql, (meesage_pkg['FROM'], meesage_pkg['FROM_UID'], meesage_pkg['TO'], meesage_pkg['MESSAGE_TYPE'], meesage_pkg['MESSAGE'], now))
