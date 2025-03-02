import streamlit as st
import openai
import keyboard
import os
import psutil
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv(override=True)

st.set_page_config(page_title="ArqBot responde!!!")
st.write("# Arquitetura & Interiores")

client = OpenAI(api_key=os.getenv("chaveApi"))

# Instrucoes iniciais para o Bot
assistant_instructions = {
    "role": "system",
    "content": os.getenv("instrucoes")
}

listaMensagens = []
listaMensagens.insert(0, assistant_instructions)

st.session_state["messages"] = listaMensagens

@st.cache_data

def montarIA(textoRecebido):
    st.session_state.messages.append({"role": "user", "content": texto})
    response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
    return response.choices[0].message.content    

with st.container():
    i = 0
    while True:
        texto = st.text_input("Faça sua pergunta: ", key=i)
        i = i + 1
        if texto == "fim" or len(texto) < 1:
            break
        else:
            msg = montarIA(texto)
            st.chat_message("assistant").write(msg)

    if texto == "fim":
        st.write("ArqBot: Até mais! ArqBot à disposição!")
