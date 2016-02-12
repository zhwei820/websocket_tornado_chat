# -*- coding: UTF-8 -*-
import sqlite3, logging, sys

if __name__ == '__main__':
    sys.path.append("../")

class sqlite_con:
    con = None
    cur = None

    def __init__(self):
        if self.con is None:
            self.con = sqlite3.connect("data.db")
            self.con.isolation_level = None
            self.cur = self.con.cursor()

    def Q(self, sql, par = ()):
        return self.query(sql, par)

    # 事物需要TQ支持 而不是Q
    # def TQ(self, sql):
    #     rs = self.cur.execute(sql)
    #     return rs

    def query(self, sql, par):
        try:
            rs = self.cur.execute(sql, par)
            return rs
        except Exception, e:
            logging.error('sql execute error: %s', sql, exc_info=True)

    def fetch_one(self):
        return self.cur.fetchone()

    def fetch_all(self):
        return self.cur.fetchall()

    def close(self):
        try:
            self.cur.close()
            self.con.close()
        except:
            pass
        self.con = None

    def __del__(self):
        try:
            if self.con is not None:
                self.close()
        except:
            pass

    def __exit__(self):
        # 添加对with语句的支持
        try:
            if self.con is not None:
                self.close()
        except:
            pass


if __name__ == '__main__':
    db_con = sqlite_con()
    db_con.Q("""
        CREATE TABLE IF NOT EXISTS `c_user` (
          `uid` int(11)  NOT NULL ,
          `pnum` int(11)  NOT NULL ,
          `user_name` varchar(50) NOT NULL ,
          `password` varchar(64) NOT NULL ,
          `status` tinyint(1)  NOT NULL ,
          `ctime` datetime,
          utime datetime
        ) ;""")

    db_con.Q("""
        CREATE TABLE IF NOT EXISTS `c_message` (
           ID INTEGER PRIMARY KEY   AUTOINCREMENT,
          `from_uid` varchar(50) NOT NULL ,
          `from` int(11)  NOT NULL ,
          `to` varchar(50) NOT NULL ,
          `message_type` tinyint(1) NOT NULL ,
          `message_body` varchar(500) NOT NULL ,
          `status` tinyint(1)  NOT NULL ,
          `ctime` datetime
        ) ;""")
    db_con.Q("INSERT INTO c_user (uid, pnum, user_name, password, status, ctime, utime) VALUES ('11049604', '45435435', '345435', 'c08bf614c5265f7a1b42ab90ae3359e7', '1', '2016-02-06 16:41:22.815160', '2016-02-06 16:41:22.815160')")
