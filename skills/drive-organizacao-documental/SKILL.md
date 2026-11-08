---
name: drive-organizacao-documental
description: Planeja organização, classificação e incorporação de arquivos em Drive autorizado, sem ampliar compartilhamento. Use para convenções de nome, deduplicação e movimentação com escopo mínimo.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.2.0"
  domain: drive
  language: pt-BR
---

# Organização documental (Drive)

## Autoria e escopo

Receita **original** desta biblioteca. Não deriva de plugin. Sem API fixa nem sincronização automática presumida.

## Entradas

Origem autorizada, destino confirmado, convenção de nomes, classificação e operações permitidas. IDs reais só na configuração privada de execução.

## Passos

1. Descobrir capacidades do conector; escopo mínimo de pastas.
2. Metadados mínimos; evitar ler conteúdo sensível se metadados bastarem.
3. Propor árvore e nome `AAAA-MM-DD_descricao.ext`; desconhecido explícito.
4. Duplicatas por checksum quando disponível; não excluir automaticamente.
5. Plano mover/copiar/renomear — confirmar efeito em permissões; parar se ampliar acesso.
6. Referência/atalho quando apropriado; upload/movimentação com escopo mínimo.
7. Validar destino e restrições; reportar parciais.
8. Índice privado opcional — nunca virar skill pública.

## Limites

Sem link público, concessão de acesso, exclusão de original ou mudança de fronteira de segurança sem autorização específica.

## Runtime

[Guardrails EPA](../../docs/runtime-guardrails.md) · [Privacidade](../../docs/privacidade.md)
