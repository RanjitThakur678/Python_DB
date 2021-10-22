import psycopg2
#
def create_table():
    conn = psycopg2.connect("dbname='student'user='postgres' password='Rony1995$' host ='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS shop(Item TEXT,Quantity INTEGER,Price REAL)')
    conn.commit()
    conn.close()

create_table()



def insert_value(item,quantity,price):
    conn = psycopg2.connect("dbname='student'user='postgres'password='Rony1995$' host ='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT into shop VALUES('%s','%s','%s')" %(item,quantity,price))
    conn.commit()
    conn.close()

insert_value('Apple-laptop',12000,15)


def view_db():
    conn = psycopg2.connect("dbname='student'user='postgres'password='Rony1995$' host ='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM shop")
    views = cur.fetchall()
    conn.commit()
    conn.close()
    return views

print(view_db())



## For My sql data the below code works

# import mysql.connector
# word = input("Enter a word in English and press Enter: ")
# con = mysql.connector.connect(
#     user="ardit700_student",
#     password = "ardit700_student",
#     host="108.167.140.122",
#     database = "ardit700_pm1database"
# )
# cursor = con.cursor()
# query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
# results = cursor.fetchall()
# if results:
#     for result in results:
#         print(result[1])
# else:
#     print("We couldn't find any results about that.")
