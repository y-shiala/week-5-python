# Assignment 1

class my_bank:
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance
  
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Deposit ${amount}. New balance: ${self.balance}")
    else:
      print("Deposit amount must be positive.")
  
  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      print(f"withdraw ${amount}. New balance: ${self.balance}")
    else:
      print("Insufficient funds or invalid amount.")
      
  def get_balance(self):
    return self.balance
  
  def show_info(self):
    print(f"Account Owner: {self.owner}, Balance: ${self.balance}")
  
# Subclass with interest
class my_savings(my_bank):
  def __init__(self, owner, balance=0, interest_rate=0.02):
    super().__init__(owner, balance)
    self.interest_rate = interest_rate
    
  # Polymorphism: Overriding show_info
  def show_info(self):
    print(f"[Savings] Owner: {self.owner}, Balance: ${self.get_balance()}, Interest Rate: {self.interest_rate*100}%")
    
  def apply_interest(self):
    interest = self.get_balance() * self.interest_rate
    self.deposit(interest)
    print(f"[{self.owner}] Interest of ${interest:.2f} applied.")  
    
 # Activity 2
 
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def move(self):
        print("Running 🐕")

class Bird(Animal):
    def move(self):
        print("Flying 🐦")

class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

class Snake(Animal):
    def move(self):
        print("Slithering 🐍")

              