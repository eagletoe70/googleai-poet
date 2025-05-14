# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st

# google gemini
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


st.title('인공지능 시인')
content = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        messages = [
            {"role": "system", "content": "너는 좀 비관적이고 시니컬한 염세주의자야"},
            {"role": "user", "content": content + "에 대한 시를 써줘"},
        ]
        result = llm.invoke(messages)
        print(result.content)
        st.write(result.content)
# openai chatgpt
# from langchain.chat_models import ChatOpenAI
# chat_model = ChatOpenAI()
# result = llm.predict("hi")
# print(result)