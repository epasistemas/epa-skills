# Contribuição

## Fluxo

1. Crie uma branch a partir de `main` (ex.: `feature/minha-skill` ou `cursor/descricao-0b2d` para agentes cloud).
2. Adicione ou altere conteúdo em `skills/<slug>/`.
3. Atualize `catalog.json` ao incluir ou remover skills.
4. Leia [privacidade.md](privacidade.md) — sem PII/contato/JID/tenant/URL privada/credencial; config por cliente **fora** do repo.
5. Execute `./scripts/pre_push.sh` (ou validação equivalente).
6. Revisar o **diff inteiro** (catálogo, docs, CI, scripts), não apenas skills.
7. Abra **pull request** para `main` **sem auto-merge**.
8. Um mantenedor **diferente do autor** revisa e aprova (política humana; o bot não substitui revisor independente).

## Edição paralela (várias IDEs)

Siga [concorrencia.md](concorrencia.md) antes de cada push. O protocolo **não elimina** corrida. Proibido: `reset --hard`, force-push, amend/rebase de commits já no remoto sem acordo explícito.

## Modelo de pull request

Use o template em `.github/pull_request_template.md`.

## Autor não aprova a própria PR

Quem abre a PR **não deve** aprovar ou fazer merge da própria alteração. Em trabalho assistido por bot com identidade do mantenedor, outro humano com permissão de escrita deve revisar.

## Convenção de skills

- Diretório: `skills/<slug>/` onde `<slug>` é igual ao campo `name` do frontmatter.
- `name`: minúsculas, hífens, 1–64 caracteres, sem `--`, sem hífen inicial/final ([spec](https://agentskills.io/specification)).
- `description`: clara, com gatilhos de quando usar (até 1024 caracteres).
- `metadata.version`: semver da skill (recomendado).
- Links para outros arquivos: **caminhos relativos** a partir da raiz da skill.

## Escopo aceitável

- Skills **genéricas**, sem URLs internas, tokens, contatos ou tenants reais.
- Sem duplicar políticas de plataforma (aprovação de envio, conformidade WhatsApp Meta, etc.): referencie limites e remeta aprovação humana.

## Escopo rejeitável

- Dados pessoais, credenciais, históricos exportados de produção.
- Cópia de skills proprietárias de marketplaces/plugins.
- Dependência obrigatória de ferramentas não documentadas no próprio skill.

## Migração de skills existentes

Há candidatos internos (nomes como `wa-bot-ops`, `epa-visitas-*`, etc.) que podem conter material sensível. Use o [checklist de migração](migracao.md); **não** commitar arquivos de origem sem sanitização.
