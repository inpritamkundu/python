import psycopg2

connection = psycopg2.connect(dbname="postgres", user="postgres",
                              password="mithukundu60@", host="localhost", port="5432")
print("connection established")

# Creating cursor
cursor = connection.cursor()
# Serial is used for generating sequence automatically
cursor.execute(
    '''CREATE TABLE student(ID serial,NAME text,ADDRESS text, AGE text);''')
print("Table created")
# Commiting the changes
connection.commit()
connection.close
