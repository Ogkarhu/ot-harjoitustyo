import tkinter as tk
import sqlite3

con = sqlite3.connect(":memory:")#vaihda oikeaan kun tallennetaan esim. connect(budget)
cur = con.cursor()
cur.execute("CREATE TABLE budget(income,expense)")
cur.execute("""
    INSERT INTO budget (income, expense)
    VALUES
        (3000, 800),
        (4500, 1500),
        (5200, 2000)
""")


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents
        print(self.get_budget())
        # Define a callback for when the user hits return.
        # It prints the current value of the variable.

        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

    def get_budget(self):
        cur.execute("SELECT * FROM budget")
        return cur.fetchall()


root = tk.Tk()
myapp = App(root)
myapp.mainloop()