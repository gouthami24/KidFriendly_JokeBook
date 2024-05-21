import streamlit as st
import openai
from langchain_openai import ChatOpenAI

# Set your OpenAI API key here
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Function to convert text to local slang
def generate_joke(type):
    llm = ChatOpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo", temperature = 0.5)
    prompt=f"Tell me a {type} joke that is kid friendly"
    response = llm.stream(prompt)
    return (response)

# Streamlit App
st.title('Joke Generator')

# User input
type = st.selectbox('Select Type of Joke:', ['One Liners','puns','Knock Knock Jokes','Observational','Riddles', 'Animal','Light Bulb'])  

# Generate Joke
if st.button('Generate'):
     generatejoke(type)
else:
     st.write('Please Press Generate Button.')
