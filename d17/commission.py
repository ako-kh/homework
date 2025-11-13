
def commission(func):
    def wrapper(balance, pay_n):
        pay_n += 1
        if pay_n > balance:
            return "not enough money"
        return func(balance, pay_n)
    return wrapper

@commission
def pay(balance, pay_n):
    return balance - pay_n

print(pay(pay_n=3, balance=3))
print(pay(3, 2))