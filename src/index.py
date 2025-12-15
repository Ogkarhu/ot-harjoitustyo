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
        self.budget_display = tk.Text(self, width=80,height=30)
        self.budget_display.pack()

        self.fetch_monthly_budget()

        #Kulujen ja menojen lisäämiset
        entries_frame = tk.LabelFrame(self)
        entries_frame.pack(fill="x", padx=2,pady=2)

        tk.Button(entries_frame, text="Add income",
            command=self.open_income_dialog).pack(side="left", padx=3)

        tk.Button(entries_frame, text="Add expense",
            command=self.open_expense_dialog).pack(side="right", padx=3)
        #Tekstilaatikko päättyy

        #Nappi yksittäisen lisäyksen poistamiseksi
        #tekoälygeneroitu osa alkaa
        self.delete_button = tk.Button(self, text="Delete entry", command=self.open_delete_dialog)
        self.delete_button.pack()
        #tekoälygeneroitu osa loppuu

        #Tekstilaatikko yksittäisten tulojen ja menojen näyttämiseksi
        report_frame = tk.LabelFrame(self, text="Budget")
        report_frame.pack(fill="x", padx=3, pady=3)

        #Nappi joka näyttää kaikki tietokannan rivit
        tk.Button(report_frame, text="Show all entries",
                  command=self.show_all_entries).pack(side="left", padx=5)

        #Nappi joka näyttää tulot listana
        tk.Button(report_frame, text="Show income",
                  command=self.fetch_income).pack(side="left", padx=5)

        #Nappi joka näyttää menot listana
        tk.Button(report_frame, text="Show expenses",
                  command=self.fetch_expense).pack(side="left", padx=5)

        #Nappi joka näyttää koko budjetin listana
        tk.Button(report_frame, text="Monthly budget",
                  command=self.fetch_monthly_budget).pack(side="left", padx=5)    
        #Tekstilaatikko päättyy


    def open_delete_dialog(self):
        """Avaa ikkunan syötteen poistamiseksi
        """
        id_num = simpledialog.askinteger("Delete income/expense", "enter ID:")
        if id_num is not None:
            self.budget.delete_entry(id_num)
            self.budget_display.delete("1.0", tk.END)
            self.fetch_budget()


    #osittain tekoälygeneroitu osa alkaa
    def open_expense_dialog(self):
        """Avaa ikkunan kulun lisäämiseksi
        """
        dialog = ExpenseDialog(self)
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
        self.fetch_budget()
    #osittain tekoälygeneroitu osa loppuu

    def open_income_dialog(self):
        """Avaa ikkunan tulon lisäämiseksi
        """
        dialog = IncomeDialog(self)
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
        self.fetch_budget()

    def fetch_income(self):
        """Kutsuu budget.get_income() ja näyttää tulot oikeassa
        kentässä
        """

        income_output = self.budget.get_income()
        self.budget_display.delete("1.0", tk.END)
        for income in income_output:
            self.budget_display.insert(tk.END, f"{income}\n")



    def fetch_expense(self):
        """Kutsuu budget.get_expense() ja näyttää menot
        oikeassa kentässä
        """
        expense_output = self.budget.get_expense()
        self.budget_display.delete("1.0", tk.END)
        for expense in expense_output:
            self.budget_display.insert(tk.END,f"{expense}\n")




    def fetch_budget(self):
        """Apufunktio budjetin hakemiseksi,
        
        palauttaa: budget output
        """
        self.show_all_entries()



    def fetch_monthly_budget(self):
        """Hakee kuukausibudjetin ja muotoilee sen tekstikenttään
        """
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




class ExpenseDialog(simpledialog.Dialog):
    """Luokka joka luo valintaruudun kulun lisäämiseksi
    """
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

class IncomeDialog(simpledialog.Dialog):
    """Luokka joka luo valintaruudun tulon lisäämiseksi
    """
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
