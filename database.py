import sqlite3

connection = sqlite3.connect('john_phone_book.db')
# by default the connection grabs columns and stores them in a tuple which can be stored in the cursor
# you can change connection to grab columns and store them as a dictionary in the cursor.
connection.row_factory = sqlite3.Row


welcome = "Welcome to John's Phone Book"

menu = """
Please choose a selection.

1. Add new entry.
2. View all entries.
3. Quit.

Enter your selection:
"""

def create_table():
  with connection:
    connection.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, phone_number TEXT, age INTEGER);')

def add_entry(name,phone_number,age):
  with connection:
    connection.execute('INSERT INTO users VALUES(?,?,?);',(name,phone_number,age))

def prompt_entry():
  name = input("Enter Name to Record: ")
  phone_number = input("Enter Phone Number: ")
  age = input("Enter age: ")
  add_entry(name,phone_number,age)

def get_entries():
  # Method 1
  # cursor = connection.cursor()
  # cursor.execute('SELECT * FROM entries;')
  cursor = connection.execute('SELECT * FROM users;')
  # cursor.fetchone() # Fetch the first row and move the cursor to the next row
  return cursor.fetchall() # Fetches all of the results from the cursor and puts them in a list.

def view_entries(entries):
  # Prints row by row
  for entry in entries:
    print(f"{entry['name']}\n{entry['phone_number']}\n{entry['age']}\n\n")

def close_connection():
  connection.close()

print(welcome)
create_table()

while(user_input := input(menu)) != "3":
  if user_input == "1":
    prompt_entry()
  elif user_input == "2":
    view_entries(get_entries())
  else:
    print("Invalid option, please try again!")

close_connection()

