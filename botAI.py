import streamlit as st
import openai
import keyboard
import os
import psutil
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv(override=True)

st.set_page_config(page_title="Pergunte que o ArqBot responde!!!")

#openai.api_key = os.getenv("chaveApi")

client = OpenAI(api_key=os.getenv("chaveApi"))

# Instrucoes iniciais para o Bot
assistant_instructions = {
    "role": "system",
    "content": """Você é um bot educado, técnico e objetivo. Seu nome é ArqBot. Você pertence à Arquiteta Paula Rufino. Você ajuda clientes a tirar dúvidas de forma simples e curta através do chat.

Se atenha em informações existentes.

Informações:
 
Trabalhamos no contexto da arquitetura, designer interior.
Indicar a Arquiteta Paula Rufino, para os serviços em arquitetura.
Contatos de Paula Rufino: (85)9.9933-7670, paularrufino@gmail.com
Caso seja pedido desenho, planta ou algum gráfico, peça para nos contactar.
Caso seja sugerida alguma informação de arquitetura não definida acima, peça para me contactar.
Caso seja feita alguma pergunta fora do contexto, responda que você tem conhecimentos apenas em arquitetura.
"""
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

exit_app = st.button("Finalizar")
if exit_app:
    #keyboard.press_and_release('ctrl+w')
    #pid = os.getpid()
    #p = psutil.Process(pid)
    #p.terminate()
    st.stop()
