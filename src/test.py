# coding=utf-8
from backports import configparser
from dbPool import Mysql
class Test ():
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read("./db.cfg")
        self.mysql = Mysql(self.cfg.get('DB', 'HOST'), int(self.cfg.get('DB', 'PORT')), self.cfg.get('DB', 'NAME'), self.cfg.get('DB', 'PASSWORD'), 3, 5)

    def start(self):
        sql_insert = 'INSERT INTO show.test (name) VALUES (%s)'
        b = self.mysql.insertOne(sql_insert, '123455')
        self.mysql.end()

if __name__ == '__main__':
    Test = Test()
    Test.start()