
from tkinter import *

import tkinter.ttk as ttk


# ------------------------------------------- Class -----------------------------------
array = []


# =============================(CLASSES)==========================


def Exit(root):
    print("exit")
    root.destroy()


class Employee:

    def __init__(self, name, family, roll, personal_number):
        self.name = name
        self.family = family
        self.roll = roll
        self.personal_number = personal_number


class Student:

    def __init__(self, name, family, field, student_number):
        self.name = name
        self.family = family
        self.field = field
        self.student_number = student_number


class Room:

    def __init__(self, number, block_name, floor, students):
        self.number = number
        self.block_name = block_name
        self.floor = floor
        self.students = students


class Block:
    def __init__(self, block_name, code, supervisor, rooms):
        self.code = code
        self.block_name = block_name
        self.superviser = supervisor
        self.rooms = rooms


# -------------------------- pages ------------------------------------

class Main_Page:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="black")
        self.root.geometry("600x600")
        self.root.title("Main Page")

        BlockBTN = Button(self.root, text='Block', width="10", height="1", bd='3', activebackground='green', bg='white')
        EmployeeBTN = Button(self.root, text='Employee', width="10", height="1", bd='3', activebackground='#0000ff',
                             bg='white',
                             command=lambda: rabet(employee_menu, root))
        SrearchBTN = Button(self.root, text='Search', width='10', height='1', bd='3', activebackground='#ff8000',
                            bg='white')

        Exit_BTN = Button(self.root, text='EXIT', width='10', height='1', bd='3', activebackground='#ff8000',
                          bg='white',
                          command=lambda: Exit(self.root))

        label = Label(self.root, text='Welcome Boss!', font=("Courier", 12))
        label.place(x='80', y='280')

        BlockBTN.pack(padx=5, pady=20)
        EmployeeBTN.pack(padx=5, pady=20)
        SrearchBTN.pack(padx=5, pady=20)
        Exit_BTN.pack(padx=5, pady=20)

        self.root.geometry("%dx%d+%d+%d" % (300, 300, 500, 200))
        self.root.resizable(0, 0)


# ----------------------------------منوی کارمندان-----------------------------------
class employee_menu:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="black")
        self.root.geometry("600x600")
        self.root.title("Emoloyee_Menu")

        AddBTN = Button(self.root, text='Add', width="10", height="1", bd='3', activebackground='green',
                        bg='white', command=lambda: rabet(add_staff, root))
        RemoveBTN = Button(self.root, text='Remove', width="10", height="1", bd='3', activebackground='#0000ff',
                           bg='white', command=lambda: rabet(remove_staff, root))
        ShowList_BTN = Button(self.root, text='Show List', width='10', height='1', bd='3', activebackground='#ff8000',
                              bg='white', command=lambda: rabet(show_List, root))

        AddBTN.pack(padx=5, pady=20)
        RemoveBTN.pack(padx=5, pady=20)
        ShowList_BTN.pack(padx=5, pady=20)

        self.root.geometry("%dx%d+%d+%d" % (300, 300, 500, 200))
        self.root.resizable(0, 0)


# ===============================================================
class rabet:
    def __init__(self, _class, root):
        self.new = Toplevel(root)
        _class(self.new)


