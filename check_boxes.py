# author: Dabana Intenque
from tkinter import Checkbutton
import tkinter as tk


def list_checkbox() -> list[tk]:
    checked = tk.StringVar()
    Course_Project_check_box = Checkbutton(text='Course Project', variable=checked, onvalue='on',
                                           offvalue='off')
    Course_Project_check_box.place(x=250, y=600)

    Guest_Speaker_check_box = Checkbutton(text="Guest Speaker", variable=checked, onvalue="on",
                                          offvalue="off")
    Guest_Speaker_check_box.place(x=250, y=650)

    Site_Visit_check_box = Checkbutton(text="Site Visit", variable=checked, onvalue='on',
                                       offvalue='off')
    Site_Visit_check_box.place(x=250, y=700)

    Job_Shadow_check_box = Checkbutton(text="Job Shadow", variable=checked, onvalue='on',
                                       offvalue='off')
    Job_Shadow_check_box.place(x=250, y=750)

    Internships_check_box = Checkbutton(text="Internship", variable=checked, onvalue='on',
                                        offvalue='off')
    Internships_check_box.place(x=250, y=800)

    arr = [Course_Project_check_box, Guest_Speaker_check_box,
           Site_Visit_check_box, Job_Shadow_check_box, Internships_check_box]

    list_of_values = []

    return list_of_values

