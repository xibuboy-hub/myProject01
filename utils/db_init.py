# -*- coding: utf-8 -*-
"""
**************************************
*  @Author  ：   Joy_Lo
*  @Time    ：   2025/1/25 下午 01:11
*  @Project :   demo01
*  @FileName:   db_init.py
**************************************
程式用途:link db
"""

import sqlite3
import pymysql
import pyodbc


class Mysql:
    def __init__(self, host: str, database: str):
        self.conn = pymysql.connect(host=host, user='root', password='root123',
                                    port=3306, autocommit=True, database=database, charset='utf8mb4')

    def query_sql(self, sql: str, params=None) -> list:
        if params is None:
            params = []
        # cursor = self.conn.cursor()
        # userTable_sql = """CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(20),password varchar(20))"""
        # blogTable_sql = """CREATE TABLE IF NOT EXISTS blog (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(20),content varchar(128))"""
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
            result = cursor.fetchall()
        ret = [dict(zip([column[0] for column in cursor.description], row)) for row in result]
        return ret

    def execute_sql(self, sql: str, params=None) -> None:
        if params is None:
            params = []
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
        self.conn.commit()


# Sqlite类用于操作Sqlite数据库
class Sqlite:

    def __init__(self, sq_db: str):
        self.conn = sqlite3.connect(sq_db)

    def query_sql(self, sql: str, params=None) -> list:
        if params is None:
            params = []
        # userTable_sql = """CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(20),password varchar(20))"""
        # blogTable_sql = """CREATE TABLE IF NOT EXISTS blog (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(20),content varchar(128))"""
        with self.conn.cursor() as cursor:
            result = cursor.execute(sql, params).fetchall()
        return result

    def execute_sql(self, sql: str, params=None) -> None:
        if params is None:
            params = []
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
            self.conn.commit()


# Access类用于操作Access数据库
class Access:
    def __init__(self):
        self.conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                        r'DBQ=D:/pythonProject/flask_01/data/data.mdb;'
        self.conn = pyodbc.connect(self.conn_str)

    def query_sql(self, sql: str, params=None) -> list:
        if params is None:
            params = []
        # 创建两张表
        # userTable_sql = """CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(20),password varchar(20))"""
        # blogTable_sql = """CREATE TABLE IF NOT EXISTS blog (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(20),content varchar(128))"""
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
            result = cursor.fetchall()
        return result

    def execute_sql(self, sql: str, params=None) -> None:
        if params is None:
            params = []
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
            self.conn.commit()


if __name__ == '__main__':
    db = "../data/data_new.db"
    table = 'lx_subtnb_mi_20251014'
    conn = sqlite3.connect(db)
    cursor = conn.cursor()  # 查
    data1 = [dict(zip([column[0] for column in cursor.description], row)) for row in
             cursor.execute(rf'select  * from {table}').fetchall()]
    print(data1)
