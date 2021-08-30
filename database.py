###################### Import Statements ######################
import sqlite3

###################### Stored SQL Queries ######################
CREATE_TABLE_QUERY = 'CREATE TABLE IF NOT EXISTS contacts(name TEXT,phone_number TEXT, relationship TEXT);'

INSERT_ENTRY_QUERY = "INSERT INTO contacts(name,phone_number,relationship) VALUES(?,?,?);"

SELECT_ALL_ROWS_QUERY = 'SELECT DISTINCT * FROM contacts;'
# 'SELECT DISTINCT * FROM contacts ORDER BY name;'

####################### Python Code ########################

# Create the Database & SQLite3 Database File
connection = sqlite3.connect('address_book.db')
# by default the connection grabs columns and stores them in a tuple which can be stored in the cursor
# you can change connection to grab columns and store them as a dictionary in the cursor.
connection.row_factory = sqlite3.Row

def create_table():
  with connection:
    connection.execute(CREATE_TABLE_QUERY)
    connection.commit()

def add_entry(name,phone_number,relationship):
  with connection:
    connection.execute(INSERT_ENTRY_QUERY,(name,phone_number,relationship))
    connection.commit()

def retrieve_contacts():
  with connection:
    cursor = connection.cursor()
    cursor.execute(SELECT_ALL_ROWS_QUERY)
    return cursor.fetchall()

def close_connection():
  with connection:
    connection.close





