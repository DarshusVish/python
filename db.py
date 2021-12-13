import psycopg2

conn = None
cur = None
try:
    conn = psycopg2.connect(
        host = 'localhost',
        dbname = 'DB1',
        user = 'postgres',
        password = 'system',
        port = 5432
    )

    cur = conn.cursor()

    cur.execute('Drop Table if exists employee')

    create_script = ''' Create Table if not exists employee(
                        id  int primary key,
                        name  varchar(40) Not Null,
                        salary int,
                        dept_id varchar(30)
                        )'''

    cur.execute(create_script)

    insert_script='Insert into employee(id,name,salary,dept_id) values(%s, %s, %s, %s)'
    insert_values = [(1,'Vishal','1430000','D314'),(2,'Vish','100','D314'),
                     (3,'Vishal','1000000','D4'),(4,'Vi','2000000','D3')]
    for record in insert_values:
        cur.execute(insert_script,record)

    conn.commit()
except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
    if cur is not None:
        cur.close()