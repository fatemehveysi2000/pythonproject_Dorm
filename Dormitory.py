from tkinter import *
import tkinter

class Main_Page:
    def __init__ (self, root):
        MailPage = tkinter.Tk()
        MailPage.configure(bg="black")
        MailPage.geometry("600x600")
        MailPage.title("Main Page")

        BlockBTN = Button(MailPage, text='Block', width="50", height="2", bd='3', activebackground='green', bg='white')
        EmployeeBTN = Button(MailPage, text='Employee', width="50", height="2", bd='3', activebackground='#0000ff', bg='white')
        SrearchBTN = Button(MailPage, text='Search', width='50', height='2', bd='3', activebackground='#ff8000', bg='white')

        label = Label(MailPage, text='Welcome Boss!', font=("Courier", 24 ))
        label.place(x='10', y='10')

        BlockBTN.pack(padx=5, pady=20)
        EmployeeBTN.pack(padx=5,pady=100)
        SrearchBTN.pack(padx=5,pady=100)

        SrearchBTN.mainloop()
        BlockBTN.mainloop()
        EmployeeBTN.mainloop()
        MailPage.mainloop()

        MailPage.bind()

if __name__ == '__main__':
    root=Tk()
    first=Main_Page(root)
    root.mainloop()
