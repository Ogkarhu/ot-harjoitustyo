import sqlite3


class Budget:
    def __init__(self,db_path="budget.db"):

        self.db = sqlite3.connect(db_path)
        print(self.db)
        self.cur = self.db.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS budget(income INTEGER,expense INTEGER)")
        # self.cur.execute("""
        #     INSERT INTO budget (income, expense)
        #     VALUES
        #         (3000, 800),
        #         (4500, 1500),
        #         (5200, 2000)
        # """)
        self.db.commit()

    def get_budget(self):
        self.cur.execute("SELECT * FROM budget")
        return self.cur.fetchall()

    #def get

    def add_expense(self, amount):
        self.cur.execute(
            "INSERT INTO budget (income, expense) VALUES (?, ?)",
            (None, amount)
        )
        self.db.commit()

    def add_income(self, amount):
        self.cur.execute(
            "INSERT INTO budget (income, expense) VALUES (?, ?)",
            (amount, None)
        )
        self.db.commit()