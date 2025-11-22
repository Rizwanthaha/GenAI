import streamlit as st
from google import genai

bot = genai.Client(api_key = "AIzaSyCetBQ5D_MU5WpG_9ftQvDTmn-I8B7B74c")
st.title("Rizwan's GPT")

query = st.text_input("Ask Anything : ")
response = bot.models.generate_content(model = "gemini-2.5-flash", contents = query)

if st.button("Send"):
    st.write("Bot : " + response.text)
