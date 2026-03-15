import streamlit as st
from orchestrator import fin_debate_app

# --- UI Configuration ---
st.set_page_config(page_title="Fin-Debate-Net", layout="wide", page_icon="⚖️")

st.title("🏛️ Fin-Debate-Net: The Oracle of Wall Street")
st.markdown("""
Welcome to the Arena. Enter a stock ticker, and our AI committee will pull the latest financial data, debate its merits, and issue a final verdict.
*Powered by Llama 3.2, LangGraph, and yfinance. Running 100% locally.*
""")

# --- User Input ---
ticker = st.text_input("Enter a Stock Ticker (e.g., AAPL, TSLA, NVDA):").upper()

if st.button("⚔️ Summon the Committee"):
    if ticker:
        # The spinner keeps the user entertained while your 8GB RAM works hard
        with st.spinner(f"Summoning the champions for {ticker}... (This takes 2-3 minutes on local hardware)"):
            try:
                # 1. Trigger the LangGraph Arena
                initial_state = {"ticker": ticker}
                final_state = fin_debate_app.invoke(initial_state)
                
                # 2. Display the Ground Truth Data
                st.subheader(f"📊 The Scroll of Truth ({ticker} Data)")
                st.json(final_state.get("financial_data", {}))
                
                st.divider()
                
                # 3. Display the Debate side-by-side
                col1, col2 = st.columns(2)
                
                with col1:
                    st.success("🐂 The Bull's Thesis")
                    st.write(final_state.get("bull_argument", "No argument generated."))
                    
                with col2:
                    st.error("🐻 The Bear's Rebuttal")
                    st.write(final_state.get("bear_critique", "No critique generated."))
                    
                st.divider()
                
                # 4. Display the Final Verdict at the bottom
                st.info("⚖️ The Judge's Final Verdict")
                st.write(final_state.get("final_verdict", "No verdict generated."))
                
            except Exception as e:
                st.error(f"❌ The Arena collapsed! Error: {e}")
    else:
        st.warning("Please enter a valid ticker symbol.")