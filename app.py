import streamlit as st
import pandas as pd
import openai

openai.api_key = "YOUR_API_KEY"

st.title("🩺 AI Health Report Generator")

uploaded_file = st.file_uploader("Upload your blood test CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Uploaded Data:", df.head())

    csv_text = df.to_csv(index=False)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a medical data assistant."},
                  {"role": "user", "content": f"Analyze this blood test:
{csv_text}
Provide abnormalities and recommendations."}]
    )

    st.subheader("AI Health Report")
    st.write(response["choices"][0]["message"]["content"])