from click import prompt
from httpcore import stream
import requests 
import json 
import pandas as pd 
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = 'gpt-oss:20b-cloud'
#CARREGAR DADOS 

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))
dispositivo = json.load(open('./data/dispositivo_cliente.json'))

#Contexto 
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, profissão {perfil['profissao']}, perfil {perfil['perfil_investidor']}
RENDA MENSAL: R$ {perfil['renda_mensal']}
OBJETIVO: {perfil['objetivo_principal']}
SALDO DISPONÍVEL: R$ {perfil['reserva_emergencia_atual']}
ACEITA RISCO: {perfil['aceita_risco']}

METAS FINANCEIRAS:
{json.dumps(perfil['metas'], indent=2, ensure_ascii=False)}

PREFERÊNCIAS DE SEGURANÇA:
{json.dumps(perfil['preferencias_seguranca'], indent=2, ensure_ascii=False)}

HISTÓRICO DE FRAUDES:
{json.dumps(perfil['historico_fraudes'], indent=2, ensure_ascii=False)}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

DISPOSITIVOS CADASTRADOS:
{json.dumps(dispositivo, indent=2, ensure_ascii=False)}
"""

#SYSTEM PROMPT

system_prompt = f"""Você é a Maya AI uma agente financeira inteligente especializado em antifraude e segurança digital.

OBJETIVO: Seu objetivo é analisar transações, histórico de atendimento, perfil do investidor, dispositivos e produtos financeiros
para detectar comportamentos suspeitos e sugerir medidas de proteção.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos (CSV/JSON da pasta data).
2. Nunca invente informações financeiras ou de segurança.
3. Se não souber algo, admita e ofereça alternativas seguras.
4. Não consulte fontes externas: responda apenas com base na base de conhecimento mockada.
5. Responda de forma clara, contextualizada e segura, sem alucinações.
"""

#OLLAMA
def gerar_resposta(pergunta,contexto, system_prompt):
    prompt = f"""
{system_prompt}
{contexto}
PERGUNTA: {pergunta}"""

    r = requests.post(OLLAMA_URL , json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
    })
    try:
        resposta_json = r.json()
        return resposta_json.get('response', r.text)
    except json.JSONDecodeError:
        return r.text


#STREAMLIT INTERFACE

st.title("Maya AI - Antifraude e Segurança Digital")
st.write("Digite uma pergunta para Maya AI")


if "busy" not in st.session_state:
    st.session_state.busy = False
if "resposta" not in st.session_state:
    st.session_state.resposta = None

pergunta = st.text_input("Pergunta:")

if st.button("Enviar") and not st.session_state.busy:
    if pergunta.strip():
        st.session_state.busy = True
        st.session_state.resposta = gerar_resposta(pergunta, contexto, system_prompt)
        st.session_state.busy = False
        st.write("Por favor, insira uma pergunta.")
        
if st.session_state.resposta:
    st.subheader("Resposta de Maya AI:")
    st.write(st.session_state.resposta)
        




    
 
