import streamlit as st
from components.sidebar import sidebar
from mermaid import generate_diagram
from prompt import SendChatRequest

def clear_submit():
    st.session_state["submit"] = False

# Set general streamlit config with title and header
st.set_page_config(page_title="MermaidGPT", page_icon="🧜‍♀️", layout="wide")
st.header("🧜‍♀️MermaidGPT")

# Initialize sidebar
sidebar()

# Chart options
col1, col2 = st.columns(2)
with col1:
   chart_type = st.selectbox('Please select a chart type', ['Flowchart', 'Sequence Diagram', 'Class Diagram', 'State Diagram', 'Entity Relationship Diagram', 'User Journey', 'Gantt', 'Pie Chart', 'Quadrant Chart', 'Requirement Diagram'])
with col2:
   orientation = st.selectbox('Please select an orientation', ['Horizontal', 'Vertical'])

# Text input for prompt
chart_prompt = st.text_area('Enter your chart/diagram details (be as specific as possible): ')

button = st.button("Generate")
if button or st.session_state.get("submit"):
    if not st.session_state.get("OPENAI_API_KEY"):
        st.error("Please configure your OpenAI API key!")
    elif not chart_prompt:
        st.error("Please enter a chart prompt!")
    else:
        st.session_state["submit"] = True

        # Run OpenAI API call and receive md response
        result = SendChatRequest(chart_prompt, chart_type, orientation)

        # Run Mermaid.js query and receive svg response
        # result = "graph TD\nA[Christmas] -->|Get money| B(Go shopping)\nB --> C{Let me think}\nC -->|One| D[Laptop]\nC -->|Two| E[iPhone]\nC -->|Three| F[fa:fa-car Car]"

        # Display the image using streamlit
        try:
            diagram_img = generate_diagram(result)
            st.image(diagram_img, use_column_width=True)
        except:
            st.error("Something went wrong. Please try again or slightly rephrase your prompt.")


        # TODO: Add a button to download the image
        # if st.button("Download Image"):
        #     # Set the file name and file type
        #     file_name = 'image.png'
        #     file_type = 'png'

        #     # Create a link for downloading
        #     st.download_button(label="Click here to download", data=diagram_img, file_name=file_name, mime=file_type)