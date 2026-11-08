# Política de branches

## Branch principal

- Nome obrigatório: **`main`**.
- Destino de todas as pull requests de contribuição.

## Tipos de branch

| Padrão | Uso |
| ------ | --- |
| `main` | Histórico estável; merge somente via PR |
| `feature/<descricao>` | Skills ou docs por iniciativa humana |
| `fix/<descricao>` | Correções pontuais |
| `cursor/<descricao>-0b2d` | Trabalho de Cloud Agent (convenção EPA) |

## Merge

- **Squash merge** (configuração do repositório).
- **Delete branch on merge** habilitado.
- Sem merge direto em `main` por política de equipe (proteção GitHub pendente de plano — ver [seguranca.md](seguranca.md)).

## Force-push

Evitar force-push em `main`. Sem garantia técnica de bloqueio até rulesets elegíveis.

## Releases

Tags opcionais `v<semver>` alinhadas a `libraryVersion` em `catalog.json`.
