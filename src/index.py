import tkinter as tk
from budget import Budget


class App(tk.Frame):
    """Luokka joka muodostaa sovelluksen graafisen ikkunan

    """
    def __init__(self, master):
        """Konstruktori joka luo ikkunaan kaikki elementit ja ominaisuudet
        """
        super().__init__(master)
        
        self.budget = Budget()
        self.pack()

        #Teksti: Add expense
        self.expense_label = tk.Label(master,text="Add expense")
        self.expense_label.pack()
        #Kenttä kulun lisäämiseen
        self.expense_entry = tk.Entry()
        self.expense_entry.pack()
        #Teksti: Add income
        self.textthingy_income = tk.Label(master,text="Add income")
        self.textthingy_income.pack()
        #Kenttä tulon lisäämiseen
        self.income_entry = tk.Entry()
        self.income_entry.pack()
        #Tekstilaatikko kussakin hetkessä kulujen, menojen tai budjetin
        #näyttämiseksi
        self.budget_display = tk.Text(self, width=70,height=30)
        self.budget_display.pack()

        self.budget_display.insert(tk.END,str(self.fetch_budget()))
        #income-nappi
        self.income_button = tk.Button(self, text="Show income",command=self.fetch_income)
        self.income_button.pack()
        #näyttö tulojen summalle
        self.income_display = tk.Text(self, width=10,height=1)
        self.income_display.pack()
        #expense-nappi
        self.expense_button = tk.Button(self, text="Show expenses",command=self.fetch_expense)
        self.expense_button.pack()
        #näyttö menojen summalle
        self.expense_display = tk.Text(self, width=10,height=1)
        self.expense_display.pack()
        
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

    def fetch_income(self):
        """Kutsuu budget.get_income() ja näyttää tulot oikeassa
        kentässä
        """    
    
        income_output = self.budget.get_income()
        self.budget_display.delete("1.0", tk.END)
        self.budget_display.insert(tk.END,str(income_output))
        income_sum = self.budget.income_sum()
        self.income_display.delete("1.0", tk.END)
        self.income_display.insert(tk.END,str(income_sum))

    def fetch_expense(self):
        """Kutsuu budget.get_expense() ja näyttää menot
        oikeassa kentässä
        """
        expense_output = self.budget.get_expense()
        self.budget_display.delete("1.0", tk.END)
        self.budget_display.insert(tk.END,str(expense_output))
        expense_sum = self.budget.expense_sum()
        self.expense_display.delete("1.0", tk.END)
        self.expense_display.insert(tk.END,str(expense_sum))


    def fetch_budget(self):
        """Apufunktio budjetin hakemiseksi,
        
        palauttaa: budget output
        """
        budget_output = self.budget.get_budget()
        return budget_output


    def print_contents(self, event):
        """Apufunktio tekstikentän sisällön näyttämiseksi
        terminaalissa
        """
        print("Hi. The current entry content is:",
              self.content_expense.get())

    def add_expense(self, event):
        """Lisää kulun tietokantaan ja tyhjentää kentän
        tämän jälkeen
        """
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
        """Lisää tulon tietokantaan ja tyhjentää
        kentän tämän jälkeen
        """
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