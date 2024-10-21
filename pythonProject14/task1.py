# Задание 1. Тестирование класса с использованием pytest
# Напишите класс BankAccount, который управляет балансом счета. Он должен
# поддерживать следующие методы:
# ● deposit(amount): добавляет указанную сумму к балансу.
# ● withdraw(amount): снимает указанную сумму с баланса, если достаточно
# средств.
# ● get_balance(): возвращает текущий баланс счета.
# При попытке снять больше средств, чем доступно на счете, должно
# выбрасываться исключение InsufficientFundsError. Напишите как минимум
# 5 тестов для проверки работы классов и его методов.

class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__("Недостаточно средств на счете.")

class BankAccount:
    def __init__(self, initial_balance = 0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError ('Сумма депозита должна быть положительна')
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError()
        self.balance -= amount

    def get_balance(self):
        return self.balance




        
