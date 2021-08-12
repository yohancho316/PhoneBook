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
    self.geometry('400x400')
    self.columnconfigure(0,weight=1)
    self.rowconfigure(0,weight=1)

    # Create SQLite3 Database & Contacts SQLite3 Table
    database.create_table()

    # Create Container Frame
    container = ttk.Frame(self)
    container.grid()

    # Create Entry Frame
    entry_frame = Entry(container)
    entry_frame.grid(row=0,column=0,sticky='W')

# Entry Frame Class
class Entry(ttk.Frame):
  def __init__(self,parent):
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
    clear_button = ttk.Button(self,text='Clear',command=self.clear_entry_fields)
    add_button = ttk.Button(self,text='Add',command=self.add_database_entry)

    clear_button.grid(row=3,column=0,columnspan=1,sticky='EW')
    add_button.grid(row=3,column=1,columnspan=1,sticky='EW')

  # Clear Entry Fields
  def clear_entry_fields(self):
    self.name_entry.delete(0,'end')
    self.phone_number_entry.delete(0,'end')
    self.relationship_entry.delete(0,'end')

  def add_database_entry(self):
    print(self.name.get(),self.phone_number.get(),self.relationship.get())
    database.add_entry(self.name.get(),self.phone_number.get(),self.relationship.get())
    self.clear_entry_fields()

############################# Python Code #######################

phonebook = AddressBook()
phonebook.mainloop()