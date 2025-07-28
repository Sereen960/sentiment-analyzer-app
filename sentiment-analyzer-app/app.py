import streamlit as st
from textblob import TextBlob

st.title("💬 Sentiment Analyzer App")

text_input = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        blob = TextBlob(text_input)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            result = "Positive 😊"
            color = "green"
        elif sentiment < 0:
            result = "Negative 😞"
            color = "red"
        else:
            result = "Neutral 😐"
            color = "gray"

        st.markdown(f"**Sentiment:** <span style='color:{color}'>{result}</span>", unsafe_allow_html=True)
        st.write(f"**Polarity Score:** {sentiment}")
