import logging
import os
import pyodbc
import pandas as pd
import sqlite3


def log_demo():
    log_directory = 'log'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file_path = os.path.join(log_directory, 'app.log')
    logging.basicConfig(
        filename=log_file_path,
        level=logging.DEBUG,
        format='%(asctime)s-%(levelname)s-%(message)s'
    )

    logging.debug('this is a debug message')
    logging.info('this is a info message')
    logging.warning('this is a warning message')
    logging.error('this is a error message')
    logging.critical('this is a critical message')


class CreateAccess:
    conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
               r'DBQ=D:/E/joy/資料庫.accdb;'

    def query_sql(self, sql: str, params=None) -> list:
        if params is None:
            params = []
        conn = pyodbc.connect(
            self.conn_str)
        cursor = conn.cursor()
        # 创建两张表
        # userTable_sql = """CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(20),password varchar(20))"""
        # blogTable_sql = """CREATE TABLE IF NOT EXISTS blog (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(20),content varchar(128))"""
        cursor.execute(sql, params)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def execute_sql(self, sql: str, parames=None) -> None:
        if parames is None:
            parames = []
        conn = pyodbc.connect(
            self.conn_str)
        cursor = conn.cursor()
        cursor.execute(sql, parames)
        conn.commit()
        cursor.close()
        conn.close()


def excel2sqlite3():
    # 读取Excel文件
    excel_file = 'c:/users/joy_lo/documents/lx_subtnb_mi_20251014.xlsx'
    df = pd.read_excel(excel_file)

    # 连接到SQLite数据库
    sqlite_db = '../data/data_new.db'
    conn = sqlite3.connect(sqlite_db)

    # 将DataFrame写入SQLite数据库的表中
    table_name = 'lx_subtnb_mi_20251014'
    df.to_sql(table_name, conn, if_exists='append', index=False)  # 使用'replace'来替换现有表或'append'来追加数据

    # 关闭数据库连接
    conn.close()


def excel2mysql(path: str, table: str) -> None:
    import pandas as pd
    from sqlalchemy import create_engine
    # 读取Excel文件
    excel_file = path
    df = pd.read_excel(excel_file)
    # 创建数据库连接字符串
    database_connection = 'mysql+mysqlconnector://root:root123@10.129.116.144:3306/l3_fixture_management'
    engine = create_engine(database_connection)
    df.to_sql(table, con=engine, if_exists='append', index=False)
    print('over')

def mysql2excel():
    import pandas as pd
    from sqlalchemy import create_engine

    # 创建数据库连接引擎
    engine = create_engine('mysql+pymysql://root:root123@localhost/test')

    # 读取数据
    query = "SELECT * FROM power_list"
    df = pd.read_sql(query, engine)

    # 导出到Excel文件
    df.to_excel('c:/users/joy_lo/desktop/lx_power_list.xlsx', index=False)


if __name__ == '__main__':
    # ac = CreateAccess()
    # userTable_sql = """CREATE TABLE user(id INTEGER NOT NULL PRIMARY KEY,username TEXT,password TEXT)"""
    # ac.execute_sql(userTable_sql)
    # insert = "insert into user(id,username,password) values (1,'admin','admin')"
    # ac.execute_sql(insert)
    # a, b, c = ac.query_sql('select * from user where id=?;', 1)[0]
    # print(a, b, c)
    # ac.execute_sql('drop table user')
    # excel2sqlite3()
    table = 'lx_test_fixture'
    excel2mysql(f'c:/users/joy_lo/desktop/{table}.xlsx', table)
    # mysql2excel()
