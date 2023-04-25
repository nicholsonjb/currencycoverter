"""
Currency Converter Application
Author: James Nicholson
Date: 04/24/2023
Description: This application allows users to convert currencies using real-time exchange rates from the Apilayer API.
"""

import tkinter as tk
from gui import create_gui

# Create a Tk object
root = tk.Tk()

# Call the create_gui function with the root argument
create_gui(root)

# Start the main event loop of the GUI
root.mainloop()
