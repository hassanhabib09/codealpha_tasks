def track_portfolio():

    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "MSFT": 330.0,
        "GOOGL": 135.0,
        "AMZN": 140.0
    }

    user_portfolio = {}
    
    print("Welcome to the Stock Portfolio Tracker!")
    print(f"Available stocks and prices: {stock_prices}\n")

    while True:
        stock_name = input("Enter the stock ticker (or type 'done' to calculate): ").upper()
        
        if stock_name == 'DONE':
            break
        
        if stock_name not in stock_prices:
            print("Stock not found in our current database. Please try another.")
            continue
            
        try:
            quantity = float(input(f"Enter the quantity of {stock_name} shares you own: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue

            if stock_name in user_portfolio:
                user_portfolio[stock_name] += quantity
            else:
                user_portfolio[stock_name] = quantity
                
        except ValueError:
            print("Invalid input. Please enter a numerical value for the quantity.")

    print("\n--- Portfolio Summary ---")
    total_investment = 0.0
    summary_text = "--- Portfolio Summary ---\n"
    
    for stock, qty in user_portfolio.items():
        price = stock_prices[stock]
        stock_value = qty * price 
        total_investment += stock_value
        
        line_item = f"{stock}: {qty} shares @ ${price:.2f} each = ${stock_value:.2f}"
        print(line_item)
        summary_text += line_item + "\n"
        
    final_total_line = f"\nTotal Investment Value: ${total_investment:.2f}"
    print(final_total_line)
    summary_text += final_total_line + "\n"

    save_file = input("\nWould you like to save this summary to a .txt file? (y/n): ").lower()
    if save_file == 'y':
        try:
            with open("portfolio_summary.txt", "w") as file:
                file.write(summary_text)
            print("Successfully saved to 'portfolio_summary.txt'.")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")

if __name__ == "__main__":
    track_portfolio()