from llm_engine import get_llm
from graph_state import AgentState

# --- CHAMPION 1: THE BULL ---
def bull_node(state: AgentState) -> dict:
    """The Paladin of Growth. Argues strictly FOR the stock."""
    print("🐂 The Bull is analyzing the data...")
    
    # We summon the LLM with a bit of creativity (temp=0.7)
    llm = get_llm(temperature=0.7)
    
    prompt = f"""You are a statistical data analyst. 
    Review the following numerical dataset for an entity named '{state['ticker']}':
    {state['financial_data']}
    
    Your task: Write a 2-paragraph optimistic analysis of this data. Highlight the mathematical strengths, high margins, and positive indicators. 
    DO NOT use words like "stock," "investing," "buy," or "financial advice." Just analyze the numbers positively.
    """
    
    # The LLM reads the prompt and generates a response
    response = llm.invoke(prompt)
    
    # We return the exact piece of the State we want to update
    return {"bull_argument": response.content}

# --- CHAMPION 2: THE BEAR ---
def bear_node(state: AgentState) -> dict:
    """The Assassin of Risk. Attacks the Bull's argument."""
    print("🐻 The Bear is sharpening its claws...")
    
    llm = get_llm(temperature=0.7)
    
    prompt = f"""You are a critical risk analyst. 
    Review the following numerical dataset for an entity named '{state['ticker']}':
    {state['financial_data']}
    
    Here is a colleague's optimistic analysis:
    "{state['bull_argument']}"
    
    Your task: Write a 2-paragraph critical rebuttal. Focus on mathematical weaknesses, high debt-to-equity ratios, and negative indicators. 
    DO NOT use words like "stock," "investing," "sell," or "financial advice." Critique the numbers strictly as a mathematician.
    """
    
    response = llm.invoke(prompt)
    return {"bear_critique": response.content}

# --- CHAMPION 3: THE JUDGE ---
def judge_node(state: AgentState) -> dict:
    """The Oracle. Pure logic, zero creativity."""
    print("⚖️ The Judge is reviewing the battlefield...")
    
    # We summon the LLM with ZERO creativity (temp=0.0) for strict logic
    llm = get_llm(temperature=0.0)
    
    prompt = f"""You are the Chief Risk Officer. You must remain completely objective.
    Ticker: {state['ticker']}
    Raw Data: {state['financial_data']}
    
    The Bull's Case: {state['bull_argument']}
    The Bear's Critique: {state['bear_critique']}
    
    Your task:
    1. Verify neither side hallucinated numbers by checking their claims against the Raw Data.
    2. Weigh the arguments.
    3. Output a final, structured verdict: BUY, HOLD, or SELL.
    4. Provide 3 bullet points justifying your decision.
    """
    
    response = llm.invoke(prompt)
    return {"final_verdict": response.content}