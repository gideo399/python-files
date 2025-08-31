import tkinter as tk
from tkinter import messagebox

class BankingApp:
    def __init__(self, root):
        self.balance = 0.0
        self.root = root
        self.root.title("Simple Banking System")
        self.root.geometry("400x300")

        # Balance display
        self.balance_label = tk.Label(root, text="Balance: $0.00", font=("Arial", 16))
        self.balance_label.pack(pady=10)

        # Amount entry
        self.amount_entry = tk.Entry(root, font=("Arial", 14))
        self.amount_entry.pack(pady=10)

        # Buttons
        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit, width=20)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw, width=20)
        self.withdraw_button.pack(pady=5)

        self.show_button = tk.Button(root, text="Show Balance", command=self.show_balance, width=20)
        self.show_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit, width=20)
        self.exit_button.pack(pady=5)

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount > 0:
                
                self.balance += amount
                self.show_balance()
                messagebox.showinfo("Success", "Deposit successful!")
            else:
                messagebox.showwarning("Invalid", "Enter a positive amount!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showwarning("Invalid", "Enter a positive amount!")
            elif amount > self.balance:
                messagebox.showwarning("Insufficient Funds", "Not enough balance!")
            else:
                self.balance -= amount
                self.show_balance()
                messagebox.showinfo("Success", "Withdrawal successful!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

    def show_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()



