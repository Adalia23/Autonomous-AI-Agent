import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agent.agent import run_agent

st.set_page_config(page_title="Autonomous AI Agent", page_icon="🤖", layout="wide")

st.title("🤖 Autonomous AI Agent")
st.caption("Powered by Gemini + LangGraph | Give it a goal and watch it think")

st.markdown("""
<style>
    .stTextArea textarea { font-size: 16px; }
    .step-box { background: #1e2130; border-radius: 8px; padding: 15px; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

examples = [
    "Research the latest developments in AI agents and summarize the top 5 trends",
    "What are the best Python libraries for machine learning in 2025 and why?",
    "Compare LangChain vs LangGraph and tell me which is better for building agents",
    "Find the latest news about UAE tech startups and give me a summary"
]

st.subheader("💡 Example Goals")
cols = st.columns(2)
for i, example in enumerate(examples):
    if cols[i % 2].button(example[:60] + "...", key=f"ex_{i}"):
        st.session_state.goal = example

goal = st.text_area(
    "Enter your goal:",
    value=st.session_state.get("goal", ""),
    height=100,
    placeholder="e.g. Research the top 5 AI trends in 2025 and summarize them"
)

if st.button("🚀 Run Agent", type="primary"):
    if not goal.strip():
        st.warning("Please enter a goal first!")
    else:
        with st.spinner("🧠 Agent is thinking and using tools..."):
            try:
                result = run_agent(goal)
                st.success("✅ Agent completed the task!")
                st.subheader("📋 Result")
                if isinstance(result, list):
                    for item in result:
                        if isinstance(item, dict) and item.get('type') == 'text':
                            st.markdown(item['text'])
                else:
                    st.markdown(result)
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.markdown("---")
st.caption("Built with LangGraph + Gemini 2.0 Flash + Tavily Search")