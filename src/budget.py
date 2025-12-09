import sqlite3


class Budget:
    """Luokka, jonka avulla tehdään hakuja budjetti-tietokantaan
    """
    def __init__(self,db_path="budget.db"):
        """Luokan konstruktori joka luo uuden budjetti-tietokannan
        """
        self.db = sqlite3.connect(db_path)
        print(self.db)
        self.cur = self.db.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS budget(income INTEGER,expense INTEGER)")
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

    def add_expense(self, amount):
        """Lisää yksittäisen kulun budjettiin
        """
        self.cur.execute(
            "INSERT INTO budget (income, expense) VALUES (?, ?)",
            (None, amount)
        )
        self.db.commit()

    def add_income(self, amount):
        """Lisää yksittäisen tulon budjettiin
        """
        self.cur.execute(
            "INSERT INTO budget (income, expense) VALUES (?, ?)",
            (amount, None)
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
        