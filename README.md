# epa-skills

Biblioteca **privada e comercial** de [Agent Skills](https://agentskills.io/specification) para o CRM EPA e fluxos relacionados a WhatsApp. Mantida centralmente em `epasistemas/epa-skills`; contribuições via **pull request** para `main` (squash merge; branch excluída após merge).

## Status

| Item | Estado |
| ---- | ------ |
| Branch padrão | `main` |
| Privacidade | Repositório privado |
| Proteção de branch / rulesets | **Pendente** — API retorna 403 sem GitHub Pro (conta User) ou organização Team; ver [docs/seguranca.md](docs/seguranca.md) |
| Sincronização automática GitHub → bot | **Não documentada oficialmente** — importação assistida em [docs/distribuicao.md](docs/distribuicao.md) |

## Estrutura

```text
skills/<slug>/SKILL.md    # skill (frontmatter name + description obrigatórios)
catalog.json              # índice e libraryVersion
docs/                     # arquitetura, contribuição, segurança, distribuição
scripts/                  # validação e varredura heurística de segredos
AGENTS.md                 # regras para agentes que editam o repo
```

### Skills publicadas (`catalog.json`, 0.3.0)

| Domínio | Slugs |
| ------- | ----- |
| CRM | `epa-coleta-progressiva`, `epa-crm-mapa`, `epa-crm-operacoes`, `epa-crm-visitas`, `epa-crm-drive-incorporacao` |
| WhatsApp | `whatsapp-operacoes`, `whatsapp-onboarding`, `whatsapp-conversas`, `whatsapp-midia`, `whatsapp-reconexao` |
| Drive | `drive-organizacao-documental` |

Proveniência resumida: [docs/proveniencia-skills.md](docs/proveniencia-skills.md). Migração sanitizada integrada; revisão contínua em [docs/migracao.md](docs/migracao.md).

## Uso rápido (desenvolvedor)

```bash
git clone git@github.com:epasistemas/epa-skills.git
cd epa-skills
./scripts/pre_push.sh
```

Ativação no runtime (Cursor, Grok Bot, outros): [docs/distribuicao.md](docs/distribuicao.md).

## Contribuir

1. Branch a partir de `main`.
2. Siga [docs/privacidade.md](docs/privacidade.md), [docs/contribuicao.md](docs/contribuicao.md), [docs/concorrencia.md](docs/concorrencia.md) e [AGENTS.md](AGENTS.md).
3. Abra PR; **revisor diferente do autor** aprova.

`CODEOWNERS` aponta `@epasistemas` (não substitui ACL por pasta). Colaboração futura por **grupos** tende a repos privados separados — [docs/arquitetura.md](docs/arquitetura.md).

## Licença

Proprietária — [LICENSE](LICENSE). Termos comerciais e revisão jurídica de contratos são responsabilidade do mantenedor antes de uso em escala.

## Referências

- [Agent Skills specification](https://agentskills.io/specification)
- [About CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [Repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)
- [Fork permissions](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-for-forks)
- [Grok Bot — Skills](https://cursor.com/docs/grok-bot/work.md)

## Changelog

Ver [CHANGELOG.md](CHANGELOG.md).
