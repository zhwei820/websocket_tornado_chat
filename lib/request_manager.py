# -*- coding: UTF-8 -*-
import json, hashlib

from tornado.web import RequestHandler

from lib.json_manager import CJsonEncoder

class ToolsMixin(object):
    def __init__(self):
        self._mysql_conn_arr = {}

    def get_redis(self, host_name=''):
        return m_redis.get_instance(host_name)

    def cleaning(self):
        while 1:
            try:
                _, _conn = self._mysql_conn_arr.popitem()
            except KeyError:
                break
            else:
                _conn.close()

    def mysql_conn(self, db_name=""):
        _conn = self._mysql_conn_arr.get(db_name)
        if not _conn:
            _conn = mmysql_rw(db_name)
            self._mysql_conn_arr[db_name] = _conn
        return _conn

    def get_password(self, password):
        return hashlib.md5(password + 'aa123bb').hexdigest()


class SuperRequestHandler(RequestHandler, ToolsMixin):
    def prepare(self):
        self.exc_data = None
        self.post_data = None
        try:
            self.post_data = dict((_k, _v[0] if _v else '') for _k, _v in self.request.arguments.iteritems())

            if 'os_version' in self.post_data:
                self.post_data['os_version'] = self.post_data['os_version'][:20]
            if 'device_name' in self.post_data:
                self.post_data['device_name'] = self.post_data['device_name'][:50]
        except:
            self.on_formwork_error("request error")

    def writeS(self, obj, errcode=0, error="", call_back=None):
        u'''
        有call_back时返回 jsonp
        '''
        super(SuperRequestHandler, self).cleaning()
        self.cleaning()

        if not obj:
            j_data = {'err_code': errcode, 'err_msg': error}
            obj = json.dumps(j_data, cls=CJsonEncoder)
        elif not isinstance(obj, (str, unicode)):  # object
            j_data = {'err_code': errcode, 'err_msg': error}
            if isinstance(obj, dict):
                j_data.update(obj)
            else:
                j_data['data'] = obj
            obj = json.dumps(j_data, cls=CJsonEncoder)

        if call_back:
            self.write('%s(%s)' % (call_back, obj))
        else:
            self.write(obj)
        self.finish()
        return


    def on_formwork_error(self, error_from, exc=None):
        self.set_status(500)
        self.writeS({}, 10000, u"网络错误。")
