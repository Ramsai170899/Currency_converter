import httpx
from tkinter import *

def get_exchange_rate(from_curr, to_curr):
    base_url = f"https://api.frankfurter.app/latest?from={from_curr}&to={to_curr}"

    try:
        with httpx.Client() as client:
            response = client.get(base_url)
        data = response.json()
        return data["rates"][to_curr]
    except:
        return None

def convert_currency():
    from_curr = from_currency.get().upper()
    to_curr = to_currency.get().upper()
    amt = float(amount.get())

    exchange_rate = get_exchange_rate(from_curr, to_curr)
    if exchange_rate is None:
        result.config(state='normal')
        result.delete(0, END)
        result.insert(0, "Error")
        result.config(state='readonly')
        return

    converted_amount = round(amt * exchange_rate, 2)
    result.config(state='normal')
    result.delete(0, END)
    result.insert(0, converted_amount)
    result.config(state='readonly')

# Create a tkinter window
window = Tk()
window.title("Currency Converter")
window.geometry("350x330")

# Create labels
from_label = Label(window, text="From Currency:")
to_label = Label(window, text="To Currency:")
amount_label = Label(window, text="Amount:")
result_label = Label(window, text=" ")

# Create dropdown menus with full width
from_currency = StringVar()
from_currency.set("USD")  # Set default value
from_currency_dropdown = OptionMenu(window, from_currency, "USD", "EUR", "JPY", "GBP", "INR", "AUD", "CAD", "SGD", "CHF", "CNY")

to_currency = StringVar()
to_currency.set("EUR")  # Set default value
to_currency_dropdown = OptionMenu(window, to_currency, "USD", "EUR", "JPY", "GBP", "INR", "AUD", "CAD", "SGD", "CHF", "CNY")

# Create input fields
amount = Entry(window, font=("Helvetica", 12))  # Customize font size
result = Entry(window, state='readonly', font=("Helvetica", 12, "bold"), justify="center")  # Customize result font

# Create a Convert button with default style
convert_button = Button(window, text="Convert", command=convert_currency, font=("Helvetica", 14, "bold"))

# Place widgets on the window with padding
from_label.grid(row=0, column=0, padx=10, pady=10)
from_currency_dropdown.grid(row=0, column=1, columnspan=2, sticky="ew", padx=10, pady=10)  # Span two columns and use full width
to_label.grid(row=1, column=0, padx=10, pady=10)
to_currency_dropdown.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=10)  # Span two columns and use full width
amount_label.grid(row=2, column=0, padx=10, pady=10)
amount.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=10)  # Span two columns and use full width
convert_button.grid(row=3, column=0, columnspan=3, padx=10, pady=20)  # Span three columns
result_label.grid(row=4, column=0, padx=10, pady=10)
result.grid(row=5, column=0, columnspan=3, padx=10, pady=10)  # Span three columns

# Start the tkinter event loop
window.mainloop()
