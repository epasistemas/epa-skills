# Instruções para agentes (manutenção)

Este arquivo orienta **agentes de IA e automações** que editam `epa-skills`. Humanos devem seguir [docs/contribuicao.md](docs/contribuicao.md).

## Mandatórios

1. Branch de trabalho **não** é `main`; integrar só via PR.
2. Branch principal do repositório: **`main`** (nunca renomear para `master`).
3. Repositório **privado** — não publicar, fork público, template exportado ou pacote registry público.
4. Não adicionar convidados, credenciais, PII, URLs internas ou tokens reais.
5. Não contornar 403 de branch protection (tornar público, comprar plano, criar org) sem ordem explícita do mantenedor.
6. Autor da PR **não** aprova nem faz merge da própria PR.
7. Skills de plugin/marketplace **não** são copiadas para cá automaticamente.

## Estrutura de skill

- Caminho: `skills/<slug>/SKILL.md`
- `name` no frontmatter **igual** ao `<slug>`
- Atualizar `catalog.json` ao adicionar/remover skills
- Atualizar `CHANGELOG.md` em mudanças visíveis

## Validação antes de push

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -p 'test_*.py' -q
python3 scripts/scan_secrets.py
```

## Modelo de pull request

Preencher `.github/pull_request_template.md`. Incluir:

- Skills afetadas
- Confirmação de ausência de dados sensíveis
- Nota se ativação em runtime foi testada (dados fictícios)

## CI

- Workflow `validate-pr.yml` roda em `pull_request` no mesmo repositório.
- Não introduzir `pull_request_target` que execute código de contribuidores de fork.
- Manter `permissions: contents: read`.

## Segredos em exemplos

Use apenas placeholders documentados em [docs/seguranca.md](docs/seguranca.md).

## Migração futura

Inventário interno (nomes apenas): `wa-bot-ops`, `epa-browser-ops`, `epa-mapa`, `crm-knowledge-map`, `epa-coleta-conversacional`, `epa-visitas-*`, `epa-wa-*`, onboarding — seguir [docs/migracao.md](docs/migracao.md). **Não alegar** que migração já ocorreu neste repo salvo arquivos commitados.

## Pendências de plataforma

Proteção/rulesets em `main`: pendente GitHub Pro ou org Team — ver [docs/seguranca.md](docs/seguranca.md). Não prometer proteção ativa na comunicação externa.

## CODEOWNERS

Alterações em `.github/workflows/` exigem atenção de `@epasistemas` via CODEOWNERS.
