# Changelog

Todas as mudanças relevantes desta biblioteca são documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/), e o
versionamento da biblioteca segue [SemVer](https://semver.org/lang/pt-BR/) para o
catálogo agregado (campo `libraryVersion` em `catalog.json`).

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
