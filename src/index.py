import tkinter as tk
import datetime
from tkinter import simpledialog
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


        #Tekstilaatikko kussakin hetkessä kulujen, menojen tai budjetin
        #näyttämiseksi
        self.budget_display = tk.Text(self, width=70,height=30)
        self.budget_display.pack()

        self.budget_display.insert(tk.END,str(self.fetch_budget()))
        #income-nappi
        self.income_button = tk.Button(self, text="Show income",command=self.fetch_income)
        self.income_button.pack()
        #näyttö tulojen summalle
        self.income_display = tk.Label(self, width=10, anchor="w")
        self.income_display.pack()
        #expense-nappi
        self.expense_button = tk.Button(self, text="Show expenses",command=self.fetch_expense)
        self.expense_button.pack()
        #näyttö menojen summalle
        self.expense_display = tk.Label(self, width=10, anchor="w")
        self.expense_display.pack()
        

        

        """Nappi kulun lisäämiseksi
        """
        self.add_expense_button =tk.Button(self,text="Add expense", 
            command=self.open_expense_dialog)
        self.add_expense_button.pack()

        """Nappi tulon lisäämiseksi
        """
        
        self.add_income_button =tk.Button(self,text="Add income",
            command=self.open_income_dialog)
        self.add_income_button.pack()

        """kaikkien syötteiden näyttämisnappi
        """
        self.show_entries_button = tk.Button(self, text="Show all entries", command=self.show_all_entries)
        self.show_entries_button.pack()

        """kuukausibudjetin näyttämisnappi
        """
        self.monthly_button = tk.Button(self, text="Show monthly budget", command=self.fetch_monthly_budget)
        self.monthly_button.pack()
        
        #tekoälygeneroitu osa alkaa
        self.delete_button = tk.Button(self, text="Delete entry", command=self.open_delete_dialog)
        self.delete_button.pack()


        
        


    def open_delete_dialog(self):
            id = simpledialog.askinteger("Delete income/expense", "enter ID:")
            if id is not None:
                self.budget.delete_entry(id)
                self.budget_display.delete("1.0", tk.END)
                self.budget_display.insert(tk.END, str(self.fetch_budget()))


    #osittain tekoälygeneroitu osa alkaa
    def open_expense_dialog(self):
        dialog = Expense_Dialog(self)
        if dialog.result:
            try:
                amount = int(dialog.result["amount"])
            except ValueError:
                print("Amount must be a number!")
                return
        
        name = dialog.result["name"]
        date = dialog.result["date"]
        recurring = dialog.result["recurring"]

        self.budget.add_expense(amount, name, date, recurring)
        print("Expense added:", dialog.result)

        # budjettinäytön päivitys
        self.budget_display.delete("1.0", tk.END)
        self.budget_display.insert(tk.END, str(self.fetch_budget()))
    #osittain tekoälygeneroitu osa loppuu

    def open_income_dialog(self):
        dialog = Income_Dialog(self)
        if dialog.result:
            try:
                amount = int(dialog.result["amount"])
            except ValueError:
                print("Amount must be a number!")
                return
        name = dialog.result["name"]
        date = dialog.result["date"]
        recurring = dialog.result["recurring"]

        self.budget.add_income(amount, name, date, recurring)
        print("Income added", dialog.result)

        # budjettinäytön päivitys
        self.budget_display.delete("1.0", tk.END)
        self.budget_display.insert(tk.END, str(self.fetch_budget()))
    
    def fetch_income(self):
        """Kutsuu budget.get_income() ja näyttää tulot oikeassa
        kentässä
        """    
    
        income_output = self.budget.get_income()
        self.budget_display.delete("1.0", tk.END)
        for income in income_output:
            self.budget_display.insert(tk.END, f"{income}\n")
        income_sum = self.budget.income_sum()
        self.income_display.config(text=str(income_sum))


    def fetch_expense(self):
        """Kutsuu budget.get_expense() ja näyttää menot
        oikeassa kentässä
        """
        expense_output = self.budget.get_expense()
        self.budget_display.delete("1.0", tk.END)
        for expense in expense_output:
            self.budget_display.insert(tk.END,f"{expense}\n")
        expense_sum = self.budget.expense_sum()
        self.expense_display.config(text=str(expense_sum))



    def fetch_budget(self):
        """Apufunktio budjetin hakemiseksi,
        
        palauttaa: budget output
        """
        budget_output = self.budget.get_budget()
        self.budget_display.delete("1.0", tk.END)
        for row in budget_output:
            id, income, expense, name, date, recurring = row
            self.budget_display.insert(
                tk.END,
                f"ID:{id} | Income:{income} | Expense:{expense} | Name:{name} | Date:{date} | Recurring:{recurring}\n"
        )
        return budget_output
        


    def print_contents(self, event):
        """Apufunktio tekstikentän sisällön näyttämiseksi
        terminaalissa
        """
        print("Hi. The current entry content is:",
              self.content_expense.get())

    def fetch_monthly_budget(self):
        #osittain tekoälygeneroitu osa alkaa
        data = self.budget.get_monthly_budget()

        self.budget_display.delete("1.0", tk.END)

        for month in sorted(data.keys()):
            inc = data[month]["income"]
            exp = data[month]["expense"]
            bud = data[month]["budget"]
    
            self.budget_display.insert(
                tk.END,
                f"{month}\n  Income: {inc}\n  Expense: {exp}\n  Budget: {bud}\n\n"
            )
    
    def show_all_entries(self):
        """Näyttää kaikki yksittäiset tulot ja menot tekstikentässä id:n kanssa
        """
        data = self.budget.get_budget()
        self.budget_display.delete("1.0", tk.END)
        for row in data:
            id, income, expense, date, name, recurring = row
            self.budget_display.insert(
                tk.END,
                f"ID:{id} | Name:{name} | Date:{date} | Income:{income} | Expense:{expense} | Recurring:{recurring}\n"
            )




