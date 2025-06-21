import streamlit as st
from Ollama.Main.Agent.agent_local import (
    get_agent_llm,
    get_agent_prompt,
    build_agent,
    create_agent_executor,
    run_agent,
    tools
)
import re
with open("chat_style.html", "r", encoding="utf-8") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

st.set_page_config(page_title="Ollama Agent Chat", page_icon="🤖")

# st.title("🤖 Ollama Agent Chat")
st.sidebar.title("About")
st.sidebar.info("This is a chatbot UI powered by Ollama with Qwen:4b and Streamlit.")

if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# Initialize agent only once
if "agent_executor" not in st.session_state:
    agent_llm = get_agent_llm(model_name="qwen3:4b")
    agent_prompt = get_agent_prompt()
    agent_runnable = build_agent(agent_llm, tools, agent_prompt)
    st.session_state.agent_executor = create_agent_executor(agent_runnable, tools)
    st.session_state.chat_history = []

# Chat display area (put this BEFORE the input form)
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f'<div class="message-row"><div class="message-user">{message}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message-row"><div class="message-agent">{message}</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Fixed input form at the bottom
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message...", key="input")
    submitted = st.form_submit_button("Send")
    if submitted and user_input.strip():
        with st.spinner("Thinking..."):
            user_query = f"{user_input} /no_think"
            st.session_state.chat_history.append(("You", user_input))
            response = st.session_state.agent_executor.invoke({"input": user_query})
            agent_output = response['output']
            # Remove <think>...</think> blocks
            agent_output = re.sub(r"<think>.*?</think>", "", agent_output, flags=re.DOTALL).strip()
            st.session_state.chat_history.append(("Agent", agent_output))
            st.rerun()