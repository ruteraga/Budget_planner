import budget as b

food = b.Category("Food")
food.deposit(500, "First Deposit")
food.withdraw(14.49, "Burger")
food.withdraw(21.99, "Kebab")
food.get_balance()
food.Details()
print("\n")
transport = b.Category("Transport")
transport.deposit(100, "First Deposit")
transport.withdraw(1.70, "Bus Ticket")
transport.transfer(20, food)
transport.Details()

print("\n")
food.Details()
