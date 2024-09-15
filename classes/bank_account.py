from datetime import datetime


class BankAccount:
    monthly_interest = 0.10
    vip_minimum = 1_000_000

    def __init__(self, owner, balance=0, vip=False):
        self.owner = owner # public
        self._balance = balance # protected
        self.__vip = vip # private

    @property
    def vip(self):
        return self.__vip

    @vip.setter
    def vip(self, value):
        if self._balance >= BankAccount.vip_minimum:
            self.__vip = value


    def __str__(self):
        return f'owner: {self.owner}, balance: {self._balance}, vip: {self.__vip}'

    def __repr__(self):
        return f'{self.owner}:{self._balance}'

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self._balance + other._balance




    # def __repr__(self):



    def deposit(self, amount):
        self._balance += amount
        return f'Deposited {amount}. new balance: {self._balance}'

    def withdraw(self, amount):
        if amount > self._balance:
            return "Not enough money"
        self._balance -= amount
        return f'Withdrew {amount}. new balance: {self._balance}'

    def get_bonus(self):
        if datetime.now().date().strftime("%d") in ['28', '29', '30', '31']:
            return self._balance * BankAccount.monthly_interest

    @classmethod
    def change_monthly_interest(cls, new_interest):
        cls.monthly_interest = new_interest

    @staticmethod
    def papers_200(money):
        return money // 200








if __name__ == '__main__':
    account1 = BankAccount('Pahshish', -100)
    account2 = BankAccount('Zohar')
    account3 = BankAccount('Zohar', vip=True)
    account4= BankAccount('Zohar', balance=400, vip=True)
    account5 = BankAccount('Zohar', vip=True, balance=500)
    # account10 = BankAccount(vip=True, _balance=500)
    print(account1._balance)
    print(account1.owner)
    print(account1.withdraw(1300))
    print(account2.deposit(100))
    account5.get_bonus()

    BankAccount.change_monthly_interest(0.15)
    # in python we can access public and protected

    print(account1.owner)
    print(account1._balance)
    # print(account1.__vip)


    account21 = BankAccount('Zohar', 400, False)
    print(account21)
    account1 = BankAccount('Pahshish', -100)
    print(account1 + account21)
    print([account1, account21])
    print(account1.vip)
    account1.vip = True
    print(account1.vip)


