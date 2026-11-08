---
name: epa-crm-mapa
description: Localiza telas operacionais do CRM EPA e distingue cadastro, análise e integração documental. Use antes de navegar ou orientar operações quando o agente tem acesso de leitura autorizado, sem host real na skill.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.2.0"
  domain: crm
  language: pt-BR
---

# Mapa estrutural CRM EPA

## Entradas

Origem do admin, contexto organizacional e permissões — da configuração **privada** do cliente. Nenhum host real pertence à skill.

## Rotas estruturais (caminhos relativos ao admin)

- Home: `/admin`
- Negócios: `/admin/crm/negocios`; pipelines: `/admin/crm/pipelines`
- Clientes CRM: `/admin/crm/clientes`; cadastros: `/admin/cadastros`
- Visitas operacionais: `/admin/visits`; configurações: `/admin/visits/config`
- Imobiliárias: `/admin/agencies`; análise: `/admin/bi/imobiliarias`
- Visitas analíticas: `/admin/bi/visitas`; negócios analíticos: `/admin/bi/negocios`
- Drives incorporadoras: `/admin/crm/drives-incorporadoras`

Conhecimento **estrutural** — validar na UI da versão em uso.

## Procedimento

1. Resolver contexto antes de navegar; conferir menu e permissão.
2. Se a tela divergir, registrar divergência **sem PII** e pedir orientação; não forçar acesso nem inventar rota.
3. Não abrir configurações elevadas para consulta comum.

## Mapeamento de vocabulário (complementar)

Quando o pedido for alinhamento de termos (não navegação):

1. Coletar termos citados pelo usuário — sem scraping externo.
2. Definição operacional curta, sinônimos, anti-padrões.
3. Relações em lista ou mermaid simples; lacunas `[[PENDENTE: negócio]]`.
4. Separar fatos declarados de suposições.

Detalhes volumosos podem ir em `references/glossario.md` nesta pasta (sem dados sensíveis).

## Saída

Tela encontrada, finalidade e restrições observadas — **sem** conteúdo de registros.

## Runtime

[Guardrails EPA](../../docs/runtime-guardrails.md) · [Privacidade](../../docs/privacidade.md)
