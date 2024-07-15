import requests

API_KEY = 'W2TES2WK49IOFM5O'
BASE_URL = 'https://www.alphavantage.co/query'

portfolio = {}

def get_stock_price(symbol):
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if 'Global Quote' in data:
        return float(data['Global Quote']['05. price'])
    else:
        print(f"Error fetching data for {symbol}.")
        return None

def add_stock(symbol, quantity):
    price = get_stock_price(symbol)
    if price:
        if symbol in portfolio:
            portfolio[symbol]['quantity'] += quantity
            portfolio[symbol]['price'] = price
        else:
            portfolio[symbol] = {'quantity': quantity, 'price': price}
        print(f"Added {quantity} shares of {symbol} at ${price} each to your portfolio.")

def remove_stock(symbol, quantity):
    if symbol in portfolio:
        if portfolio[symbol]['quantity'] > quantity:
            portfolio[symbol]['quantity'] -= quantity
            print(f"Removed {quantity} shares of {symbol} from your portfolio.")
        elif portfolio[symbol]['quantity'] == quantity:
            del portfolio[symbol]
            print(f"Removed all shares of {symbol} from your portfolio.")
        else:
            print(f"Cannot remove {quantity} shares of {symbol}, you only have {portfolio[symbol]['quantity']} shares.")
    else:
        print(f"{symbol} is not in your portfolio.")

def track_performance():
    total_value = 0
    for symbol, data in portfolio.items():
        current_price = get_stock_price(symbol)
        if current_price:
            total_value += current_price * data['quantity']
            print(f"{symbol}: {data['quantity']} shares at ${data['price']} each, current price ${current_price}, total value ${current_price * data['quantity']:.2f}")
    print(f"Total portfolio value: ${total_value:.2f}")

def main():
    print("Welcome to the Stock Portfolio Tracking Tool")
    while True:
        print("\nMenu:")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Track performance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            remove_stock(symbol, quantity)
        elif choice == '3':
            track_performance()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
