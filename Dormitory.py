from tkinter import *
import tkinter

class Main_Page:
    def __init__ (self, root):
        self.root=root
        self.root.configure(bg="black")
        self.root.geometry("600x600")
        self.root.title("Main Page")

        BlockBTN = Button(self.root, text='Block', width="50", height="2", bd='3', activebackground='green', bg='white')
        EmployeeBTN = Button(self.root, text='Employee', width="50", height="2", bd='3', activebackground='#0000ff', bg='white')
        SrearchBTN = Button(self.root, text='Search', width='50', height='2', bd='3', activebackground='#ff8000', bg='white')

        label = Label(self.root, text='Welcome Boss!', font=("Courier", 24 ))
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
