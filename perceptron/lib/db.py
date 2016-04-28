import sqlite3 as sqlite

class Database():
    def __init__(self,mode='',dbname='nn.db'):
        self.con=sqlite.connect(dbname)
        if mode != 'persistent': self.droptables()
        self.maketables()

    def __del__(self):
        self.con.close()

    def droptables(self):
        self.con.execute('drop table if exists hiddens')
        self.con.execute('drop table if exists inputs')
        self.con.execute('drop table if exists outputs')
        self.con.commit()

    def maketables(self):
        self.con.execute('create table if not exists hiddens(key)')
        self.con.execute('create table if not exists inputs(fromid,toid,strength)')
        self.con.execute('create table if not exists outputs(fromid,toid,strength)')
        self.con.commit()
