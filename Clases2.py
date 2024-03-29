class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def check_budget(self, budget):
        if not isinstance(budget, (int, float)):
            raise TypeError("The budget must be a number")
            exit()
        if budget <= 0:
            raise ValueError("You dont have enough money")
            exit()

    def get_change(self, budget):
        return budget - self.price

    def sell(self, budget):
        self.check_budget(budget)
        if budget >= self.price:
            print(f"You can buy {self.name}")
            if budget == self.price:
                print("You have no change")
            else:
                print(f"Your change is {self.get_change(budget)}")

            exit("Thanks")


small = Coffee("Small", 2)
regular = Coffee("Regular", 5)
big = Coffee("Big", 6)

try:
    user_budget = float(input("What is your budget? "))
except ValueError:
    exit("Please enter a number")

for coffee in [big, regular, small]:
    coffee.sell(user_budget)
