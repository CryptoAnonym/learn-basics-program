from tkinter import *

app = Tk()
app.geometry('440x580')

e = Entry(app,width=50)
e.pack()

print(type(e))

def myClick():
    if str(e.get()) == "z":
        myLabel = Label(app, text="Prawidłowy: " + e.get())
        myLabel.pack()
    else:
        Label(app, text="Error " + e.get()).pack()


myButton = Button(app, text="Wpisz cos: ", command=myClick)
myButton.pack()
 
app.mainloop()