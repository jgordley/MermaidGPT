import streamlit as st
from components.sidebar import sidebar, PROVIDER_KEY_MAP
from mermaid import generate_diagram
from prompt import SendChatRequest

st.set_page_config(page_title="MermaidGPT", page_icon="🧜‍♀️", layout="wide")
st.header("🧜‍♀️MermaidGPT")

sidebar()

col1, col2 = st.columns(2)
with col1:
    chart_type = st.selectbox("Chart type", [
        "Flowchart", "Sequence Diagram", "Class Diagram", "State Diagram",
        "Entity Relationship Diagram", "User Journey", "Gantt", "Pie Chart",
        "Quadrant Chart", "Requirement Diagram",
    ])
with col2:
    orientation = st.selectbox("Orientation", ["Horizontal", "Vertical"])

chart_prompt = st.text_area("Enter your chart/diagram details (be as specific as possible):")

if st.button("Generate"):
    provider = st.session_state.get("provider", "OpenAI")
    session_key = PROVIDER_KEY_MAP[provider]
    if not st.session_state.get(session_key):
        st.error(f"Please enter your {provider} API key in the sidebar.")
    elif not chart_prompt:
        st.error("Please enter a chart prompt.")
    else:
        result = SendChatRequest(chart_prompt, chart_type, orientation, provider)
        try:
            diagram_img = generate_diagram(result)
            st.image(diagram_img, width=900)
        except Exception as e:
            st.error(f"Error rendering diagram: {e}")
        st.write(f"Resulting markdown: {result}")
