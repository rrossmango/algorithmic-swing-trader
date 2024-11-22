import alpaca_trade_api as tradeapi

# Alpaca API credentials
API_KEY = "your_api_key"
SECRET_KEY = "your_secret_key"
BASE_URL = "https://paper-api.alpaca.markets"  # Use this for paper trading

# Initialize the Alpaca API
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")

# Authenticate and check account
def get_account_info():
    try:
        account = api.get_account()
        print("Account Info:")
        print(f"ID: {account.id}")
        print(f"Status: {account.status}")
        print(f"Equity: ${account.equity}")
        print(f"Buying Power: ${account.buying_power}")
        return account
    except Exception as e:
        print(f"Error retrieving account info: {e}")
        return None

# Get stock price (last trade price)
def get_stock_price(symbol: str):
    try:
        barset = api.get_last_trade(symbol)
        price = barset.price
        print(f"Last trade price for {symbol}: ${price}")
        return price
    except Exception as e:
        print(f"Error retrieving stock price for {symbol}: {e}")
        return None

# Buy a stock
def buy_stock(symbol: str, quantity: int):
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=quantity,
            side="buy",
            type="market",
            time_in_force="gtc",  # Good 'til canceled
        )
        print(f"Buy order placed: {quantity} shares of {symbol}.")
        return order
    except Exception as e:
        print(f"Error placing buy order: {e}")
        return None

# Sell a stock
def sell_stock(symbol: str, quantity: int):
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=quantity,
            side="sell",
            type="market",
            time_in_force="gtc",  # Good 'til canceled
        )
        print(f"Sell order placed: {quantity} shares of {symbol}.")
        return order
    except Exception as e:
        print(f"Error placing sell order: {e}")
        return None

# Get portfolio holdings
def get_portfolio_holdings():
    try:
        positions = api.list_positions()
        print("Portfolio Holdings:")
        for position in positions:
            print(
                f"{position.qty} shares of {position.symbol} at ${position.current_price} per share."
            )
        return positions
    except Exception as e:
        print(f"Error retrieving portfolio holdings: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Get account details
    account = get_account_info()

    # Example operations
    if account and account.status == "ACTIVE":
        get_stock_price("AAPL")
        buy_stock("AAPL", 1)  # Buy 1 share of Apple
        sell_stock("AAPL", 1)  # Sell 1 share of Apple
        get_portfolio_holdings()
