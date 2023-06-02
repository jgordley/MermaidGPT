import streamlit as st

def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key

def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"
            "2. Choose the chart type you wish to generate 📈 \n"
            "3. Give a detailed description of all components and transitions in your chart✍️ \n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",
            value=st.session_state.get("OPENAI_API_KEY", ""),
        )

        if api_key_input:
            set_openai_api_key(api_key_input)

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "🧜‍♀️MermaidGPT is a simple ChatGPT and Mermaid.js integration that allows you to generate diagrams using prompts. ChatGPT generates markdown that is rendered into an image by Mermaid.js in the backend."
        )
        st.markdown(
            "Contribute here: [GitHub](https://github.com/jgordley/MermaidGPT) "
            "Feedback and suggestions are appreciated!"
        )
        st.markdown("Made by [Jack Gordley](https://twitter.com/jackgordley)")
        st.markdown("---")