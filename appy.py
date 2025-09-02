import streamlit as st
import pandas as pd
import openai
import os

# Use environment variable for security (recommended)
openai.api_key = os.getenv("OPENAI_API_KEY", "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")

st.title("🩺 AI Health Report Generator")

uploaded_file = st.file_uploader("Upload your blood test CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Uploaded Data:", df.head())

    csv_text = df.to_csv(index=False)

    # Correct way to keep the f-string on one line
    user_prompt = f"Analyze this blood test:\n{csv_text}\nProvide abnormalities and recommendations."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a medical data assistant."},
            {"role": "user", "content": user_prompt}
        ]
    )

    st.subheader("AI Health Report")
    st.write(response["choices"][0]["message"]["content"])
