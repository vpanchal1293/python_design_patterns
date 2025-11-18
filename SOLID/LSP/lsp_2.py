class Account:
    def withdraw(self, amount):
        print(f"Withdrawing {amount} from account")

class FixedDepositAccount(Account):
    def withdraw(self, amount):
        raise Exception("Withdrawal not allowed!")  # ❌ violates contract