class add_staff:
    def __init__(self, root):
        self.root = root
        self.root.title("signup menu")
        self.root["bg"] = "black"

        self.root.geometry("%dx%d+%d+%d" % (500, 300, 500, 200))
        self.root.resizable(0, 0)

        FIRSTNAME = StringVar()
        LASTNAME = StringVar()
        PERSONAL_NUMBER = StringVar()
        ROLL = StringVar()

        ContactForm = Frame(root)

        ContactForm.pack(side=TOP, pady=50, padx=100)

        lbl_firstname = Label(ContactForm, text="Firstname", font=('arial', 14), bd=5)
        lbl_firstname.grid(row=0, sticky=W)

        lbl_lastname = Label(ContactForm, text="Lastname", font=('arial', 14), bd=5)
        lbl_lastname.grid(row=1, sticky=W)

        lbl_roll = Label(ContactForm, text="Roll", font=('arial', 14), bd=5)
        lbl_roll.grid(row=3, sticky=W)

        lbl_personalnumber = Label(ContactForm, text="Personal Number", font=('arial', 14), bd=5)
        lbl_personalnumber.grid(row=5, sticky=W)

        firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
        firstname.grid(row=0, column=1)
        lastname = Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
        lastname.grid(row=1, column=1)

        roll = Entry(ContactForm, textvariable=ROLL, font=('arial', 14))
        roll.grid(row=3, column=1)

        personalnumber = Entry(ContactForm, textvariable=PERSONAL_NUMBER, font=('arial', 14))
        personalnumber.grid(row=5, column=1)
        btn_save = Button(ContactForm, text="Save", width=50,
                          command=lambda: self.Save_staff(FIRSTNAME.get(), LASTNAME.get(), ROLL.get(),
                                                          PERSONAL_NUMBER.get()))
        btn_save.grid(row=6, columnspan=2, pady=10)
        ContactForm.pack()


    def Save_staff(self, name, family, roll, personalnmber):
        array.append(Employee(name, family, roll, personalnmber))


# ----------------------------------- حذف کامندان --------------------------------------------

class remove_staff:
    def __init__(self, root):


        self.root = root
        self.root.title("remove staff")
        self.root["bg"] = "black"

        self.root.geometry("%dx%d+%d+%d" % (500, 300, 500, 200))
        self.root.resizable(0, 0)

        TableMargin = Frame(root, width=500)
        TableMargin.pack(side=TOP)

        tree = ttk.Treeview(TableMargin,
                            columns=("Name", "Lastname", "Roll", "Personal Number"),
                            height=400, selectmode="extended"
                            )


        tree.heading('Name', text="Name", anchor=W)
        tree.heading('Lastname', text="Lastname", anchor=W)
        tree.heading('Roll', text="Roll", anchor=W)
        tree.heading('Personal Number', text="Personal Number", anchor=W)

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=80)
        tree.column('#2', stretch=NO, minwidth=0, width=100)
        tree.column('#3', stretch=NO, minwidth=0, width=140)

        tree.pack()
        for object in array:
            tree.insert('', 'end', values=(object.name, object.family, object.roll, object.personal_number))

        inputNumber = IntVar()
        lbl_input = Label(self.root, text="Enter number", font=('arial', 10), bd=5)
        lbl_input.place(x=5, y=200)

        input = Entry(self.root, textvariable=inputNumber, width=16, font=('arial', 14))
        input.place(x=110, y=200)

        staffRemoveBtn = Button(self.root, text="Remove", command=lambda: self.reamove_Staff(inputNumber), width=30)
        staffRemoveBtn.place(x=140,y=270)

    def reamove_Staff(self, num):
        if (num.get()<=array.__len__() and num.get()>0):
            del array[num.get() - 1]
        else:
            print("no such Employee")


# --------------------- showlist-----------------------

class show_List:
    def __init__(self,root):
        self.root = root
        self.root.title("show list")
        self.root["bg"] = "black"

        self.root.geometry("%dx%d+%d+%d" % (500, 300, 500, 200))
        self.root.resizable(0, 0)

        TableMargin = Frame(root, width=500)
        TableMargin.pack(side=TOP)

        tree = ttk.Treeview(TableMargin,
                            columns=("Name", "Lastname", "Roll", "Personal Number"),
                            height=400, selectmode="extended"
                           )



        tree.heading('Name', text="Name", anchor=W)
        tree.heading('Lastname', text="Lastname", anchor=W)
        tree.heading('Roll', text="Roll", anchor=W)
        tree.heading('Personal Number', text="Personal Number", anchor=W)

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=80)
        tree.column('#2', stretch=NO, minwidth=0, width=100)
        tree.column('#3', stretch=NO, minwidth=0, width=140)


        tree.pack()
        for object in array:
            tree.insert('', 'end', values=(object.name,object.family,object.roll,object.personal_number))








# ------------------------------ Main ------------------------------

if __name__ == '__main__':
    root = Tk()

    first = Main_Page(root)
    root.mainloop()

