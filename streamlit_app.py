import streamlit as st
import requests

# Streamlit app title
st.title("Currency Converter")

# Default base currency as Indian Rupees (INR)
base_currency = "INR"

# User input for foreign currencies
foreign_currency1 = st.text_input("Enter the first foreign currency (e.g., USD):")
foreign_currency2 = st.text_input("Enter the second foreign currency (e.g., EUR):")

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
    if foreign_currency1 and foreign_currency2 and amount_to_convert:
        converted_amount1 = convert_currency(amount_to_convert, base_currency, foreign_currency1)
        converted_amount2 = convert_currency(amount_to_convert, base_currency, foreign_currency2)
        st.write(f"{amount_to_convert} {base_currency} is equal to:")
        st.write(f"{converted_amount1} {foreign_currency1}")
        st.write(f"{converted_amount2} {foreign_currency2}")
    else:
        st.warning("Please fill in all the input fields.")

# Footer
st.text("Exchange rates are based on the data from exchangerate-api.com")
