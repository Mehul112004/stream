import streamlit as st
import requests

# Streamlit app title
st.title("Currency Converter")

# List of currency options
currency_options = ["INR", "USD", "EUR", "GBP", "JPY"]  # Add more currencies as needed

# User input for base currency using a dropdown menu
base_currency = st.selectbox("Select the base currency:", currency_options)

# User input for foreign currencies using dropdown menus
foreign_currency1 = st.selectbox("Select the first foreign currency:", currency_options)
foreign_currency2 = st.selectbox("Select the second foreign currency:", currency_options)

# Function to perform currency conversion
def convert_currency(amount, from_currency, to_currency):
    try:
        # Make an API request to get exchange rates
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        exchange_rate = data["rates"][to_currency]

        # Calculate the converted amount
        converted_amount = amount * exchange_rate
        return converted_amount
    except:
        return "Invalid input or currency not supported."

# User input for amount to convert
amount_to_convert = st.number_input("Enter the amount to convert:", min_value=0.01)

# Convert and display results
if st.button("Convert"):
    if amount_to_convert:
        converted_amount1 = convert_currency(amount_to_convert, base_currency, foreign_currency1)
        converted_amount2 = convert_currency(amount_to_convert, base_currency, foreign_currency2)
        st.write(f"{amount_to_convert} {base_currency} is equal to:")
        st.write(f"{converted_amount1} {foreign_currency1}")
        st.write(f"{converted_amount2} {foreign_currency2}")
    else:
        st.warning("Please enter the amount to convert.")

# Footer
st.text("Exchange rates are based on the data from exchangerate-api.com")
