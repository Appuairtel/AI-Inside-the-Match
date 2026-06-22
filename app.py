import streamlit as st

st.title("AI Inside the Match")

question = st.text_input("Ask a football question")

if question:
    st.write("AI response will appear here")
