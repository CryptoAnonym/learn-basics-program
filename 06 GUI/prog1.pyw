import tkinter as tk

# --- classes ---

class UIProgram():

    def __init__(self, master):
        self.master = master # use to add elements directly to main window

        self.buttons = [] # keep buttons to change text

        # frame to group buttons and easily remove all buttons (except `Next`)
        self.frame = tk.Frame(self. master)
        self.frame.pack()

        # group button in frame
        button = tk.Button(self.frame, text='Sanjam', command=self.wrong)
        button.pack()
        self.buttons.append(button)

        button = tk.Button(self.frame, text='Sunny the Bunny', command=self.wrong)
        button.pack()
        self.buttons.append(button)

        button = tk.Button(self.frame, text='Sunjum', command=self.right)
        button.pack()
        self.buttons.append(button)

        button = tk.Button(self.frame, text='bob', command=self.wrong)
        button.pack()
        self.buttons.append(button)

        # button outside frame
        button_next = tk.Button(self.master, text='Next >>', command=self.reset)
        button_next.pack()

        self.label = tk.Label(self.frame)
        self.label.pack()


    def wrong(self):
        # create second window with message and closing button
        win = tk.Toplevel()
        tk.Label(win, text="WRONG!, you stupid idiot!!!!").pack()
        tk.Button(win, text='close', command=win.destroy).pack()

    def right(self):
        # create second window with message and closing button
        win = tk.Toplevel()
        tk.Label(win, text="CORRECT, good job!").pack()
        tk.Button(win, text='close', command=win.destroy).pack()

    def reset(self):
        # remove frame with all buttons
        self.frame.pack_forget()
        tk.Label(self.master, text="frame removed").pack()

        # or only remove text in labels
        #for button in self.buttons:
        #    button['text'] = '-- place for new text --'

# --- main ---

root = tk.Tk()
root.geometry('600x400')
root.title('hello world')

program = UIProgram(root)

root.mainloop()