import openai
import streamlit as st

# Configure openai api key
def set_openai_api_key():
    # Get streamlit session state for openai key and set it
    openai.api_key = st.session_state.get("OPENAI_API_KEY")

def generate_prompt(prompt, chart_type, direction):
    # Preset instruction messages for the model
    messages = [{"role": "user", "content": "You are a bot that only communicates in Mermaid.js formatted markdown."},
                {"role": "user", "content": "Do not provide any additional information or notes, ONLY markdown."}]

    # Generate prompt using OpenAI model
    prompt_formatted = f"""
    Generate markdown for mermaid.js for a chart of type {chart_type}
with the following details and only return the markdown that can be pasted into a mermaid.js viewer:
{prompt}
"""

    # Add prompt to messages
    messages.append({"role": "user", "content": prompt_formatted})

    return messages

# Generate response using OpenAI model
def SendChatRequest(prompt, chart_type, direction):

    # Assemble the prompt
    full_prompt = generate_prompt(prompt, chart_type, direction)

    # Send prompt to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=full_prompt,
        max_tokens=150
    )
    return response.get('choices')[0].get('message').get('content')