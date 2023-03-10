# author: Dabana Intenque
from tkinter import Tk, SINGLE, Frame, Variable, Listbox
from tkinter.ttk import Button

import Labels_folder
import backend_functions
import check_boxes


class cubes_main_window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.geo = '1300x850+300+100'
        self.title = "Cubes Project 1"


main_window = Tk()
app = cubes_main_window(master=main_window)


def Show_Views():
    Labels_folder.all_labels()
    check_boxes.list_checkbox()
    backend_functions.first_entry()
    listbox_entries.place(x=700, y=100)


list_items = ('CEO', 'President', 'Dean', 'Department Manager')
variables = Variable(value=list_items)

listbox_entries = Listbox(main_window,
                          font=("arial", 20),
                          listvariable=variables,
                          height=4,
                          selectmode=SINGLE
                          )


def selected_items(events):
    selected_value = listbox_entries.curselection()

    select_list_items = \
        ",".join([listbox_entries.get(j)
                  for j in selected_value])
    if select_list_items == "CEO":
        backend_functions.first_entry()

    elif select_list_items == "President":
        backend_functions.clear_entry()
        backend_functions.second_entry()

    elif select_list_items == "Dean":
        backend_functions.clear_entry()
        backend_functions.third_entry()

    else:
        backend_functions.clear_entry()
        backend_functions.fourth_entry()


def Update():
    update_btn = Button(text='Click to update Data in Database', command=backend_functions.update_database)
    update_btn.place(x=10, y=90)


def Visualize():
    visualize_btn = Button(main_window, text='Click to visualize Data', command=Show_Views)
    visualize_btn.place(x=10, y=10)


def clear_frame_btn():
    clear_btn = Button(main_window, text='Please click here to Clear first before update or visualize', command=clearWindow)
    clear_btn.place(x=10, y=50)
    Update()
    Visualize()


def clearWindow():
    for widget in main_window.winfo_children():
        widget.destroy()
    clear_frame_btn()


def runWindow():
    main_window.geometry(app.geo)
    main_window.title(app.title)
    listbox_entries.bind('<<ListboxSelect>>', selected_items)

    clear_frame_btn()
    app.mainloop()
    app.destroy()


if __name__ == '__main__':
    runWindow()
