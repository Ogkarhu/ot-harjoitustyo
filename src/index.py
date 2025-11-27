import tkinter as tk
from budget import Budget


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.budget = Budget()
        self.pack()

        self.expense_label = tk.Label(master,text="Add expense")
        self.expense_label.pack()
        
        self.expense_entry = tk.Entry()
        self.expense_entry.pack()

        self.textthingy_income = tk.Label(master,text="Add income")
        self.textthingy_income.pack()
        
        self.income_entry = tk.Entry()
        self.income_entry.pack()

        self.budget_display = tk.Text(self, width=70,height=30)
        self.budget_display.pack()

        self.budget_display.insert(tk.END,"")


        
        # Create the application variabl"e.
        self.content_expense = tk.StringVar()
        self.content_income = tk.StringVar()

        # Set it to some value.
        #self.contents.set("")
        # Tell the entry widget to watch this variable.
        self.expense_entry["textvariable"] = self.content_expense
        print(self.budget.get_budget())

        self.income_entry["textvariable"] = self.content_income

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.

        self.expense_entry.bind('<Key-Return>',
                             self.add_expense)

        self.income_entry.bind('<Key-Return>',
                            self.add_income)

    def fetch_budget(self):
        budget_output = self.budget.get_budget()


    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.content_expense.get())

    def add_expense(self, event):
        value =self.content_expense.get()

        #osittain tekoälygeneroitu osa alkaa
        try:
            amount = int(value)
        except ValueError:
            print("Insert a valid sum")
            return
        self.budget.add_expense(amount)
        print("Added expense:",amount)
        #osittain tekoälygeneroitu osa loppuu
        self.content_expense.set("")


    def add_income(self, event):
        value =self.content_income.get()

        try:
            amount = int(value)
        except ValueError:
            print("Insert a valid sum")
            return
        self.budget.add_income(amount)
        print("Added income:",amount)
        self.content_income.set("")


root = tk.Tk()
myapp = App(root)
myapp.mainloop()