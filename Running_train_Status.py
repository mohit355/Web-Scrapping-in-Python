import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter.font import Font
from tkinter import messagebox

root=tk.Tk()
root.title("running train status")


def Actions():
    train_no=train.get()
    Date=date.get()
    print(len(Date))
    day,month,year=Date.split("-")
    train_no_length=len(train_no)
    if train_no_length<5 or len(Date)>10 or len(Date)<7:
        messagebox.showerror("missing value","something missing")
    elif train_no_length>5:
        messagebox.showerror("to long","train number is too long")
    else:
        webbrowser.open("https://runningstatus.in/status/"+str(train_no)+"-on-"+year+month+day)
        l4=tk.Label(root,text="thanks for using our app").grid(row=5,column=1)


fonts=Font(size=30,family='HelvLight',weight='bold',slant='italic',underline=1,overstrike=0)

l1=ttk.Label(root,text="Welcome to running status",font=fonts)
l1.grid(row=0,columnspan=9,padx=10,pady=20)


labelframe=tk.LabelFrame(root,text="Enter train details")

l2=tk.Label(labelframe,text="Enter train number",fg="blue").grid(row=0,column=0,padx=4,pady=4)
l3=tk.Label(labelframe,text="Enter running date",fg="blue").grid(row=1,column=0,padx=4,pady=4)

train=tk.StringVar()
entry1=tk.Entry(labelframe,textvariable=train).grid(row=0,column=1,padx=4,pady=4)

date=tk.StringVar()
entry2=tk.Entry(labelframe,textvariable=date).grid(row=1,column=1,padx=4,pady=4)

button1=tk.Button(root,text="SEARCH",fg="red",command=Actions).grid(row=3,columnspan=10)
button2=tk.Button(root,text="EXIT",fg="orange",command=root.quit).grid(row=4,columnspan=10)

labelframe.grid(row=2,columnspan=10)

root.configure(bg="yellow")

root.geometry("550x250+120+120")

root.resizable(0,0)
root.mainloop()
