# author: Dabana Intenque

from tkinter import *
import sqlite3 as sq
from tkinter import ttk

import tkinter as tk
from tkinter.messagebox import showinfo

window = Tk()
window.title("Cubes Data")

# window
window.geometry('1000x700+100+100')

# list to select from
list_items = ('CEO', 'President', 'Dean', 'Department Manager')
variables = tk.Variable(value=list_items)

listbox = tk.Listbox(
    window,
    listvariable=variables,
    height=4,
    selectmode=SINGLE
)

Label(window, text="cubes data info",
      font=("arial", 30, "bold"), fg="black").pack()

# connect to sql
con = sq.connect('cubes_database.db')
cursor = con.cursor()


def display_data() -> list[dict]:
    cursor.execute('SELECT * FROM cubesProposal')
    rows = cursor.fetchall()
    list_of_entries = []
    for row in rows:
        list_of_entries.append(row)

    return list_of_entries


Label(window, text="Prefix:", font=("arial", 17)).place(x=10, y=150)
Label(window, text="First Name:", font=("arial", 17)).place(x=10, y=200)
Label(window, text="Last Name:", font=("arial", 17)).place(x=10, y=250)
Label(window, text="Title:", font=("arial", 17)).place(x=10, y=300)
Label(window, text="Organization Name:", font=("arial", 17)).place(x=10, y=350)
Label(window, text="organization Website", font=("arial", 17)).place(x=10, y=400)
Label(window, text="Email:", font=("arial", 17)).place(x=10, y=450)
Label(window, text="Phone Number:", font=("arial", 17)).place(x=10, y=500)

prefix_box = Entry(window)
prefix_box.place(x=220, y=150)

first_name_box = Entry(window)
first_name_box.place(x=220, y=200)

last_name_box = Entry(window)
last_name_box.place(x=220, y=250)

title_box = Entry(window)
title_box.place(x=220, y=300)

organization_name_box = Entry(window)
organization_name_box.place(x=220, y=350)

organization_website_box = Entry(window)
organization_website_box.place(x=220, y=400)

email_box = Entry(window)
email_box.place(x=220, y=450)

phone_number_box = Entry(window)
phone_number_box.place(x=220, y=500)


# list from sql
def first_entry():
    entry_1 = display_data()
    lists_of_entry = list[dict]
    lists_of_entry = []
    for i in entry_1[0]:
        lists_of_entry.append(i)

    prefix_box.insert(0, lists_of_entry[1])
    first_name_box.insert(0, lists_of_entry[2])
    last_name_box.insert(0, lists_of_entry[3])
    title_box.insert(0, lists_of_entry[4])
    organization_name_box.insert(0, lists_of_entry[5])
    organization_website_box.insert(0, lists_of_entry[6])
    email_box.insert(0, lists_of_entry[7])
    phone_number_box.insert(0, lists_of_entry[8])


def second_entry():
    entry_1 = display_data()
    lists_of_entry = list[dict]
    lists_of_entry = []
    for i in entry_1[1]:
        lists_of_entry.append(i)

    prefix_box.insert(0, lists_of_entry[1])
    first_name_box.insert(0, lists_of_entry[2])
    last_name_box.insert(0, lists_of_entry[3])
    title_box.insert(0, lists_of_entry[4])
    organization_name_box.insert(0, lists_of_entry[5])
    organization_website_box.insert(0, lists_of_entry[6])
    email_box.insert(0, lists_of_entry[7])
    phone_number_box.insert(0, lists_of_entry[8])


def third_entry():
    entry_1 = display_data()
    lists_of_entry = list[dict]
    lists_of_entry = []
    for i in entry_1[3]:
        lists_of_entry.append(i)

    prefix_box.insert(0, lists_of_entry[1])
    first_name_box.insert(0, lists_of_entry[2])
    last_name_box.insert(0, lists_of_entry[3])
    title_box.insert(0, lists_of_entry[4])
    organization_name_box.insert(0, lists_of_entry[5])
    organization_website_box.insert(0, lists_of_entry[6])
    email_box.insert(0, lists_of_entry[7])
    phone_number_box.insert(0, lists_of_entry[8])


def fort_entry():
    entry_1 = display_data()
    lists_of_entry = list[dict]
    lists_of_entry = []
    for i in entry_1[4]:
        lists_of_entry.append(i)

    prefix_box.insert(0, lists_of_entry[1])
    first_name_box.insert(0, lists_of_entry[2])
    last_name_box.insert(0, lists_of_entry[3])
    title_box.insert(0, lists_of_entry[4])
    organization_name_box.insert(0, lists_of_entry[5])
    organization_website_box.insert(0, lists_of_entry[6])
    email_box.insert(0, lists_of_entry[7])
    phone_number_box.insert(0, lists_of_entry[8])


# clear the entry
def clear_entry():
    prefix_box.delete(0, 'end')
    first_name_box.delete(0, 'end')
    last_name_box.delete(0, 'end')
    title_box.delete(0, 'end')
    organization_website_box.delete(0, 'end')
    organization_name_box.delete(0, 'end')
    email_box.delete(0, 'end')
    phone_number_box.delete(0, 'end')


def selected_items(event):
    # all the list values
    select_value = listbox.curselection()

    # selected values

    select_list_items = \
        ",".join([listbox.get(j)
                  for j in select_value])

    if select_list_items == 'CEO':
        clear_entry()
        first_entry()

    elif select_list_items == 'President':
        clear_entry()
        second_entry()

    elif select_list_items == 'Dean':
        clear_entry()
        third_entry()

    else:
        clear_entry()
        fort_entry()

    message = f'Click ok to know who is the: {select_list_items}'
    showinfo('0', message=message, command=select_list_items)


def main():
    first_entry()
    listbox.bind('<<ListboxSelect>>', selected_items)
    listbox.place()
    listbox.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
