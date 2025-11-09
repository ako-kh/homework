class BankAccount:
    bank_name = ""
    _total_accounts = 0

    def __init__(self, owner: str, balance: float,):
        self._owner = owner

        if not self.validate_amount(balance):
            print(f"invalid amount {balance}")
            raise ValueError(f"Invalid amount {balance}")
        self._balance = balance

        n = 10000 + self._total_accounts + 1
        self._account_number = f"AN{str(n)[1:]}"
        BankAccount._total_accounts += 1


    def deposit(self, amount):
        if not self.validate_amount(amount):
            print(f"invalid deposit {amount}")
            return
        self._balance += amount


    def withdraw(self, amount):
        if not self.validate_amount(amount):
            print(f"withdraw amount {amount} is invalid")
            return
        elif amount > self._balance:
            print(f"you can not withdraw more than {self.check_balance()}$")
            return
        self._balance -= amount


    def check_balance(self):
        return self._balance


    def get_account_number(self):
        return self._account_number


    def change_owner(self,new_owner):
        self._owner = new_owner


    @classmethod
    def get_total_accounts(cls):
        return cls._total_accounts


    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            return False
        return True
