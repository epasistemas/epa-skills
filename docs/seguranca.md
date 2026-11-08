# Segurança e governança

## Privacidade do repositório

- O repositório **deve permanecer privado**.
- Não tornar público para contornar limites de API (rulesets/proteções).
- Não adicionar convidados, criar orgs/repos extras, comprar plano, nem publicar template/pacote público sem decisão explícita do mantenedor.

## Proteção de `main` — pendência documentada

Consultas a proteções/rulesets via API retornaram **403** na conta User sem GitHub Pro.

| Recurso | Estado atual | Desbloqueio |
| ------- | ------------ | ----------- |
| Branch protection rules | Não configurável via API | GitHub Pro (conta) **ou** org com plano Team |
| Rulesets | 403 upgrade | Idem |
| Privacidade | Privado | Mantido |

**Não prometemos** proteção ativa nem bloqueio de force-push até upgrade ou configuração manual elegível no plano. Práticas compensatórias:

- Política de merge apenas por PR (disciplina de equipe).
- CI obrigatória antes do merge (ver workflow).
- Revisão humana cruzada (autor ≠ aprovador).

## CODEOWNERS e permissões

- `CODEOWNERS` solicita revisão; **não é ACL**.
- Permissões são **por repositório**; não há isolamento por pasta, branch ou sparse-checkout.
- Mantenedores centrais: `@epasistemas` (ver `/CODEOWNERS`).

## Distribuição e vazamento

- Permissão **Read** permite clonar e copiar todo o histórico.
- Revogar acesso **não remove** clones locais ou forks privados já criados.
- Skills com maior sensibilidade devem migrar para repos privados dedicados no futuro.

## CI e forks

O workflow de validação:

- Dispara em `pull_request` no mesmo repositório.
- **Não usa** `pull_request_target` para executar código de forks (evita RCE por PR malicioso).
- PRs de fork externo: validação local exigida pelo revisor; CI pode não rodar com o mesmo trust model.

Permissões mínimas: `contents: read` (ver workflow).

## Detecção de segredos — limitações

A CI pode varrer padrões comuns (ver `scripts/scan_secrets.py`). **Limitações:**

- Não detecta segredos codificados de forma customizada ou em imagens.
- Falsos positivos em exemplos de documentação são possíveis — use apenas placeholders sintéticos.
- Não substitui revisão humana nem scanners corporativos.

Exemplos **permitidos** em docs (sintéticos):

```text
Bearer SYNTHETIC_TOKEN_EXAMPLE_A1B2C3
https://internal.example.invalid/api/v1
tenant-id: 00000000-0000-0000-0000-000000000099
```

**Proibido:** colar tokens, JWT, URLs de produção ou exports de `contatos.md` / `tenants.md`.

## Bots e identidade

Agentes automatizados podem abrir PR com a identidade do mantenedor; isso **não** dispensa segunda revisão humana para merge.

## Revisão jurídica

`LICENSE` é conservadora e não define pessoa jurídica. Contratos com clientes, termos de uso e DPA devem ser revisados por assessoria jurídica antes de uso comercial em escala.
