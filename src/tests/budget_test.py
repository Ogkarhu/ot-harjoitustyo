import unittest
from budget import Budget


#tekoälygeneroitu osa alkaa
class TestBudget(unittest.TestCase):

    def setUp(self):
        self.budget = Budget(":memory:")

    def test_database_starts_empty(self):
        """Testaa että tietokanta on alussa tyhjä
        """
        self.assertEqual(self.budget.get_budget(), [])
    #tekoälygeneroitu osa loppuu

    def test_add_expense(self):
        """Testaa kulun lisäämistä
        """
        self.budget.add_expense(420, "test1", "2025-01-01", False)
        self.assertEqual(self.budget.get_expense(), [420])

    def test_expense_sum(self):
        """Testaa kulujen summaa
        """
        self.budget.add_expense(55, "test2", "2025-01-01", False)
        self.budget.add_expense(45, "test3", "2025-01-01", False)
        self.assertEqual(self.budget.expense_sum(), (100,))

    def test_add_income(self):
        """Testaa tulon lisäämistä
        """
        self.budget.add_income(2000, "test4", "2025-01-01", False)
        self.assertEqual(self.budget.get_income(), [2000])

    def test_monthly_budget(self):
        """Testaa kuukausittaisen budejetin toimimista
        """
        self.budget.add_income(150, "test5", "2025-01-01", False)
        self.budget.add_expense(50, "test6", "2025-01-15", False)

        monthly = self.budget.get_monthly_budget()

        self.assertEqual(monthly["2025-01"]["budget"], 100)

    #tekoälygeneroitu osa alkaa
    def test_income_sum_single(self):
        """Testaa että tulojen summa toimii yhdellä syötteellä
        """
        self.budget.add_income(1000, "test7", "2025-01-01", False)
        self.assertEqual(self.budget.income_sum(), (1000,))

    def test_monthly_budget_ignores_rows_without_date(self):
        """testaa virhettä päivämäärättömästä syötteestä
        """
        # oikeellinen syöte
        self.budget.add_income(1000, "Salary", "2025-01-01", False)

        # virheellinen syöte ilman päivämäärää
        self.budget.cur.execute(
            "INSERT INTO budget (income, expense, date, name, recurring) "
            "VALUES (?, ?, ?, ?, ?)",
            (500, None, None, "Broken income", False)
        )
        self.budget.db.commit()

        monthly = self.budget.get_monthly_budget()

        # Virheellinen syöte ei mene läpi
        self.assertIn("2025-01", monthly)
        self.assertEqual(monthly["2025-01"]["income"], 1000)
        #tekoälygeneroitu osa loppuu
