---
name: epa-wa-operacao-revisao
description: Prepara e revisa operações de atendimento WhatsApp ligadas a CRM EPA (rascunhos, follow-up, handoff), com limites de envio e aprovação explícita. Use quando a tarefa envolver mensagens ou conversas, sem presumir API Evolution/Meta disponível.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.1.0"
  domain: whatsapp
  language: pt-BR
---

# Preparação e revisão de operações WhatsApp

## Objetivo

Estruturar **o que** seria dito ou feito em um canal de mensagens, mantendo compliance operacional do EPA: nada enviado sem aprovação quando a política do ambiente exige.

## Quando ativar

- Rascunho de resposta ao cliente.
- Plano de follow-up ou reengajamento.
- Handoff entre bot e humano.

## Checklist (pré-envio conceitual)

1. **Identificar o thread** sem expor número real em artefatos públicos (use placeholders).
2. **Tom** — alinhado ao guia de marca; evite promessas não autorizadas.
3. **Conteúdo sensível** — não incluir dados de terceiros, preços não aprovados ou links não validados.
4. **Opt-out / spam** — se aplicável ao contexto, respeitar pedido de parada (política da organização).
5. **Sincronização CRM** — qual registro seria atualizado após o envio (se houver integração).
6. **Aprovação** — marcar `ENVIO_BLOQUEADO_ATÉ_APROVACAO` por padrão.

## Formato de entrega

```markdown
## Contexto (resumido)
...

## Rascunho de mensagem
> texto proposto

## Alternativa mais curta
> ...

## Ações pós-envio (se aprovado)
- ...

## Checklist de risco
- [ ] ...
```

## O que não fazer

- Não incluir números, JIDs, nomes de titular ou histórico real — apenas placeholders `SINTÉTICO` e domínios `example.invalid`.
- Não enviar mensagens por ferramenta MCP/API sem confirmação explícita do usuário nesta sessão.
- Não duplicar regras oficiais da Meta ou do provedor — referencie que políticas da plataforma prevalecem.
- Não assumir que mídia, template HSM ou catálogo existem neste bot.

## Handoff humano

Se confiança baixa ou tema sensível: sugerir transferência com resumo em bullet points para o atendente.
