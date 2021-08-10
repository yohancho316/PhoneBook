import tkinter as tk
from tkinter import ttk
import sqlite3

class AddressBook(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("John's Phone Address Book")
    self.resizable(True,True)
    self.geometry('400x400')
    self.columnconfigure(0,weight=1)
    self.rowconfigure(0,weight=1)

    container = ttk.Frame(self)
    container.grid()

    entry_frame = Entry(container)
    entry_frame.grid(row=0,column=0,sticky='W')

class Entry(ttk.Frame):
  def __init__(self,parent):
    super().__init__(parent)
    self.name = tk.StringVar()
    self.phone_number = tk.StringVar()
    self.Relationship = tk.StringVar()

    # Labels
    name_label = ttk.Label(self,text='Name: ')
    phone_label = ttk.Label(self,text='Phone: ')
    relationship_label = ttk.Label(self,text='Relationship: ')

    name_label.grid(row=0,column=0,sticky='W')
    phone_label.grid(row=1,column=0,sticky='W')
    relationship_label.grid(row=2,column=0,sticky='W')


phonebook = AddressBook()
phonebook.mainloop()