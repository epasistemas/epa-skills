# Contribuição

## Fluxo

1. Crie uma branch a partir de `main` (ex.: `feature/minha-skill` ou `cursor/descricao-0b2d` para agentes cloud).
2. Adicione ou altere conteúdo em `skills/<slug>/`.
3. Atualize `catalog.json` ao incluir ou remover skills.
4. Execute validação local: `python3 scripts/validate_skills.py` e `python3 -m unittest discover -s tests -p 'test_*.py'`.
5. Abra **pull request** para `main` **sem auto-merge**.
6. Um mantenedor **diferente do autor** revisa e aprova (política humana; o bot não substitui revisor independente).

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
