import unittest
from budget import Budget


class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget()

    def test_database_created_correctly(self):
        self.assertEqual(self.budget.get_budget(), [
                         (3000, 800), (4500, 1500), (5200, 2000)])
