import streamlit as st

st.set_page_config(page_title="AI Inside the Match", page_icon="0")

st.title("0 AI Inside the Match")
st.subheader("Football Match Explainer Assistant")

st.write(
    "This app helps football fans understand matches before, during, and after the game."
)

match_text = st.text_area("Paste football match report or match details here")

question = st.text_input("Ask a football question")

if st.button("Generate AI Explanation"):
    if match_text or question:
        st.subheader("AI Explanation")
        st.write("IBM Granite AI will analyse the match and provide a simple explanation here.")
    else:
        st.warning("Please enter match details or a question.")
