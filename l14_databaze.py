# from sklearn.datasets import load_linnerud
# data=load_linnerud()
# print(data.data[0])
# https://pypi.python.org/pypi/cx_Oracle
# conda install oracle-instantclient # http://www.oracle.com/technetwork/topics/winsoft-085727.html
from sqlalchemy import create_engine
engine = create_engine(
    "oracle+cx_oracle://SYSTEM:12345@(DESCRIPTION = "
    "(LOAD_BALANCE=on) (FAILOVER=ON) (ADDRESS = "
    "(PROTOCOL = TCP)(HOST = 10.20.20.230)(PORT = 1521)) "
    "(CONNECT_DATA = (SERVER = DEDICATED) "
    "(SERVICE_NAME = XE)))")
conn = engine.connect()

from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
metadata = MetaData()
users = Table('Karpov', metadata,
    Column('id', Integer, primary_key=True),
    Column('Name', String(50)),
    Column('Birth', String(50)),
    Column('City', String(50)),
    Column('Position', String(50)))
#metadata.create_all(engine)

ins = users.insert().values(id=3, Name='Ivanov',
                            Birth='22.03.1980', City='Moscow')
ins.compile().params
result = conn.execute(ins)
# print(result)
from sqlalchemy.sql import select
s = select([users])
result = conn.execute(s)
for row in result:
    print(row)

###############Настоящий SQL
# query1="create table Staff (id NUMBER(6), name VARCHAR2(15) not NULL)"
# from sqlalchemy.orm import sessionmaker
# Internal = sessionmaker(bind=engine)
# internal = Internal()
# result = internal.execute(query1)
# Удаление таблицы
# result = internal.execute("drop table Staff")
# internal.commit()
# internal.close()
# print(result)