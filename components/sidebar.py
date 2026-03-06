import streamlit as st

PROVIDERS = ["OpenAI", "Anthropic", "Gemini"]

PROVIDER_KEY_MAP = {
    "OpenAI": "OPENAI_API_KEY",
    "Anthropic": "ANTHROPIC_API_KEY",
    "Gemini": "GEMINI_API_KEY",
}

def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Select your AI provider and enter its API key\n"
            "2. Choose the chart type you wish to generate\n"
            "3. Give a detailed description of your chart\n"
        )

        provider = st.selectbox("Provider", PROVIDERS)
        st.session_state["provider"] = provider

        session_key = PROVIDER_KEY_MAP[provider]
        api_key = st.text_input(
            "API Key",
            type="password",
            placeholder="Paste your API key here",
            value=st.session_state.get(session_key, ""),
        )
        if api_key:
            st.session_state[session_key] = api_key

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "MermaidGPT is a simple app that generates Mermaid.js diagrams from text prompts "
            "using your choice of AI provider."
        )
        st.markdown(
            "Contribute here: [GitHub](https://github.com/jgordley/MermaidGPT) — "
            "feedback and suggestions are appreciated!"
        )
        st.markdown("Made by [Jack Gordley](https://twitter.com/jackgordley)")
        st.markdown("---")
