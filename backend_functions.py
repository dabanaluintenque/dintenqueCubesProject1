# author: Dabana Intenque
import sqlite3

from tkinter.ttk import Entry

con = sqlite3.connect('cubes_database.db')
cursor = con.cursor()


def text_fields() -> []:
    prefix_box = Entry()
    prefix_box.place(x=220, y=150)

    first_name_box = Entry()
    first_name_box.place(x=220, y=200)

    last_name_box = Entry()
    last_name_box.place(x=220, y=250)

    title_box = Entry()
    title_box.place(x=220, y=300)

    organization_name_box = Entry()
    organization_name_box.place(x=220, y=350)

    organization_website_box = Entry()
    organization_website_box.place(x=220, y=400)

    email_box = Entry()
    email_box.place(x=220, y=450)

    phone_number_box = Entry()
    phone_number_box.place(x=220, y=500)

    arr = [prefix_box, first_name_box, last_name_box, title_box,
           organization_name_box, organization_website_box, email_box, phone_number_box]

    return arr


def display_data() -> list[dict]:
    cursor.execute('SELECT * FROM cubesProposal')
    rows = cursor.fetchall()
    list_of_entries = []
    for row in rows:
        list_of_entries.append(row)

    return list_of_entries


def first_entry():
    text_field_entry = text_fields()
    list_data = display_data()
    text_list = []
    lists_of_entry = []

    for j in text_field_entry:
        text_list.append(j)

    for i in list_data[0]:
        lists_of_entry.append(i)
    text_list[0].insert(0, lists_of_entry[1])
    text_list[1].insert(0, lists_of_entry[2])
    text_list[2].insert(0, lists_of_entry[3])
    text_list[3].insert(0, lists_of_entry[4])
    text_list[4].insert(0, lists_of_entry[5])
    text_list[5].insert(0, lists_of_entry[6])
    text_list[6].insert(0, lists_of_entry[7])
    text_list[7].insert(0, lists_of_entry[8])


def second_entry():
    text_field_entry = text_fields()
    list_data = display_data()
    text_list = []
    lists_of_entry = []

    for j in text_field_entry:
        text_list.append(j)

    for i in list_data[1]:
        lists_of_entry.append(i)
    text_list[0].insert(0, lists_of_entry[1])
    text_list[1].insert(0, lists_of_entry[2])
    text_list[2].insert(0, lists_of_entry[3])
    text_list[3].insert(0, lists_of_entry[4])
    text_list[4].insert(0, lists_of_entry[5])
    text_list[5].insert(0, lists_of_entry[6])
    text_list[6].insert(0, lists_of_entry[7])
    text_list[7].insert(0, lists_of_entry[8])


def third_entry():
    text_field_entry = text_fields()
    list_data = display_data()
    text_list = []
    lists_of_entry = []

    for j in text_field_entry:
        text_list.append(j)

    for i in list_data[2]:
        lists_of_entry.append(i)
    text_list[0].insert(0, lists_of_entry[1])
    text_list[1].insert(0, lists_of_entry[2])
    text_list[2].insert(0, lists_of_entry[3])
    text_list[3].insert(0, lists_of_entry[4])
    text_list[4].insert(0, lists_of_entry[5])
    text_list[5].insert(0, lists_of_entry[6])
    text_list[6].insert(0, lists_of_entry[7])
    text_list[7].insert(0, lists_of_entry[8])


def fourth_entry():
    text_field_entry = text_fields()
    list_data = display_data()
    text_list = []
    lists_of_entry = []

    for j in text_field_entry:
        text_list.append(j)

    for i in list_data[3]:
        lists_of_entry.append(i)
    text_list[0].insert(0, lists_of_entry[1])
    text_list[1].insert(0, lists_of_entry[2])
    text_list[2].insert(0, lists_of_entry[3])
    text_list[3].insert(0, lists_of_entry[4])
    text_list[4].insert(0, lists_of_entry[5])
    text_list[5].insert(0, lists_of_entry[6])
    text_list[6].insert(0, lists_of_entry[7])
    text_list[7].insert(0, lists_of_entry[8])


# clear the entry
def clear_entry():
    text_field_entry = text_fields()
    print(text_field_entry[0])
    text_field_list = []
    for entry in text_field_entry:
        text_field_list.append(entry)

    text_field_list[0].delete(0, 'end')
    text_field_list[1].delete(0, 'end')
    text_field_list[2].delete(0, 'end')
    text_field_list[3].delete(0, 'end')
    text_field_list[4].delete(0, 'end')
    text_field_list[5].delete(0, 'end')
    text_field_list[6].delete(0, 'end')
    text_field_list[7].delete(0, 'end')