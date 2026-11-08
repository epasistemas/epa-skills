# Instruções para agentes (manutenção)

Este arquivo orienta **agentes de IA e automações** que editam `epa-skills`. Humanos devem seguir [docs/contribuicao.md](docs/contribuicao.md).

## Mandatórios

1. Branch de trabalho **não** é `main`; integrar só via PR.
2. Branch principal do repositório: **`main`** (nunca renomear para `master`).
3. Repositório **privado** — não publicar, fork público, template exportado ou pacote registry público.
4. **Privacidade** — política central em [docs/privacidade.md](docs/privacidade.md): sem PII, contatos, JID, tenant, URL privada, credencial ou config por cliente. Não buscar fontes legadas fora do que o mantenedor anexar sanitizado.
5. Não adicionar convidados nem contornar plano/privacidade do repositório.
6. Não contornar 403 de branch protection (tornar público, comprar plano, criar org) sem ordem explícita do mantenedor.
7. Autor da PR **não** aprova nem faz merge da própria PR.
8. Skills de plugin/marketplace **não** são copiadas para cá automaticamente.
9. **Concorrência** — seguir [docs/concorrencia.md](docs/concorrencia.md): sem `reset --hard`, force-push, amend/rebase de commits publicados; integrar remoto com merge; parar em conflito sensível.

## Estrutura de skill

- Caminho: `skills/<slug>/SKILL.md`
- `name` no frontmatter **igual** ao `<slug>`
- Atualizar `catalog.json` ao adicionar/remover skills
- Atualizar `CHANGELOG.md` em mudanças visíveis

## Antes de pull / commit / push

1. `git branch -vv` · `git status` · `git fetch origin`
2. Comparar SHAs e `git log HEAD..origin/<branch>`
3. `./scripts/git_concurrency_check.sh` (se behind: merge, não force-push)
4. Revisar diff **completo** (skills, docs, catalog, workflows, scripts) — não só `SKILL.md`
5. `./scripts/pre_push.sh` ou comandos equivalentes

## Validação (heurística; revisor humano obrigatório)

```bash
./scripts/pre_push.sh
```

`scan_policy.py` reporta apenas `arquivo:linha:regra` — nunca o valor detectado nos logs.

## Modelo de pull request

Preencher `.github/pull_request_template.md`. Incluir:

- Skills afetadas
- Confirmação de ausência de dados sensíveis
- Nota se ativação em runtime foi testada (dados fictícios)

## CI

- Workflow `validate-pr.yml`: job `validate` só no **mesmo repositório**.
- PR de **fork**: job `fork-manual-validation-required` falha de propósito — **skipped validate ≠ aprovado**.
- Não introduzir `pull_request_target` executando código de fork.
- Manter `permissions: contents: read`.

## Segredos e exemplos

Placeholders: [docs/seguranca.md](docs/seguranca.md) e [docs/privacidade.md](docs/privacidade.md). Exceções pontuais: `scripts/privacy_allowlist.json`.

## Migração futura

Inventário interno (nomes apenas): `wa-bot-ops`, `epa-browser-ops`, `epa-mapa`, `crm-knowledge-map`, `epa-coleta-conversacional`, `epa-visitas-*`, `epa-wa-*`, onboarding — seguir [docs/migracao.md](docs/migracao.md). **Não alegar** que migração já ocorreu neste repo salvo arquivos commitados.

## Pendências de plataforma

Proteção/rulesets em `main`: pendente GitHub Pro ou org Team — ver [docs/seguranca.md](docs/seguranca.md). Não prometer proteção ativa na comunicação externa.

## CODEOWNERS

Alterações em `.github/workflows/` exigem atenção de `@epasistemas` via CODEOWNERS.
