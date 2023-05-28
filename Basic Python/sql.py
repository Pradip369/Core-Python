import psycopg2

conn = psycopg2.connect(host = 'localhost',user = "pradip",password = '3690',database = 'patrepedia')

cursor = conn.cursor()

# CRATE THE TABLE
# query = 'create table dummy (empno int unique,name char(20),surname char(250),salary float not null)'

# DETE THE TABLE
query = 'DROP TABLE dummy'

# INSERT THE DATA IN ROW
# for i in range(2,51):
#     query = f"insert into dummy (empno,name,surname,salary) values ({i},'pradip_{i}','kachhadiya_{i}',{20 + i})"

# RETRIVE THE DATA
# query = "select * from dummy"
# query = "select empno,name from dummy where empno in (2,3,5)"

# UPDATE THE DATA
# query = "update dummy set name = 'up_pradip' where empno=1"

# DELETE THE DATA
# query = "delete from dummy where empno=2"

cursor.execute(query)

# query_set = cursor.fetchall()
# query_set = cursor.fetchone()
# for i in query_set:
#     print(i)

cursor.close()
conn.commit()

conn.close()