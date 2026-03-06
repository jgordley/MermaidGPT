import streamlit as st

SYSTEM_PROMPT = (
    "You are a bot that only communicates in Mermaid.js formatted markdown. "
    "Do not provide any additional information or notes, ONLY markdown."
)

def _build_prompt(prompt, chart_type):
    return (
        f"Generate markdown for mermaid.js for a chart of type {chart_type} "
        f"with the following details and only return the markdown that can be pasted into a mermaid.js viewer:\n{prompt}"
    )

def _clean(graph):
    return graph.replace("```mermaid", "").replace("```", "").strip()

def _send_openai(prompt, chart_type):
    import openai
    client = openai.OpenAI(api_key=st.session_state.get("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _build_prompt(prompt, chart_type)},
        ],
        max_tokens=1000,
    )
    return _clean(response.choices[0].message.content)

def _send_anthropic(prompt, chart_type):
    import anthropic
    client = anthropic.Anthropic(api_key=st.session_state.get("ANTHROPIC_API_KEY"))
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": _build_prompt(prompt, chart_type)}],
    )
    return _clean(message.content[0].text)

def _send_gemini(prompt, chart_type):
    import google.generativeai as genai
    genai.configure(api_key=st.session_state.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash", system_instruction=SYSTEM_PROMPT)
    response = model.generate_content(_build_prompt(prompt, chart_type))
    return _clean(response.text)

def SendChatRequest(prompt, chart_type, direction, provider):
    if provider == "OpenAI":
        return _send_openai(prompt, chart_type)
    elif provider == "Anthropic":
        return _send_anthropic(prompt, chart_type)
    elif provider == "Gemini":
        return _send_gemini(prompt, chart_type)
