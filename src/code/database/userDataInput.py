import psycopg2

connection = psycopg2.connect(dbname="postgres", user="postgres",
                              password="mithukundu60@", host="localhost", port="5432")
print("connection established")

# Creating cursor
cursor = connection.cursor()
# Serial is used for generating sequence automatically

# Input data from user
name = input('enter name')
address = input('enter address')
age = input('enter age')

# Method to enter data from user into query
query = '''INSERT INTO student(NAME,ADDRESS,AGE) VALUES(%s,%s,%s);'''
cursor.execute(query, (name, address, age))


print("Data inserted")
# Commiting the changes
connection.commit()
connection.close
