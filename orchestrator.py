from langgraph.graph import StateGraph, END
from graph_state import AgentState
from data_ingestion import fetch_financial_metrics
from agents import bull_node, bear_node, judge_node

# --- THE GATEKEEPER NODE ---
def fetch_node(state: AgentState) -> dict:
    """Wraps our data scraper so LangGraph can use it."""
    ticker = state["ticker"]
    data = fetch_financial_metrics(ticker)
    
    # We return the exact dictionary key we want to update in the State
    return {"financial_data": data}

# --- BUILD THE ARENA ---
# 1. Initialize the Graph with our magical scroll (AgentState)
workflow = StateGraph(AgentState)

# 2. Add the Champions to the Arena (Nodes)
workflow.add_node("fetch_data", fetch_node)
workflow.add_node("bull_agent", bull_node)
workflow.add_node("bear_agent", bear_node)
workflow.add_node("judge_agent", judge_node)

# 3. Define the Rules of Combat (Edges)
# This forces the strictly sequential turn-based execution!
workflow.set_entry_point("fetch_data")
workflow.add_edge("fetch_data", "bull_agent")
workflow.add_edge("bull_agent", "bear_agent")
workflow.add_edge("bear_agent", "judge_agent")
workflow.add_edge("judge_agent", END)

# 4. Lock the Gates (Compile the Graph)
fin_debate_app = workflow.compile()

# --- TESTING THE ARENA ---
# This only runs if you execute this file directly in the terminal
if __name__ == "__main__":
    print("⚔️ Welcome to the Arena. Let the debate begin!")
    
    # We hand the system a blank scroll with just a target ticker
    initial_state = {"ticker": "MSFT"}  # Let's test Microsoft
    
    # Trigger the workflow!
    final_state = fin_debate_app.invoke(initial_state)
    
    print("\n\n🏆 THE FINAL VERDICT 🏆\n")
    print(final_state["final_verdict"])