import psycopg2

connection = psycopg2.connect(dbname="postgres", user="postgres",
                              password="mithukundu60@", host="localhost", port="5432")
print("connection established")

# Creating cursor
cursor = connection.cursor()
# Serial is used for generating sequence automatically
cursor.execute(
    '''INSERT INTO student(NAME,ADDRESS,AGE) VALUES('santosh','garwa',23);''')
print("Data inserted")
# Commiting the changes
connection.commit()
connection.close
