import streamlit as st

from agent import AIAgent

st.set_page_config(page_title="AI Agent Demo", page_icon="🤖")
st.title("🤖 AI Agent Demo")
st.caption("A minimal UI to test your AI agent.")

# Sidebar controls
with st.sidebar:
    st.header("Settings")
    system_prompt = st.text_area(
        "System prompt",
        value="You are a helpful assistant.",
        height=120,
    )
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask the agent something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                agent = AIAgent(system_prompt=system_prompt)
                reply = agent.run(st.session_state.messages)
            except Exception as exc:  # noqa: BLE001
                reply = f"⚠️ Error: {exc}"
            st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})

