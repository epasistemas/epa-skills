# Arquitetura

## Propósito

`epa-skills` é a biblioteca **privada e comercial** de [Agent Skills](https://agentskills.io/specification) para operações de CRM EPA e fluxos relacionados a WhatsApp. O repositório é fonte de verdade para **conteúdo versionado**; a **ativação** no runtime do agente é um passo separado (ver [distribuicao.md](distribuicao.md)).

## Topologia

```text
epa-skills/
├── skills/<slug>/SKILL.md   # unidade distribuível
├── catalog.json             # índice agregado (opcional para runtimes)
├── docs/                    # políticas e manuais
├── scripts/                 # validação local/CI
└── .github/workflows/       # CI de PR
```

Cada skill é um diretório com `SKILL.md` obrigatório e, opcionalmente, `references/`, `scripts/` e `assets/` conforme a especificação.

## Fronteiras de acesso (futuro)

Hoje existe **um** repositório privado. A estratégia recomendada para **grupos com acesso distinto** não é sparse-checkout ou ACL por pasta (o GitHub não oferece isso), e sim **repositórios privados independentes** por fronteira:

| Fronteira (exemplo) | Conteúdo típico |
| ------------------- | --------------- |
| `epa-skills` (core) | skills genéricas CRM, políticas, validador |
| `epa-skills-whatsapp` | skills com maior sensibilidade operacional WA |
| `epa-skills-crm-visitas` | visitas, validação de campo |

O papel **Read** no GitHub permite clonar e copiar; revogar acesso **não apaga cópias** já extraídas. Planeje distribuição assumindo vazamento possível de cópias locais.

## Conta e organização

A conta `epasistemas` é **User** (sem organização GitHub listada). **Teams** do GitHub exigem organização; colaboradores externos recebem acesso **individual** ao repositório. Mantenedores concentram-se em `@epasistemas` via `CODEOWNERS` e permissões de repo até existir org Team.

## Skills de terceiros / plugin

Skills empacotadas em plugins de produtos (Cursor, Grok Bot, etc.) **não são propriedade** deste repositório para redistribuição automática. Este catálogo cobre apenas skills **originais** commitadas aqui.

## Compatibilidade com runtimes

Skills são **agnósticas de runtime** quando possível: descrevem processo, critérios de qualidade e limites de aprovação sem assumir que toda instalação expõe as mesmas ferramentas MCP. Matriz detalhada: [compatibilidade.md](compatibilidade.md).

## Proteção de branch

Branch padrão: **`main`** (obrigatório). Merge squash e exclusão da branch após merge já configurados no repositório.

**Proteção ativa** (required reviews, bloqueio de force-push via rulesets/API) retornou **403** sem GitHub Pro na conta User ou org Team. Isso **não foi contornado** e o repositório **permanece privado**. Ver [seguranca.md](seguranca.md).
