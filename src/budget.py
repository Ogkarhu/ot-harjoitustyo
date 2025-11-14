import sqlite3


class Budget:
    def __init__(self):
        self.db = sqlite3.connect(":memory:")#vaihda oikeaan kun tallennetaan esim. connect(budget)
        self.cur = self.db.cursor()
        self.cur.execute("CREATE TABLE budget(income,expense)")
        self.cur.execute("""
            INSERT INTO budget (income, expense)
            VALUES
                (3000, 800),
                (4500, 1500),
                (5200, 2000)
        """)

    def get_budget(self):
        self.cur.execute("SELECT * FROM budget")
        return self.cur.fetchall()