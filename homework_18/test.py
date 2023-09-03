import unittest
from unittest.mock import patch

from Bank import Bank, SavingsAccount, CurrentAccount


class TestAccount(unittest.TestCase):
    # Ensure that the account is opened and has balance.
    def test_open_account(self):
        test_bank = Bank()

        test_account = SavingsAccount(200.0, "SAV000", 0.03)
        test_bank.open_account(test_account)

        self.assertIn(
            test_account,
            test_bank.accounts,
            "Account should be opened and saved into the list in the Bank object",
        )

    # Test update method. It should check that code added interest and sent a message (print function was called).
    def test_update_method(self):
        test_bank = Bank()
        test_account = CurrentAccount(100.0, "SAV000", 200)
        test_bank.open_account(test_account)
        test_account.deposit(150)

        with patch("builtins.print") as mock_print:
            test_bank.update_account()

            self.assertTrue(mock_print.called, "Print should be called")


unittest.main()
