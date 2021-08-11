###################### Import Statements ######################
import sqlite3

###################### Stored SQL Queries ######################
CREATE_TABLE_QUERY = 'CREATE TABLE IF NOT EXISTS contacts(name TEXT,phone_number TEXT, relationship TEXT);'

####################### Python Code ########################

# Create the Database & SQLite3 Database File
connection = sqlite3.connect('address_book.db')
# by default the connection grabs columns and stores them in a tuple which can be stored in the cursor
# you can change connection to grab columns and store them as a dictionary in the cursor.
connection.row_factory = sqlite3.Row

def create_table():
  connection.execute(CREATE_TABLE_QUERY)

def add_entry(name,phone_number,age):
  with connection:
    connection.execute('INSERT INTO users VALUES(?,?,?);',(name,phone_number,age))

def get_entries():
  # Method 1
  # cursor = connection.cursor()
  # cursor.execute('SELECT * FROM entries;')
  cursor = connection.execute('SELECT * FROM users;')
  # cursor.fetchone() # Fetch the first row and move the cursor to the next row
  return cursor.fetchall() # Fetches all of the results from the cursor and puts them in a list.


def close_connection():
  connection.close()





