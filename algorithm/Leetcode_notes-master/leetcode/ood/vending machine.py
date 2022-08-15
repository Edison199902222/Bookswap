from abc import ABC
from enum import Enum


class coin:
    def __init__(self, value):
        self.value = value

class Five_cent(coin):
    def __init__(self, v = 0.05):
        coin.__init__(self, v)

class Ten_cent(coin):
    def __init__(self,  v = 0.1):
        coin.__init__(self, v)

class Quarter(coin):
    def __init__(self, v = 0.25):
        coin.__init__(self, v)

class one_dollar(coin):
    def __init__(self, v = 1):
        coin.__init__(self, v)

class two_dollar(coin):
    def __init__(self, v = 2):
        coin.__init__(self, v)

class Item(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

class ITEMS(Enum):
    PEPSI = 1
    COKE = 2
    SODA = 3

class Coke(Item):
    def __init__(self):
        super(Coke, self).__init__(ITEMS.COKE, 1)

class Pepsi(Item):
    def __init__(self):
        super(Pepsi, self).__init__(ITEMS.PEPSI, 1.25)

class Soda(Item):
    def __init__(self):
        super(Soda, self).__init__(ITEMS.SODA, 2.25)

class Vending_machine:
    def __init__(self):
        self.item = {}
        self.cash = {}
        self.balance = []
        self.current_item = None

    def add_item(self, item, n):
        self.item[item] += n

    def initialize_cash(self, coin, n):
        item = [Five_cent(), Ten_cent(), Quarter(), one_dollar(), two_dollar()]
        for i in item:
            self.cash[i] = n

    def get_balance(self):
        return sum(self.balance)

    def insert_cash(self, coin):
        self.balance.append(coin.value)
        self.cash[coin] += 1

    def is_balance_enough(self):
        return self.get_balance() >= self.current_item.get_price()

    def is_item_enough(self, item):
        return self.item[item] >= 1

    def get_change(self, val):
        cash = [Five_cent(), Ten_cent(), Quarter(), one_dollar(), two_dollar()]
        cash.reverse()
        change = []
        for coin in cash:
            while val > 0:
                    if val >= coin.value and self.cash[coin] >= 1:
                        change.append(coin)
                        val -= coin.value
                    else:
                        break
        if val == 0:
            flag = True
        else:
            flag = False
        return flag, change

    def selectItemAndGetPrice(self, item):
        if self.is_item_enough(item):
            self.current_item = item
            return self.current_item.get_price()
        else:
            return "Sold out"

    def clear_balance(self):
        for coin in self.balance:
            self.cash[coin] += 1
        self.balance = []

    def collectItemAndChange(self):
        if self.is_balance_enough():
            price = self.current_item.get_price()
            balance = self.get_balance()
            flag, change = self.get_change(balance - price)
            if flag:
                self.item[self.current_item] -= 1
                self.change_out(change)
                self.clear_balance()
                return [self.current_item, change]
            else:
                return "Not Sufficient change "
        else:
            return "Price not full paid "

    def change_out(self, change):
        for coin in change:
            self.cash[coin] -= 1








