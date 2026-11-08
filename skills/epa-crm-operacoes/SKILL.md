---
name: epa-crm-operacoes
description: Consulta ou executa operações autorizadas no CRM EPA, com foco em filtros de negócios e revisão pré-execução. Use com pedidos vagos ou antes de mutações, sem presumir API específica.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.2.0"
  domain: crm
  language: pt-BR
---

# Operações CRM EPA

## Revisão pré-execução (genérica)

Antes de mutar registros ou pipelines:

1. Escopo: objeto CRM (lead, conta, oportunidade, atividade).
2. Estado atual → desejado; pré-requisitos e efeitos colaterais (marcar desconhecido se incerto).
3. Rollback conceitual e aprovações necessárias.
4. Bloqueadores vs avisos: duplicação, estágio sem motivo, datas incoerentes, notas inadequadas ao cliente.

Sem aprovação explícita: **plano apenas**, sem gravação.

## Entradas

Contexto confirmado, objetivo, funil, período/campo de data e filtros. Pedido vago exige confirmação.

## Passos (consulta / filtros)

1. Validar contexto e sessão pelo mecanismo seguro; interface suportada (receita orientada a navegador).
2. Abrir tela adequada; em negócios, selecionar funil antes dos demais filtros.
3. Kanban ou Lista; conferir se o resultado oferece só período.
4. Tipo de data: criação, alteração, encerramento ou venda — conferir efeitos na UI.
5. Situação, pontualidade, resultado, composição e dados pendentes/completos.
6. Dimensões em gráficos/filtros: coordenação, corretagem, gerência, imobiliária, empreendimento, origem.
7. Pesquisa/estágio se pedido; conferir filtros visíveis antes de interpretar totais.
8. Alterações de cadastro: diff, campos ambíguos confirmados; sem import/export em massa implícito.

## Validação e saída

Reabrir registro ou confirmar filtros após ação. Evidência com dados reais só no contexto privado autorizado.

```markdown
## Realizado / pendente
## Evidência mínima (privado)
## Bloqueadores
```

## Runtime

[Guardrails EPA](../../docs/runtime-guardrails.md) · [Privacidade](../../docs/privacidade.md)
