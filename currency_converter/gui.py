"""
Currency Converter GUI
Author: James Nicholson
Date: 04/24/2023
Description: Provide a user-friendly interface for converting currency

"""
import tkinter as tk
from utils import convert_currency

# Replace "YOUR_API_KEY" with your actual API key from Apilayer
API_KEY = "iXoFQv4XxNB5LRwWD3PO8SH55Te5ehQc"

def create_gui(root):
    # ...


import tkinter as tk
from utils import convert_currency

# Replace "YOUR_API_KEY" with your actual API key from Apilayer
API_KEY = "iXoFQv4XxNB5LRwWD3PO8SH55Te5ehQc"

def create_gui(root):
    def update_result():
        # Get the input values from the GUI
        amount = amount_var.get()
        currency_from = from_var.get().upper()
        currency_to = to_var.get().upper()

        # Convert the currency and update the result label
        converted_amount = convert_currency(amount, currency_from, currency_to, API_KEY)
        if converted_amount is not None:
            result_label.config(text=f"{float(amount):.2f} {currency_from} = {converted_amount:.2f} {currency_to}")
        else:
            result_label.config(text="Sorry, something went wrong. Please try again later.")

    # Define function to clear input fields and result label
    def clear_fields():
        amount_var.set("")
        from_var.set("USD")
        to_var.set("EUR")
        result_label.config(text="")

    # Set the title of the window
    root.title("Currency Converter")

    # Create input fields for the amount, "from" currency, and "to" currency
    amount_label = tk.Label(root, text="Amount:")
    amount_label.pack()

    amount_var = tk.StringVar()
    amount_entry = tk.Entry(root, width=20, textvariable=amount_var)
    amount_entry.pack()

    from_label = tk.Label(root, text="From:")
    from_label.pack()

    from_var = tk.StringVar()
    from_var.set("USD")
    from_menu = tk.OptionMenu(root, from_var, "USD", "EUR", "JPY", "GBP", "KRW")
    from_menu.pack()

    to_label = tk.Label(root, text="To:")
    to_label.pack()

    to_var = tk.StringVar()
    to_var.set("EUR")
    to_menu = tk.OptionMenu(root, to_var, "USD", "EUR", "JPY", "GBP", "KRW")
    to_menu.pack()

    # Create button for converting currencies
    convert_button = tk.Button(root, text="Convert", command=lambda: update_result())
    convert_button.pack()

    # Create button for clearing input fields
    clear_button = tk.Button(root, text="Clear", command=lambda: clear_fields())
    clear_button.pack()

    # Create label for displaying the converted amount
    result_label = tk.Label(root, text="")
    result_label.pack()

    # Start the main event loop of the GUI
    root.mainloop()

# Call the create_gui function to start the application
if __name__ == "__main__":
    # Create a Tk object
    root = tk.Tk()

    # Call the create_gui function with the root argument
    create_gui(root)
