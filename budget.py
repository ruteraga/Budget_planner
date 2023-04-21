class Category:

  def __init__(self, category):
    self.ledger = []
    self.amount = 0
    self.category = category

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.amount = self.amount + amount

  def withdraw(self, w_amount, description=""):
    if self.amount > w_amount:
      self.amount = self.amount - w_amount
      self.ledger.append({"amount": -w_amount, "description": description})
      print("Withdraw completed.")
    else:
      print("Withdraw failed.")

  def get_balance(self):
    print("The current amount:", self.amount)

  def transfer(self, t_amount, category):
    if self.amount > t_amount:
      self.amount = self.amount - t_amount
      self.ledger.append({
        "amount": -t_amount,
        "description": "Transfer to " + category.category
      })
      category.deposit(t_amount, "Transfer from " + self.category)
      print("Transfer completed.")
    else:
      print("Transfer failed")

  def check_funds(self, amount):
    if self.amount < amount:
      print("Not enough")
    else:
      print("Enough")

  def Details(self):
    result = ""
    result += "**************" + str(self.category) + "**************" + "\n"

    for transaction in self.ledger:
      amount = 0
      description = ""

      for key, value in transaction.items():
        if key == "amount":
          amount = value
        elif key == "description":
          description = value
      if len(description) > 23:
        description = description[:23]
      amount = str(format(float(amount), '.2f'))
      if len(amount) > 7:
        amount = amount[:7]
      result += description + str(amount).rjust(30 - len(description)) + "\n"
    result += "Total:" + str(format(float(self.amount), '.2f'))
    print(result)
