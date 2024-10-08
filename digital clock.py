from tkinter import *
import time as t

cl=Tk()
cl.title("DIGITAL CLOCK")
cl.geometry("815x150")

l=Label(cl,font=("Times New Roman",110,'bold'),bg="yellow",fg="green")
l.pack()
def digiClock():
    time=t.strftime('%H:%M:%S %p')
    l.config(text=time)
    l.after(60,digiClock)


digiClock()
mainloop()
