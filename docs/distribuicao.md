# Distribuição e instalação

## Conceitos

| Etapa | O que é |
| ----- | ------- |
| **Download** | Obter arquivos (clone, sparse checkout, cópia de release interna) |
| **Ativação** | Runtime passa a carregar metadata/instruções da skill |

Não há documentação oficial verificada de **sincronização automática GitHub → Grok Bot** para repositórios privados. Trate a integração como **importação assistida** até existir conector suportado.

Referências úteis (comportamento pode variar por produto):

- [Agent Skills specification](https://agentskills.io/specification)
- [Work with Grok Bot — Skills](https://cursor.com/docs/grok-bot/work.md) (skills privadas via Connect apps / habilitação por Bot)

**Não use** exportações de template público que possam tornar o conteúdo visível fora do perímetro privado.

## Grupos de acesso

Hoje: um repo privado; colaboradores com permissão individual no GitHub.

Futuro: repos separados por grupo (core, whatsapp, visitas). Times GitHub exigem **organização**; até lá, use listas de acesso manual e processos de onboarding documentados internamente.

## Instalação por runtime (assistida)

### Cursor / IDE com skills em disco

1. Clone (SSH ou HTTPS com token pessoal de escopo mínimo):

   ```bash
   git clone git@github.com:epasistemas/epa-skills.git
   ```

2. Copie ou vincule skills desejadas para o caminho de skills do produto (conforme documentação local do cliente — tipicamente diretório de skills do usuário ou do projeto).

3. Valide antes de ativar:

   ```bash
   cd epa-skills && python3 scripts/validate_skills.py
   ```

4. Reinicie ou recarregue o agente para incluir metadata (`name`, `description`) no catálogo.

### Grok Bot

1. Garanta que o Bot tem acesso ao repositório (conta com permissão de leitura no repo privado).
2. **Download:** clone ou sincronize `skills/<slug>/` para área persistente do ambiente (`/workspace` no computador compartilhado do Bot, em subpasta acordada, ex. `epa-skills/`).
3. **Ativação:** em Connect apps / Private skills, habilite a skill para o Bot específico (ver doc do produto). Pedir ao Bot para usar a skill **pelo `name`** do frontmatter.
4. Confirme em um chat de teste com entrada fictícia; não use dados de clientes reais no primeiro teste.

### Outros agentes (genérico)

1. Liste skills via `catalog.json`.
2. Para cada skill ativada, exponha `SKILL.md` ao mecanismo de progressive disclosure do agente (metadata global, corpo sob demanda).
3. Ferramentas (`allowed-tools`) são experimentais; não presuma suporte.

## Versionamento

- Biblioteca: `libraryVersion` em `catalog.json` + entradas em `CHANGELOG.md`.
- Skill: `metadata.version` no frontmatter de cada `SKILL.md`.
- Releases GitHub (tags) são opcionais; tags `v*` podem referenciar `libraryVersion`.

## Atualizações

1. `git pull` na branch `main` (ou checkout da tag acordada).
2. Reexecute o validador.
3. Reative ou recarregue skills no runtime.
4. Se uma skill mudou de forma incompatível (semver major), atualize runtimes dependentes de forma coordenada (ver [compatibilidade.md](compatibilidade.md)).
