from tkinter import *
def click_me():
    l=Label(root,text='Welcome')
    l.pack()
root=Tk()
root.geometry('2000x500')
b=Button(root,text='Click Me',font=('times new roman',40),bg='#100349',fg='white',activebackground='#340765',activeforeground='#723123',command=click_me)
b.pack()
root.mainloop()
