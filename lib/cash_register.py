#!/usr/bin/env python3

class CashRegister:
  
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.prices = []
        self.discount = discount
        self.transaction_counts = []  # Keep track of the quantity for each transaction

    def add_item(self, title, price, quantity=1):
        for i in range(quantity):
            self.items.append(title)
            self.prices.append(price)
            self.total += price
        self.transaction_counts.append(quantity)

    def apply_discount(self):
        if self.discount == 0: 
            print("There is no discount to apply.")
        else:
            discount_price = self.total * (self.discount / 100)
            self.total = round(self.total - discount_price)
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if len(self.items) == 0:
            self.total = 0.0
        else:
            last_transaction_count = self.transaction_counts.pop()
            for _ in range(last_transaction_count):
                self.items.pop()
                self.total -= self.prices.pop()