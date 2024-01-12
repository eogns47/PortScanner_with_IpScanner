#---------------------------POSTGRESQL VERSION---------------------------
import psycopg2
import logging
import binascii
def getConnection():
    with open('./../database-info/sql-password', 'r', encoding='utf-8') as f:
        password = f.readline().strip()
    with open('../database-info/sql-id', 'r', encoding='utf-8') as f:
        id = f.readline().strip()

    return psycopg2.connect(
        host='localhost', user=id, password=password, database='potato'
    )

def insertCrawlingData(allKoreaIP):
    with getConnection() as connection:
        with connection.cursor() as cursor:
            createAndUseDatabase(cursor)
            createIpTableIfNotExist(cursor)

            insertSql = 'INSERT INTO IP (ip,ip_crc) VALUES (%s, %s) ON CONFLICT (ip) DO NOTHING'
            insertedNum = 0
            for ip_list in allKoreaIP:
                for ip in ip_list:
                    ip_crc= binascii.crc32(ip.encode())
                    cursor.execute(insertSql, (ip,ip_crc))
                    insertedNum += 1
            connection.commit()

    logging.info(f'Inserted {insertedNum} IPs to database')

def createAndUseDatabase(cursor):
    
    cursor.execute("""
        DO $$ 
        BEGIN 
            IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'potato') THEN
                CREATE DATABASE potato;
            END IF;
        END $$;
    """)

def createIpTableIfNotExist(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS IP (
            ip_id SERIAL PRIMARY KEY,
            ip VARCHAR(15) NOT NULL UNIQUE,
            ip_crc BIGINT NOT NULL,
            create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE INDEX IF NOT EXISTS ip_crc_idx ON IP(ip_crc);
    ''')




#---------------------------MYSQL VERSION---------------------------
# import pymysql
# import logger
# from sqlite3 import Cursor
# import logging


# def getConnection():
#     with open('sql-password', 'r', encoding='utf-8') as f:
#         password = f.readline().strip()
#     return pymysql.connect(
#         host='localhost', user='root', password=password, charset='utf8mb4')


# def insertCrawlingData(AllkoreaIP:list): 
#     with getConnection() as connection:
#         with connection.cursor() as cursor:
#             create_and_use_database(cursor)
#             createIpTableIfNotExist(cursor)

#             insert_sql = 'REPLACE INTO IP (ip) VALUES (%s)'
#             inserted_num=0;
#             for ip in AllkoreaIP:
#                 cursor.execute(insert_sql, (ip))
#                 inserted_num+=1
#         connection.commit()

#     logging.info(f'Inserted {inserted_num} IPs to database')


# def create_and_use_database(cursor: Cursor):
#     cursor.execute('CREATE DATABASE IF NOT EXISTS potato')
#     cursor.execute('USE potato')


# def createIpTableIfNotExist(cursor):
#     cursor.execute('''
#             CREATE TABLE IF NOT EXISTS IP (
#                 ip VARCHAR(15) NOT NULL,
#                 port INT,
#                 weak VARCHAR(1024),
#                 PRIMARY KEY (ip)
#             );
#     ''')
            
#     cursor.execute('''
#         alter table IP convert to charset utf8;
#     ''')

