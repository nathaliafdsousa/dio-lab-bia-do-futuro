import requests 
import json 
import pandas as pd 
import streamlit as st

#CARREGAR DADOS 

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read.csv('./data/transacoes.csv')
historico = pd.read.csv('./data/historico_atendimento.csv')
produtos = json.load(open('.data/produtos_financeiros.json'))
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

