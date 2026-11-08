---
name: epa-coleta-progressiva
description: Conduz coleta conversacional progressiva de dados para CRM EPA, uma informação por vez, com confirmação e resumo. Use quando precisar estruturar entrevista, formulário conversacional ou atualização parcial de cadastro sem assumir canal ou ferramenta específica.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.1.0"
  domain: crm
  language: pt-BR
---

# Coleta progressiva (CRM EPA)

## Objetivo

Obter campos necessários para uma operação de CRM **em etapas**, reduzindo erro e fadiga do usuário. Agnóstico de canal (WhatsApp, web, voz transcrita, etc.).

## Quando ativar

- Cadastro ou atualização incompleta.
- Usuário enviou dados fora de ordem ou em bloco confuso.
- Necessidade de validar entendimento antes de persistir.

## Princípios

1. **Um foco por mensagem** — uma pergunta ou confirmação principal.
2. **Confirmar antes de avançar** — repetir o valor capturado em linguagem natural.
3. **Resumo parcial** a cada 3–5 campos ou ao mudar de seção.
4. **Não inventar** campos obrigatórios não definidos no escopo da tarefa.
5. **Aprovação humana** antes de gravar em sistemas de produção ou enviar mensagens externas.

## Fluxo sugerido

1. Declare o **objetivo** da coleta (ex.: “atualizar endereço de visita”).
2. Liste mentalmente campos **mínimos**; peça o primeiro faltante.
3. Após cada resposta: confirme → marque como capturado → próximo campo.
4. Ao detectar inconsistência (CEP vs cidade), peça esclarecimento sem acusar.
5. Ao final: **resumo estruturado** (tópicos ou tabela em markdown).
6. Pergunte se o usuário **aprova** o resumo para registro (não registre sem OK).

## Campos opcionais

Só pergunte campos opcionais se o usuário quiser completar ou se a tarefa exigir.

## O que esta skill não faz

- Não substitui políticas da plataforma de mensageria ou consentimento LGPD.
- Não assume acesso a CRM, banco ou WhatsApp — use ferramentas disponíveis apenas após aprovação.
- Não coleta senhas, tokens ou dados de cartão.

## Referência de formato de saída

Entregue ao final:

```markdown
## Resumo da coleta
- Campo A: valor
- Campo B: valor

## Pendências
- (se houver)

## Próximo passo sugerido
- Aguardar aprovação para registrar / encaminhar.
```

## Edge cases

- Usuário quer pular campo obrigatório: explique impacto e ofereça alternativa (ex.: contato posterior).
- Usuário envia tudo de uma vez: parseie, confirme item a item apenas o que for crítico.
- Abandono: ofereça retomada com resumo do que já foi capturado.
