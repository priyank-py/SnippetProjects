from tkinter import *
from tkinter import messagebox

root = Tk()

menubar = Menu(root)

def open_something():
    pass

def find_str():
    pass

def replace_str():
    pass



files = Menu(menubar, tearoff=0)
files.add_command(label='Open', command=open_something)
files.add_command(label='Quit', command=quit)
menubar.add_cascade(label='File', menu=files)

edits = Menu(menubar, tearoff=0)
edits.add_command(label='Find', command=find_str)
edits.add_command(label='Replace', command=replace_str)
menubar.add_cascade(label='Edit', menu=edits)




Label(root, text='username').grid(row=0, column=0)
user_name = Entry(root)
user_name.grid(row=0, column=1)

Label(root, text='email').grid(row=1, column=0)
email_id = Entry(root)
email_id.grid(row=1, column=1)

Label(root, text='Gender').grid(row=2, column=0)

options = Canvas(root)

genders = StringVar()
male = Radiobutton(options, text='male', variable=genders, value=False)
male.grid(row=0, column=0)
female = Radiobutton(options, text='female', variable=genders, value=True)
female.grid(row=0, column=1)

options.grid(row=2, column=1)

Label(root, text='Password').grid(row=3, column=0)
pass_word = Entry(root, show='\u2022')
pass_word.grid(row=3, column=1)

rem = StringVar();
remember_me = Checkbutton(root, text='Remember me', variable=rem)
remember_me.grid(row=4, column=0);

def do_this():
    user = user_name.get()
    email = email_id.get()
    gender = genders.get()
    password = pass_word.get()
    remember = rem.get()

    Label(root, text=f'user\n{email}\n{gender}\n{password}\n{remember}').grid(row=6)
    messagebox.showinfo('Information', 'Data Saved')


Button(root, text='login', width=10, command=do_this).grid(row=5)

root.config(menu=menubar)
root.mainloop()
