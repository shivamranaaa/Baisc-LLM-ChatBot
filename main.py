# Q&A Chatbot
from langchain.llms import OpenAI
import langchain

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

def get_openai_response(question):
    try:
        # Initialize the InferenceClient with the model name (not repo_id)
        llm_huggingface=langchain.llms.HuggingFaceHub(repo_id="google/flan-t5-large",model_kwargs={"temperature":0,"max_length":64})
        output=llm_huggingface.predict(question)
        return output
    except:
        return "model loading"
##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)