# Matriz de compatibilidade

Versão da biblioteca: **0.2.0** (`catalog.json`).

Legenda:

- **Suportado**: fluxo documentado e validado neste repo.
- **Assistido**: requer passos manuais; sem garantia de sync automático.
- **Experimental**: depende de feature do produto.

| Runtime / produto | Leitura spec Agent Skills | Validação local | Ativação privada | `allowed-tools` | Observação |
| ----------------- | ------------------------- | --------------- | ---------------- | --------------- | ---------- |
| Cursor Agent (skills path) | Suportado | Suportado (`validate_skills.py`) | Assistido (cópia/symlink) | Experimental | Não assumir MCPs idênticos entre máquinas |
| Grok Bot | Suportado | Assistido | Assistido (Connect / Private skills) | Experimental | Ver [distribuicao.md](distribuicao.md); computador compartilhado entre Bots |
| Agent SDK / hosted | Suportado | Suportado | Assistido | Experimental | Deploy separado do conteúdo Git |
| Forks públicos | N/A | N/A | **Proibido** para este repo | N/A | Repo permanece privado |

## Compatibilidade por skill (0.2.0)

Todas as skills listadas em `catalog.json`: rede opcional conforme conector do runtime; **nenhuma** ferramenta MCP/API obrigatória; dados reais apenas no contexto privado de execução.

Slugs **aposentados** (conteúdo fundido): `epa-crm-operacao-revisao` → `epa-crm-operacoes`; `epa-crm-conhecimento-mapeamento` → `epa-crm-mapa`; `epa-wa-operacao-revisao` → `whatsapp-operacoes`.

## Política de versão

- **Patch**: correções de texto, exemplos, links.
- **Minor**: nova skill ou conteúdo retrocompatível em skill existente.
- **Major**: remoção/renomeação de skill ou mudança de contrato semântico (campos obrigatórios, comportamento esperado pelo time).

Atualize `CHANGELOG.md` e `catalog.json` em mudanças minor/major da biblioteca.
