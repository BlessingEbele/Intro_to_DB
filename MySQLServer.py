# author: Anochili Blessing Ebele
# purpose: Write a simple python script that creates the database alx_book_store in your MySQL server.
# date: 14/10/2024

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',   # Replace with your MySQL username
            password='$qlP@55w0rd!2o24#Db' # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: '{e}' occurred while connecting to the MySQL server.")

    finally:
        # Close the connection and cursor to avoid memory leaks
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()

