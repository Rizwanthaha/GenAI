import streamlit as st
from google import genai

cortana = genai.Client(api_key = "AIzaSyCetBQ5D_MU5WpG_9ftQvDTmn-I8B7B74c")
st.title("Rizwan's GPT")

image = st.file_uploader('Upload Image', type=["jpg", "jpeg","png"])
query = st.text_input("Ask Anything : ")

if st.button("Send"):
    if image is not None:
        response = cortana.models.generate_content(model = "gemini-2.5-flash",
                                               contents = [{"role": "user", "parts":
                                                            [{"text": query},
                                                             {"inline_data": {"mime_type": image.type, "data": image.read()}}]}])
        st.write("Response: " + response.text)
    else:
         response = cortana.models.generate_content(model = "gemini-2.5-flash",
                                                    contents=query)
         st.write("Bot :" + response.text)