class Expense_Dialog(simpledialog.Dialog):
    def body(self,master):
        #tekoälygeneroitu osa alkaa
        tk.Label(master, text="Amount:").grid(row=0, column=0, sticky="w")
        tk.Label(master, text="Name:").grid(row=1, column=0, sticky="w")
        tk.Label(master, text="Date (YYYY-MM-DD):").grid(row=2, column=0, sticky="w")
        tk.Label(master, text="Recurring?").grid(row=3, column=0, sticky="w")
        #tekoälygeneroitu osa loppuu

        self.amount_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.rec_var = tk.BooleanVar()

        self.date_var.set(datetime.datetime.now().strftime("%Y-%m-%d"))


        #tekoälygeneroitu osa alkaa
        tk.Entry(master, textvariable=self.amount_var).grid(row=0, column=1)
        tk.Entry(master, textvariable=self.name_var).grid(row=1, column=1)
        tk.Entry(master, textvariable=self.date_var).grid(row=2, column=1)
        tk.Checkbutton(master, variable=self.rec_var).grid(row=3, column=1)
        #tekoälygeneroitu osa loppuu

        return master

    def apply(self):
        self.result = {
            "amount":self.amount_var.get(),
            "name":self.name_var.get(),
            "date":self.date_var.get(),
            "recurring":self.rec_var.get()
        }

class Income_Dialog(simpledialog.Dialog):
    def body(self,master):
        tk.Label(master, text="Amount:").grid(row=0, column=0, sticky="w")
        tk.Label(master, text="Name:").grid(row=1, column=0, sticky="w")
        tk.Label(master, text="Date (YYYY-MM-DD):").grid(row=2, column=0, sticky="w")
        tk.Label(master, text="Recurring?").grid(row=3, column=0, sticky="w")

        self.amount_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.rec_var = tk.BooleanVar()

        self.date_var.set(datetime.datetime.now().strftime("%Y-%m-%d"))


        tk.Entry(master, textvariable=self.amount_var).grid(row=0, column=1)
        tk.Entry(master, textvariable=self.name_var).grid(row=1, column=1)
        tk.Entry(master, textvariable=self.date_var).grid(row=2, column=1)
        tk.Checkbutton(master, variable=self.rec_var).grid(row=3, column=1)

    def apply(self):
        self.result = {
            "amount":self.amount_var.get(),
            "name":self.name_var.get(),
            "date":self.date_var.get(),
            "recurring":self.rec_var.get()
        }

root = tk.Tk()
myapp = App(root)
myapp.mainloop()