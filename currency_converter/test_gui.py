import tkinter as tk
from gui import create_gui

def test_create_gui():
    # Create a Tk object
    root = tk.Tk()

    # Call the create_gui function with the root argument
    create_gui(root)

    # Get the label text and check if it matches the expected value
    result_label = root.children["!label3"]
    assert result_label.cget("text") == ""

    # Get the amount entry field and set its value to 100
    amount_entry = root.children["!entry"]
    amount_entry.delete(0, tk.END)
    amount_entry.insert(0, "100")

    # Get the "from" currency menu and set its value to "EUR"
    from_menu = root.children["!optionmenu"]
    from_menu.children["!menu"].entryconfig("EUR", state="normal")
    from_menu.children["!menu"].entryconfig("USD", state="disabled")
    from_menu.children["!menu"].invoke("EUR")

    # Get the "to" currency menu and set its value to "JPY"
    to_menu = root.children["!optionmenu2"]
    to_menu.children["!menu"].entryconfig("JPY", state="normal")
    to_menu.children["!menu"].entryconfig("USD", state="disabled")
    to_menu.children["!menu"].invoke("JPY")

    # Click the "Convert" button
    convert_button = root.children["!button"]
    convert_button.invoke()

    # Get the label text and check if it matches the expected value
    assert result_label.cget("text") == "100.00 EUR = 12304.50 JPY"
    
    # Get the "from" currency menu and set its value to "JPY"
    from_menu.children["!menu"].entryconfig("JPY", state="normal")
    from_menu.children["!menu"].entryconfig("USD", state="disabled")
    from_menu.children["!menu"].invoke("JPY")

    # Get the "to" currency menu and set its value to "EUR"
    to_menu.children["!menu"].entryconfig("EUR", state="normal")
    to_menu.children["!menu"].entryconfig("USD", state="disabled")
    to_menu.children["!menu"].invoke("EUR")

    # Click the "Convert" button
    convert_button.invoke()

    # Get the label text and check if it matches the expected value
    assert result_label.cget("text") == "100.00 JPY = 0.77 EUR"

    # Click the "Clear" button
    clear_button = root.children["!button2"]
    clear_button.invoke()

    # Get the label text and check if it matches the expected value
    assert result_label.cget("text") == ""
