# Changelog

Todas as mudanças relevantes desta biblioteca são documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/), e o
versionamento da biblioteca segue [SemVer](https://semver.org/lang/pt-BR/) para o
catálogo agregado (campo `libraryVersion` em `catalog.json`).

## [Unreleased]

## [0.3.0] - 2026-11-08

### Adicionado

- `whatsapp-reconexao`: conferir e reconectar instância WhatsApp (Evolution via MCP) sem trocar nome nem token; código no celular ou QR em outra tela; acompanhamento finito; conferência do número; sem restart/webhook/settings.

## [0.2.0] - 2026-11-08

### Adicionado

- Dez skills sanitizadas CRM / WhatsApp / Drive (pacote mantenedor).
- `docs/runtime-guardrails.md`, `docs/proveniencia-skills.md`.

### Alterado

- `epa-coleta-progressiva` fundida com rascunho da PR e pacote sanitizado.
- Slugs aposentados fundidos: `epa-crm-operacao-revisao`, `epa-crm-conhecimento-mapeamento`, `epa-wa-operacao-revisao`.
- Biblioteca `0.2.0` em `catalog.json`.

### Já em 0.1.0 / unreleased anterior

- Política de privacidade, concorrência, `scan_policy.py`, CI fork vs mesmo repo.

### Limitações

- Scanner heurístico + revisão humana; sem teste em sistemas reais.

## [0.1.0] - 2026-11-08

### Adicionado

- Estrutura inicial `skills/<slug>/SKILL.md` conforme [Agent Skills specification](https://agentskills.io/specification).
- Documentação em português: arquitetura, contribuição, segurança, distribuição, migração e compatibilidade.
- `AGENTS.md` para manutenção segura por agentes e humanos.
- Skills genéricas originais: coleta progressiva, revisão de operações CRM e WhatsApp, mapeamento de conhecimento CRM.
- Validador Python, testes e workflow de CI em pull requests.
- `catalog.json` com inventário das skills publicadas no repositório.

### Pendências conhecidas

- Regras de proteção de branch e rulesets exigem GitHub Pro (conta User) ou organização Team; ver `docs/seguranca.md`.
- Sincronização automática GitHub → runtime do bot não documentada oficialmente; instalação assistida descrita em `docs/distribuicao.md`.

[0.1.0]: https://github.com/epasistemas/epa-skills/releases/tag/v0.1.0
