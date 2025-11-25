import unittest
from budget import Budget


class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget()

    def test_database_created_correctly(self):
        self.assertEqual(self.budget.get_budget(), [])
