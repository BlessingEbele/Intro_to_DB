#pip.py
import mysql.connector
mydb = mysql.connetor.connet(
    host = "localhost",
    user = "newuser",
    password = "newuserpassword"
)

mycursor = mydb.cursor()


mycursor.execute("CREATE DATABASE library")
mycursor.execute("USE library")
mycursor.execute("""
    CREATE TABLE books
                 id INT AUTO_INCREMENT PRIMARY KEY
                 title VARCHAR(200)
                 author VARCHAR(100)
                 );
""")
result = mycursor.fetchall()
for row in result:
    print(row)