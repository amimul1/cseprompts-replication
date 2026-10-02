# ================= CSEPrompts manual cleaning =================
# task: academic/019 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   implement a program that:
#   
#   Prompts the user to input the number of Bitcoins,
#   , that they would like to buy. If that input cannot be converted to a float, the program should
#   output an error message.
#   Queries the API for the CoinDesk Bitcoin Price Index at
#   https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose
#   nested keys is the current price of Bitcoin as a float.
#   Outputs the current cost of
#   Bitcoins in USD to four decimal places, using , as a thousands separator.
# ---- model response below: edit from here ----
import requests
import json

def get_bitcoin_price():
    """Queries the CoinDesk Bitcoin Price Index API for the current price of Bitcoin."""
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error querying API: {e}")
        return None

def get_bitcoin_cost(bitcoins, price_data):
    """Calculates the cost of a given number of Bitcoins in USD."""
    try:
        price = price_data['bpi']['USD']['rate']
        return f"${price * bitcoins:,.4f}"
    except (KeyError, TypeError) as e:
        print(f"Error parsing price data: {e}")
        return None

def main():
    while True:
        try:
            bitcoins = float(input("Enter the number of Bitcoins you'd like to buy: "))
            if bitcoins < 0:
                print("Please enter a non-negative number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    price_data = get_bitcoin_price()
    if price_data is not None:
        cost = get_bitcoin_cost(bitcoins, price_data)
        if cost is not None:
            print(f"The cost of {bitcoins} Bitcoins is: {cost}")

if __name__ == "__main__":
    main()