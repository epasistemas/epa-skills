# Matriz de compatibilidade

Versão da biblioteca: **0.1.0** (`catalog.json`).

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

## Compatibilidade por skill (0.1.0)

| Skill (`name`) | Rede | Dados externos | Ferramentas específicas |
| -------------- | ---- | -------------- | ----------------------- |
| `epa-coleta-progressiva` | Opcional | Não exige | Nenhuma obrigatória |
| `epa-crm-operacao-revisao` | Opcional | Não exige | Nenhuma obrigatória |
| `epa-crm-conhecimento-mapeamento` | Opcional | Não exige | Nenhuma obrigatória |
| `epa-wa-operacao-revisao` | Opcional | Não exige | Nenhuma obrigatória |

## Política de versão

- **Patch**: correções de texto, exemplos, links.
- **Minor**: nova skill ou conteúdo retrocompatível em skill existente.
- **Major**: remoção/renomeação de skill ou mudança de contrato semântico (campos obrigatórios, comportamento esperado pelo time).

Atualize `CHANGELOG.md` e `catalog.json` em mudanças minor/major da biblioteca.
