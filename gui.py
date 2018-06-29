from tkinter import *
from tkinter import messagebox
from database import  Data

database = Data("bookstore.db")

class Frontend(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("My Book Store")

        l1 = Label(window,font=("ALGERIAN",20),bg="blue",bd=10, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(window,font=("ALGERIAN",20),bg="blue",bd=10,text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(window, font=("ALGERIAN",20),bg="blue",bd=10,text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(window,font=("ALGERIAN",20),bg="blue",bd=10, text="ISBN")
        l4.grid(row=1, column=2)

        self.title_text = StringVar()
        self.e1 = Entry(window,insertwidth=10,bd=0,font=("arial",15), textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.e2 = Entry(window, insertwidth=10,bd=0,font=("arial",15),textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.e3 = Entry(window,insertwidth=10,bd=0,font=("arial",15), textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.ISBN_text = StringVar()
        self.e4= Entry(window, insertwidth=10,bd=0,font=("arial",15),textvariable=self.ISBN_text)
        self.e4.grid(row=1, column=3)

        self.list1 = Listbox(window, height=20, width=70)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)


        b1 = Button(window, padx=25,pady=15,bd=8,bg="blue",fg="White",font=("arial",10),text="View all", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(window, padx=25,pady=15,bd=8,bg="blue",fg="White",font=("arial",10),text="Search entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(window, padx=25,pady=15,bd=8,bg="blue",fg="White",font=("arial",10),text="Add entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, padx=25,pady=15,bd=8,bg="blue",fg="White",font=("arial",10),text="Update selected", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, padx=25,pady=15,bd=8,bg="blue",fg="White",font=("arial",10),text="Delete selected", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(window, padx=25,pady=15,bd=8,bg="blue",fg="White",font=("arial",10),text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)


    def get_selected_row(self,event):  
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass              

    def view_command(self):
        self.list1.delete(0, END)  
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.ISBN_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        self.list1.delete(0, END)
        if self.title_text.get()!="" and self.author_text.get()!="" and self.year_text.get()!="" and self.ISBN_text.get()!=null:
            database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
            self.list1.delete(0, END)
            self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()))

        
    def delete_command(self):
        try:
             database.delete(self.selected_tuple[0])
             self.view_command()
        except(AttributeError):
            messagebox.showinfo("No book selected", "Please select a book!")
       

    def update_command(self):
        try:
            database.update(self.selected_tuple[0],self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
            self.view_command()
        
        except(AttributeError):
            messagebox.showinfo("No book selected", "Please select a book!")


frontend = Tk()
frontend.geometry("800x600")
frontend.configure(background='cyan2')
Frontend(frontend)
frontend.mainloop()
