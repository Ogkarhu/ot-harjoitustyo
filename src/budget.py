import sqlite3
from collections import defaultdict
from datetime import datetime

class Budget:
    """Luokka, jonka avulla tehdään hakuja budjetti-tietokantaan
    """
    def __init__(self,db_path="budget.db"):
        """Luokan konstruktori joka luo uuden budjetti-tietokannan
        """
        self.db = sqlite3.connect(db_path)
        print(self.db)
        self.cur = self.db.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS budget(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                income INTEGER,
                expense INTEGER,
                date DATE,
                name TEXT,
                recurring BOOLEAN
            )
            """)
        self.db.commit()

    def get_budget(self):
        """Hakee ja palauttaa koko budjetin 
        """
        self.cur.execute("SELECT * FROM budget")
        return self.cur.fetchall()

    def get_income(self):
        """Hakee ja palauttaa kaikki tulot budjetista
        """
        self.cur.execute("SELECT income FROM budget WHERE income IS NOT NULL")
        return [row[0] for row in self.cur.fetchall()]

    def get_expense(self):
        """Hakee ja palauttaa kaikki kustannukset budjetista
        """
        self.cur.execute("SELECT expense FROM budget WHERE expense IS NOT NULL")
        return [row[0] for row in self.cur.fetchall()]

    def add_expense(self, amount, name, date, recurring):
        """Lisää yksittäisen kulun budjettiin
        """
        self.cur.execute(
            "INSERT INTO budget (income, expense, name, date, recurring) VALUES (?, ?, ?, ?, ?)",
            (None, amount, name, date, recurring)
        )
        self.db.commit()

    def add_income(self, amount, name, date, recurring):
        """Lisää yksittäisen tulon budjettiin
        """
        self.cur.execute(
            "INSERT INTO budget (income, expense, name, date, recurring) VALUES (?, ?, ?, ?, ?)",
            (amount, None, name, date, recurring)
        )
        self.db.commit()


    def expense_sum(self):
        """Hakee ja palauttaa kulujen tulon
        """
        self.cur.execute(
            "SELECT SUM(expense) FROM budget"
        )
        return self.cur.fetchone()
        

    def income_sum(self):
        """Hakee ja palauttaa tulojen tulon
        """
        self.cur.execute(
            "SELECT SUM(income) FROM budget"
        )
        return self.cur.fetchone()

    #tekoälygeneroitu osa alkaa
    def get_monthly_budget(self):
        monthly = defaultdict(lambda: {"income": 0, "expense": 0})

        # Hae kaikki rivit, joissa on joko tulo tai meno
        self.cur.execute("SELECT income, expense, date FROM budget")
        rows = self.cur.fetchall()

        for income, expense, date in rows:
            if date is None:
                continue

            # Muoto: "YYYY-MM-DD" -> "YYYY-MM"
            month = date[:7]

            if income is not None:
                monthly[month]["income"] += income
            if expense is not None:
                monthly[month]["expense"] += expense

        # laske kuukausibudjetti
        for month in monthly:
            monthly[month]["budget"] = (
                monthly[month]["income"] - monthly[month]["expense"]
            )

        return monthly
    #tekoälygeneroitu osa loppuu

    def delete_entry(self, id):
        self.cur.execute("DELETE FROM budget WHERE id = ?", (id,))
        self.db.commit()

        