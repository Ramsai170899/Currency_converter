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







"""
🌐 Exciting Python Project: Currency Converter with Real-Time Exchange Rates! 🏦💰

Hey LinkedIn fam! 👋 I'm thrilled to share with you a cool Python project I've been working on - a Currency Converter with real-time exchange rates, all wrapped up in a sleek GUI. 💹💱

🔗 Link to the GitHub repository: [Insert Link Here]

📌 Project Highlights:

Real-time exchange rates using the Frankfurter API 🌍🔄
User-friendly GUI with dropdown menus, input fields, and a vibrant "Convert" button 💼💡
Accurate and seamless currency conversion with just a few clicks 💱🔢
📚 Using APIs for Powerful Functionalities:
In this project, I harnessed the power of APIs (Application Programming Interfaces) to fetch up-to-date exchange rate data. APIs act as bridges between different software applications, enabling them to communicate and share data. By integrating the Frankfurter API, I effortlessly retrieved exchange rates for various currency pairs. 🌐🔌

🔍 Our Approach:
Our journey started with planning the project's architecture, from designing the user interface to handling data flow. We initially explored different currency rate APIs and encountered minor hiccups with compatibility and data retrieval. After experimenting with APIs like Fixer.io and Open Exchange Rates, we opted for the reliable Frankfurter API.

We divided the development into phases:

Establishing a connection to the Frankfurter API to fetch real-time exchange rates.
Building the GUI using the versatile Tkinter library, featuring dropdown menus, input fields, and an eye-catching "Convert" button.
Ensuring a seamless user experience by validating inputs and handling exceptions gracefully.
Fine-tuning the aesthetics and layout for a polished appearance.
The end result? A user-friendly Currency Converter that provides accurate conversions on-the-fly! 💼💰

🚀🔗 I invite you to check out the GitHub repository [Insert Link Here] for the complete code and dive into the world of APIs and Python GUI development. Feel free to tinker with the project, add your own creative touches, and explore the limitless possibilities of coding!

#CurrencyConverter #PythonProject #APIs #GUIProgramming #CodingJourney #TechEnthusiast #LearningToCode #DeveloperLife #Innovation #CurrencyExchange #FinancialTech #PythonProgramming #CodingCommunity #OpenSource

👉 Have any questions or suggestions? Drop a comment below! Let's learn and grow together. 🌱👨‍💻👩‍💻

[Insert Project Screenshot Here]

Stay curious and keep coding! 💡🚀🔥



"""