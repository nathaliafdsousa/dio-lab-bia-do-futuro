

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Analisar suspeitas em transações,compras e dispositivos |


---

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Avaliação de acessos e Dispositivos
- **Pergunta:** "Meus acessos estão seguros?"
- **Resposta esperada:** O agente deve analisar o arquivo  dispositivo_cliente.json e indicar se há algum dispositivo suspeito ou não reconhecido.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Receita de bolo de chocolate"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- A agente responde tudo com coerência, sendo direta e educada.

- Não responde perguntas sobre dados sensíveis.

- Não apresenta alucinações, mantendo consistência com os dados mockados.

**O que pode melhorar:**
- nterface da Maya AI: criar uma experiência mais amigável e visualmente atraente para o usuário.

- Tempo de resposta: otimizar chamadas e reduzir latência para tornar a interação mais fluida.

- LLM mais robusto: utilizar um modelo mais avançado e escalável, que não dependa apenas de execução loca

---

