---
name: epa-crm-visitas
description: Consulta visitas, prepara validação e preenche Feedback autorizado no CRM EPA. Use em filas A Validar, feedback de visita ou cadastro de agência relacionado, sem contatos automáticos.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.2.0"
  domain: crm
  language: pt-BR
---

# Visitas CRM EPA

## Entradas

Período, status, filtros, registros-alvo e respostas confirmadas. Não inferir presença ou interesse da ausência de resposta.

## Passos

1. Abrir lista de visitas; confirmar contexto; filtrar período/status — validação: **A Validar** quando disponível.
2. Indicadores de validação; abrir linha → Feedback no detalhe.
3. Campos: fluxo; aconteceu?; observação; se sim, interesse e coordenação; se não, ação remarcar/cancelar quando exibida.
4. Não inventar campos; não confundir botão Cancelar com cancelamento da visita.
5. Pendências: obter faltantes via [coleta progressiva](../epa-coleta-progressiva/SKILL.md); contatos só por fluxo autorizado.
6. Salvar somente respostas verificadas; arquivar/cancelar/limpar feedback exige autorização específica.
7. Reabrir e verificar persistência; em erro, manter pendência.

## Cadastro relacionado

Imobiliária operacional: tela de agências, não BI. Apenas campos exigidos no sistema autorizado.

## Saída

Quantidade processada, pendências e falhas — sem exportação em massa obrigatória.

## Runtime

[Guardrails EPA](../../docs/runtime-guardrails.md) · [Privacidade](../../docs/privacidade.md)
