from tkinter import *
s="lightgrey"
window=Tk()
window.geometry("500x500")
window.config(background=s)
lbl_1=Label(window,text="Enter the Password",fg="black",bg=s,font=("Agency FB",30))
lbl_2=Label(window,text="Hint=The password has only 4 digits ang one bit can be only 0 or 1",fg="black",bg=s,font=("Vijaya",10))
src= Entry(window,width=60)
src.pack(side=TOP)
lbl_1.pack()
lbl_2.pack()
window.mainloop()