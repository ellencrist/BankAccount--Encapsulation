# Bank account

Training encapsulation in Python with a simple program that simulates a bank account, allowing operations such as deposits, withdrawals and balance inquiries.

# Functionalities
__init__(self, holder_name, initial_balance=0.0): Constructor of the BankAccount class. Creates a new bank account instance with a holder name and an optional opening balance.

deposit(self, amount): Makes a deposit into the bank account. The deposit amount must be greater than zero. If the value is valid, the account balance will be updated and a success message will be displayed. Otherwise, an error message will be displayed.

withdraw(self, value): Performs a withdrawal from the bank account. The withdrawal amount cannot be greater than the available balance in the account. If the value is valid, the account balance will be updated and a success message will be displayed. Otherwise, an error message will be displayed.

consult_saldo(self): Displays the current balance of the bank account.

get_name_holder(self): Returns the name of the bank account holder.

set_name_holder(self, new_name): Updates the name of the bank account holder.

# Grades
The default starting balance is zero, but can be specified when creating a new bank account instance.
Deposit and withdrawal operations verify that the amount is valid before updating the balance.
The balance is held as a float value and is displayed with two decimal places when querying the balance.

<p>Used IDE: </p>
     <img src="https://i.ibb.co/VvHCbPg/1-k-Ig3-dwee-DFVGCQBUNWc-Fw.png" height="50" >
