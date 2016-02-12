# -*- coding: UTF-8 -*-
import json, datetime
import tornado.websocket

from applib.user_lib import UserLib
from applib.message_lib import MessageLib

from tornado import gen

# Different message types
MESSAGE     = 0  # public message
PRIVATE_MESSAGE     = 1
NAMECHANGE  = 11
JOIN        = 12
LEAVE       = 13
USERLIST    = 14
ERROR       = 15

# The list of currently connected clients
CONNECTED_CLIENTS = set()
NAMED_CONNECTED_CLIENTS = {}


class ChatWebSocket(tornado.websocket.WebSocketHandler):
    """ The chat implemententation, all data send to server is json, all responses are json """
    def check_origin(self, origin):
        return True

    def open(self):
        CONNECTED_CLIENTS.add(self)
        self.client_name = ''
        self.uid = ''
        self.join_completed = False # Not completed until a name has been selected

    @gen.coroutine
    def on_message(self, message):
        try:
            pkg = json.loads(message)
        except:
            self.write_message(self.create_error_pkg(u'Format error'))
            return

        if pkg['TYPE'] == JOIN:
            self.client_name = pkg['USER_NAME']
            self.uid = pkg['UID']
            self.join_completed = True
            NAMED_CONNECTED_CLIENTS[pkg['UID']] = self
            CONNECTED_CLIENTS.remove(self)
            self.broadcast(self.create_join_pkg())
            message_pkg = yield self.create_userlist_pkg()
            self.broadcast(message_pkg)
            # self.write_message(self.create_userlist_pkg())
        elif pkg['TYPE'] == PRIVATE_MESSAGE:
            self.send_private_message(pkg['TO'], self.create_private_message_pkg(pkg['MESSAGE']))
            pkg['FROM_UID'] = self.uid
            pkg['FROM'] = self.client_name
            pkg['MESSAGE_TYPE'] = PRIVATE_MESSAGE
            yield MessageLib.save_message(pkg)
        elif pkg['TYPE'] == MESSAGE:
            self.broadcast(self.create_message_pkg(pkg['MESSAGE']))
            pkg['FROM_UID'] = self.uid
            pkg['FROM'] = self.client_name
            pkg['TO'] = ''
            pkg['MESSAGE_TYPE'] = MESSAGE
            yield MessageLib.save_message(pkg)
        elif pkg['TYPE'] == USERLIST:
            message_pkg = yield self.create_userlist_pkg()
            self.write_message(message_pkg)
        elif pkg['TYPE'] == NAMECHANGE:
            old_name = self.client_name
            self.client_name = pkg['NEWNAME']
            self.broadcast(self.create_name_change_pkg(old_name))
        else:
            self.write_message(self.create_error_pkg('unknown message type'))

    def send_private_message(self, uid, message_pkg):
        self.write_message(message_pkg)
        NAMED_CONNECTED_CLIENTS[uid].write_message(message_pkg)

    def broadcast(self, message_pkg, all_but=None):
        for c in NAMED_CONNECTED_CLIENTS.values():
            if c.join_completed and c != all_but:
                c.write_message(message_pkg)

    def create_join_pkg(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pkgdata = {'TYPE': JOIN, 'USER_NAME': self.client_name, "UID": self.uid, 'TIME': now}
        return json.dumps(pkgdata)

    def create_name_change_pkg(self, old_name):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pkgdata = {'TYPE': NAMECHANGE, 'OLDNAME': old_name, 'NEWNAME': self.client_name, 'TIME': now}
        return json.dumps(pkgdata)

    def create_private_message_pkg(self, msg):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pkgdata = {'TYPE': PRIVATE_MESSAGE, 'SENDER': {"uid": self.uid, "user_name": self.client_name}, 'MESSAGE': msg, 'TIME': now}
        return json.dumps(pkgdata)

    def create_message_pkg(self, msg):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pkgdata = {'TYPE': MESSAGE, 'SENDER': {"uid": self.uid, "user_name": self.client_name}, 'MESSAGE': msg, 'TIME': now}
        return json.dumps(pkgdata)

    def create_leave_pkg(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pkgdata = {'TYPE': LEAVE, 'USER': self.client_name, 'TIME': now}
        return json.dumps(pkgdata)

    @gen.coroutine
    def create_userlist_pkg(self):
        users = []
        for c in NAMED_CONNECTED_CLIENTS.values():
            user_info = yield UserLib.get_user_by_uid(c.uid)
            pnum = user_info.get("pnum", '')
            users.append({'name': c.client_name, 'uid': c.uid, 'pnum': pnum});
        pkgdata = {'TYPE': USERLIST, 'USERS': users}
        raise gen.Return(json.dumps(pkgdata))

    def create_error_pkg(self, detail):
        pkgdata = {'TYPE': ERROR, 'DETAIL': detail}
        return json.dumps(pkgdata)

    def on_close(self):
        print self.client_name , 'leave'
        self.broadcast(self.create_leave_pkg(), all_but=self)
        del NAMED_CONNECTED_CLIENTS[self.uid]
        self.broadcast(self.create_userlist_pkg())
