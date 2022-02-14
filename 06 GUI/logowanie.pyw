from tkinter import *
import tkinter

root_window = Tk() #Creates window
root_window.title("Tutorial Login") #Gives title to window
root_window.geometry("500x500") #Makes the window size 500x500


Label(root_window, text = "Username:").pack()
userEntry = Entry(root_window)
userEntry.pack()

root_window.mainloop()