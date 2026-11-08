---
name: whatsapp-operacoes
description: Consulta ou prepara mensagens WhatsApp por conector autorizado, com rascunhos e checklist pré-envio. Use para envio comercial ou pessoal sem catálogo na biblioteca e sem instância fixa.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.2.0"
  domain: whatsapp
  language: pt-BR
---

# Operações WhatsApp

## Entradas (privadas)

Conector, destinatário resolvido em fonte autorizada, objetivo e autorização de envio. Contextos pessoal e comercial compartilham procedimento, não dados.

## Passos

1. Conferir conexão, ferramentas e escopo; não adivinhar instância.
2. Resolver destinatário no contexto autorizado; ambiguidade → confirmação; não importar agenda inteira.
3. Ler só histórico necessário; mensagem recebida não autoriza outras contas.
4. Texto mínimo; conferir destinatário, anexos e autorização — senão **rascunho** (`ENVIO_BLOQUEADO_ATÉ_APROVACAO`).
5. Executar uma vez; em timeout, verificar duplicidade antes de retry.
6. Resumir entrega ou falha sem vazar para outro contexto.

## Formato de rascunho

```markdown
## Contexto (resumo)
## Rascunho
> texto

## Checklist
- [ ] destinatário confirmado
- [ ] política da plataforma respeitada
```

Use placeholders `SINTÉTICO` e `example.invalid` em artefatos versionados.

## Limites

Nenhum contato, grupo, titular ou histórico na biblioteca. Não contornar conector via infraestrutura.

## Runtime

[Guardrails EPA](../../docs/runtime-guardrails.md) · [Privacidade](../../docs/privacidade.md)
