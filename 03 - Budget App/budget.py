import math

class Category:

    def __init__(self, name) -> None:
        self.name = name
        self.deposits = 0
        self.expenses = 0
        self.ledger = list()

    def deposit(self, amount, description=""):
        '''Accepts an amount and a description.'''
        self.ledger.append({"amount": amount, "description": description})
        self.deposits = self.deposits + amount

    def withdraw(self, amount, description=""):
        '''Allows you to make a withdraw if the amount is smaller than the balance.'''
        if self.check_funds(amount=amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.expenses = self.expenses + amount
            return True
        else:
            return False

    def transfer(self, amount, transfer_category):
        '''Allows you to transfer funds to another category'''
        if self.check_funds(amount=amount):
            self.ledger.append({"amount":-amount, "description": f"Transfer to {transfer_category.name}"})
            self.expenses = self.expenses + amount
            transfer_category.ledger.append({"amount":amount, "description": f"Transfer from {self.name}"})
            transfer_category.deposits = transfer_category.deposits + amount
            return True
        else:
            return False

    def get_balance(self):
        '''Returns the current balance.'''
        return self.deposits - self.expenses

    def check_funds(self, amount):
        '''Checks to see if the amount of money is available in the balance.'''
        if amount <= (self.deposits - self.expenses):
            return True
        else:
            return False

    def __str__(self):
        space = 30
        transactions = ""
        title = "*" * int((space - len(self.name))/2) + self.name + "*" * int((space - len(self.name))/2) + "\n"
        for transaction in self.ledger:
            i = 0
            for letter in transaction["description"]:
                if i < 23:
                    transactions += letter
                    i += 1
            transactions += " " * (30 - i - len(str('{:.2f}'.format(transaction["amount"])))) + str('{:.2f}'.format(transaction["amount"]))
            transactions += "\n"

        total = f"Total: {self.deposits - self.expenses}"

        return title + transactions + total

def create_spend_chart(categories):

    percentages = list()
    expenses = list()
    total_expenses = 0
    categories_names = list()
    max_lenght = 0
    graph_string = "Percentage spent by category\n"

    for category in categories:
        categories_names.append(category.name)
        if len(category.name) > max_lenght:
            max_lenght = len(category.name)
        total_expenses = total_expenses + category.expenses
        expenses.append(category.expenses)

    for expense in expenses:
        tmp = math.floor((expense * 100) / total_expenses)
        percentages.append(tmp)

    for i in range(11):
        graph_string += " " * (3-len(str(100 - 10 * i)))
        graph_string += str(100 - 10 * i) + "| "
        for value in percentages:
            if  (100 - 10 * i) <= value:
                graph_string += "o  "
            else:
                graph_string += "   "
        graph_string += "\n"

    graph_string += "    "
    for _ in range(7 + len(percentages)):
        graph_string += "-"
    graph_string += "\n"
    for i in range(max_lenght):
        graph_string += "     "
        for category in categories_names:
            if i < len(category):
                graph_string += category[i] + "  "
            else: 
                graph_string += "   "
        if i != max_lenght - 1:
            graph_string += "\n"

    return graph_string