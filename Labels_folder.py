# author: Dabana Intenque
from tkinter import Label


def all_labels():
    Label(text="Prefix:", font=("arial", 17)).place(x=10, y=150)
    Label(text="First Name:", font=("arial", 17)).place(x=10, y=200)
    Label(text="Last Name:", font=("arial", 17)).place(x=10, y=250)
    Label(text="Title:", font=("arial", 17)).place(x=10, y=300)
    Label(text="Organization Name:", font=("arial", 17)).place(x=10, y=350)
    Label(text="organization Website", font=("arial", 17)).place(x=10, y=400)
    Label(text="Email:", font=("arial", 17)).place(x=10, y=450)
    Label(text="Phone Number:", font=("arial", 17)).place(x=10, y=500)
    # Label(text="cubes data info",
    #      font=("arial", 30, "bold"), fg="black").pack()
