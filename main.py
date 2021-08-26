###################### Import Statements ######################
import tkinter as tk
from tkinter import ttk
import sqlite3
import database as database

######################### TKinter Code ########################
class AddressBook(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("John's Phone Address Book")
    self.resizable(True,True)
    self.columnconfigure(0,weight=1)
    self.rowconfigure(0,weight=1)

    # Implement TK Styling Theme
    style = ttk.Style(self)
    style.theme_use('alt')

    # Create SQLite3 Database & Contacts SQLite3 Table
    database.create_table()

    # Create Container Frame
    container = ttk.Frame(self)
    container.grid()

    # Create Frames Dictionary for Switching Views
    self.frames = dict()

    # Create Entry Frame
    entry_frame = Entry(container,self,lambda:self.show_frame(Records))
    entry_frame.grid(row=0,column=0,sticky='NSWE')

    # Create Records Frame
    record_frame = Records(container,self,lambda:self.show_frame(Entry))
    record_frame.grid(row=0,column=0,sticky='NSWE')

    self.frames[Entry] = entry_frame
    self.frames[Records] = record_frame

    self.show_frame(Entry)

  def show_frame(self,container):
    frame = self.frames[container]
    frame.tkraise()

# Entry Frame Class
class Entry(ttk.Frame):
  # Class Constructor Method
  def __init__(self,parent,controller,show_record):
    super().__init__(parent)
    self.name = tk.StringVar()
    self.phone_number = tk.StringVar()
    self.relationship = tk.StringVar()

    # Label Widgets
    name_label = ttk.Label(self,text='Name: ')
    phone_label = ttk.Label(self,text='Phone: ')
    relationship_label = ttk.Label(self,text='Relationship: ')

    name_label.grid(row=0,column=0,sticky='W')
    phone_label.grid(row=1,column=0,sticky='W')
    relationship_label.grid(row=2,column=0,sticky='W')

    # Entry Widgets
    self.name_entry = ttk.Entry(self,textvariable=self.name)
    self.phone_number_entry = ttk.Entry(self,textvariable=self.phone_number)
    self.relationship_entry = ttk.Entry(self,textvariable=self.relationship)

    self.name_entry.grid(row=0,column=1,sticky='W')
    self.phone_number_entry.grid(row=1,column=1,sticky='W')
    self.relationship_entry.grid(row=2,column=1,sticky='W')

    # Button Widgets
    clear_button = ttk.Button(self,text='Clear',command=self.clear_entry_fields,cursor='hand2')
    add_button = ttk.Button(self,text='Add',command=self.add_database_entry,cursor='hand2')
    show_records_button = ttk.Button(self,text='Show Records',command=show_record,cursor='hand2')

    clear_button.grid(row=3,column=0,columnspan=1,sticky='EW')
    add_button.grid(row=3,column=1,columnspan=1,sticky='EW')
    show_records_button.grid(row=4,column=0,columnspan=2,sticky='EW')

  # Clear Entry Fields
  def clear_entry_fields(self):
    self.name_entry.delete(0,'end')
    self.phone_number_entry.delete(0,'end')
    self.relationship_entry.delete(0,'end')

  def add_database_entry(self):
    print(self.name.get(),self.phone_number.get(),self.relationship.get())
    database.add_entry(self.name.get(),self.phone_number.get(),self.relationship.get())
    self.clear_entry_fields()
    self.display_records()

  def display_records(self):
    records = database.retrieve_contacts()
    for row in records:
      print(f"{row['name']}, {row['phone_number']}, {row['relationship']}")

# Records Frame Class
class Records(ttk.Frame):
  # Class Constructor Method
  def __init__(self,parent,controller,show_entry):
    super().__init__(parent)

    # TTK Treeview Widget
    tree = ttk.Treeview(self)

    # Define Columns
    # Creates Phantom Column
    tree['columns'] = ('Name','Phone Number','Relationship')

    # Format Columns
    tree.column('#0',width=0,minwidth=0)
    tree.column('Name',anchor='w',width=120)
    tree.column('Phone Number',anchor='center',width=120)
    tree.column('Relationship',anchor='w',width=120)

    # Create Headings
    tree.heading('#0',text='',anchor='w')
    tree.heading('Name',text='Name',anchor='w')
    tree.heading('Phone Number',text='Phone Number',anchor='center')
    tree.heading('Relationship',text='Relationship',anchor='center')

    # Retrieve Phone Records
    records = database.retrieve_contacts()

    # Populate Records in Treeview Widget
    x = 0
    for row in records:
      tree.insert(parent='',index='end',iid=x,text='',values=(row['name'],row['phone_number'],row['relationship']))
      x += 1
    tree.grid()

    # Button Widgets
    change_entry = ttk.Button(self,text='Change to Entry',command=show_entry,cursor='hand2')
    change_entry.grid()

############################# Python Code #######################

phonebook = AddressBook()
phonebook.mainloop()