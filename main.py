class Bank_account:
  def __init__(self, owner, start_balance):
    self.balance = start_balance
    self.owner = owner
    
  def __repr__(self):
    return "This is the bank account of %s with %s balance" % (self.owner, self.balance)
    
  def deposit(self, amount):
    self.balance += amount
    return "Your new balance is %s" % self.balance
    
  def withdraw(self, amount):
    if amount > self.balance:
      return "Your balance is not enough"
    self.balance -= amount
    return "Your new balance is %s" % self.balance
    
  def current_balance(self):
    return self.balance
    
account = Bank_account("Nima", 10000)
print(account)
print(account.deposit(100))
print(account.withdraw(50))
print(account.withdraw(12000))
print(account.current_balance())
