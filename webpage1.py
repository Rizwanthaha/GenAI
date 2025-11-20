import streamlit as st
from google import genai
st.title("My chatGPT")
chitti=genai.Client(api_key="AIzaSyCetBQ5D_MU5WpG_9ftQvDTmn-I8B7B74c")
question=st.text_input("Ask Anything")

if st.button("Send"):
    response=chitti.models.generate_content(
        model="gemini-2.5-flash",
               contents=question)
    st.write(response.text)
