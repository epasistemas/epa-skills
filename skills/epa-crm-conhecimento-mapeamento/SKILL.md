---
name: epa-crm-conhecimento-mapeamento
description: Mapeia conceitos, entidades e fluxos de conhecimento CRM EPA a partir de descrições textuais, produzindo glossário e diagrama em texto. Use ao onboardar agentes ou alinhar vocabulário entre times, sem scraping de sistemas.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.1.0"
  domain: crm
  language: pt-BR
---

# Mapeamento de conhecimento CRM

## Objetivo

Organizar **vocabulário e relações** do domínio CRM EPA para consulta por agentes e humanos.

## Quando usar

- Novo membro ou bot precisa entender estágios, papéis e artefatos.
- Documentação espalhada em mensagens precisa virar estrutura estável.

## Método

1. Colete **termos** mencionados pelo usuário (não busque sistemas externos).
2. Para cada termo: definição operacional curta, sinônimos, anti-padrões.
3. Relacione entidades (ex.: Lead → Oportunidade → Pedido) em lista ou diagrama mermaid simples.
4. Marque lacunas com `[[PENDENTE: confirmar com negócio]]`.
5. Separe **fatos declarados** de **suposições**.

## Artefatos

Salve em `references/glossario.md` **dentro da conversa ou PR**, não com dados sensíveis:

```markdown
## Glossário
| Termo | Definição | Sinônimos |
| ----- | --------- | --------- |

## Fluxos principais
(mermaid ou lista numerada)
```

## Progressive disclosure

Mantenha `SKILL.md` enxuto; detalhes volumosos vão para arquivos em `references/` nesta pasta da skill quando versionados no repo.

## Limites

- Não substitui documentação oficial de produto ou contrato.
- Não incluir contatos, tenants ou URLs de produção.
