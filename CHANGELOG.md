# Changelog

Todas as mudanças relevantes desta biblioteca são documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/), e o
versionamento da biblioteca segue [SemVer](https://semver.org/lang/pt-BR/) para o
catálogo agregado (campo `libraryVersion` em `catalog.json`).

## [Unreleased]

### Adicionado

- Política central de privacidade (`docs/privacidade.md`) e protocolo de concorrência (`docs/concorrencia.md`).
- `scripts/scan_policy.py`, `privacy_allowlist.json`, `git_concurrency_check.sh`, `pre_push.sh`.
- Testes de detecção heurística sem vazar valores nos logs.
- CI: job explícito para PRs de fork (falha = validação manual obrigatória).

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
