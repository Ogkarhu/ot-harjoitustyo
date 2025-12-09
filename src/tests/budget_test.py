import unittest
from budget import Budget


class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget()

    def test_database_created_correctly(self):
        """Testaa luodaanko tietokanta onnistuneesti
        """
        self.assertEqual(self.budget.get_budget(), [(None,1000)])

    def test_add_expense(self):
        """Testaa onnistuuko kulun luominen
        """
        self.budget.add_expense(1000)
        self.assertEqual(self.budget.expense_sum(),[(1000,)])