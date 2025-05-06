# Python OOP Examples: Bank Account System & Animal Polymorphism

This project contains two simple Python programs demonstrating key object-oriented programming (OOP) concepts: **encapsulation**, **inheritance**, and **polymorphism**.

---

## 🏦 Bank Account System

### Description
A basic simulation of a bank account using object-oriented programming. It includes a base class `my_bank` and a subclass `my_savings` that adds interest-handling functionality.

### Features
- Encapsulation of account balance.
- Constructor initialization with unique values.
- Deposit and withdraw operations.
- Inheritance from base to savings account.
- Polymorphism via method overriding (`show_info()`).

### Classes
- **my_bank**: Base class with deposit, withdraw, and balance display.
- **my_savings**: Subclass of `my_bank` with an interest rate and the ability to apply interest.

### Sample Usage
```python
# Creating unique objects
account1 = my_bank("Alice", 500)
account2 = my_savings("Bob", 1000, interest_rate=0.05)

# Using the objects
account1.deposit(200)
account1.withdraw(100)
account1.show_info()

print()

account2.deposit(300)
account2.withdraw(50)
account2.apply_interest()
account2.show_info() 
