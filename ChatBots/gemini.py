import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_response(user_question):
    prompt_template = """
    Answer the question based on your knowledge as detailed as possible.\n\n
    Question: \n{question}\n
    Answer:
    """
    model = genai.GenerativeModel('gemini-pro')
    prompt = prompt_template.format(question=user_question)
    response = model.generate_content(prompt)
    text_content = response.candidates[0].content.parts[0].text
    return text_content

def main():
    st.set_page_config("Chat Gemini")
    st.header("Gemini Bot")

    user_question = st.text_input("Ask a Question")
    if user_question and st.button("Submit Question"):
        response = get_response(user_question)
        st.write("Reply: ", response)

if __name__ == "__main__":
    main()



#.env
#GOOGLE_API_KEY="YOUR API KEY"

