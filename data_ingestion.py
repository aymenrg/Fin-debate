import yfinance as yf

def fetch_financial_metrics(ticker_symbol: str) -> dict:
    """
    The 'Eyes of Truth'.
    Fetches hard financial data from Yahoo Finance to prevent AI hallucinations.
    """
    print(f"🦅 Sending the raven to fetch market data for {ticker_symbol}...")
    
    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info
        
        # Extract metrics with strict fallback to "Data Unavailable"
        data = {
            "current_price": info.get("currentPrice", "Data Unavailable"),
            "trailing_pe": info.get("trailingPE", "Data Unavailable"),
            "forward_pe": info.get("forwardPE", "Data Unavailable"),
            "debt_to_equity": info.get("debtToEquity", "Data Unavailable"),
            "profit_margins": info.get("profitMargins", "Data Unavailable"),
            "52_week_high": info.get("fiftyTwoWeekHigh", "Data Unavailable"),
            "52_week_low": info.get("fiftyTwoWeekLow", "Data Unavailable")
        }
        
        # Format the profit margin into a readable percentage if it's a number
        if isinstance(data["profit_margins"], float):
            data["profit_margins"] = f"{round(data['profit_margins'] * 100, 2)}%"
            
        return data

    except Exception as e:
        print(f"❌ The raven was intercepted! Error: {e}")
        return {"error": "Failed to fetch data. Check the ticker or your connection."}

# --- TESTING THE ARTIFACT ---
# This block only runs if you execute this specific file directly.
if __name__ == "__main__":
    # Let's test it with Apple (AAPL)
    test_data = fetch_financial_metrics("AAPL")
    
    print("\n📜 The Scroll of Truth returned:")
    for key, value in test_data.items():
        print(f"- {key}: {value}")