from tkinter import *
from tkinter.scrolledtext import ScrolledText
window=Tk()
# add widgets here
Label(window, text="enter what do you want anything") .grid(row=1, column=0, sticky=W)
entry=Entry(window, width=20, bg="light green") .grid(row=2, column=0, sticky=W)
btn=Button(window, text="This is button", width=10, fg="green") .grid(row=3, column=0, sticky=W)
Button(window, text="output", command=(lambda: print(entry.get(2.0, END)))) .grid(row=4, column=0, sticky=W)
window.title('Hello Python')
window.geometry("300x200+10+20")
window.mainloop()