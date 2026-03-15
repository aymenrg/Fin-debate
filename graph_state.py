from typing import TypedDict

class AgentState(TypedDict):
    """
    The Shared Ledger. 
    This state gets passed sequentially through our LangGraph arena.
    """
    ticker: str                  # The stock symbol (e.g., "AAPL")
    financial_data: dict         # Ground truth numbers pulled from Yahoo Finance
    bull_argument: str           # The growth thesis 
    bear_critique: str           # The risk manager's rebuttal
    final_verdict: str           # The Judge's final decision