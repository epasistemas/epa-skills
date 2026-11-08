# Edição paralela e concorrência

Várias IDEs ou agentes podem editar o mesmo branch (ex.: PR #1). Este protocolo **reduz** corrida; **não elimina** conflitos.

## Antes de `pull` / `commit` / `push` (ou ao retomar trabalho)

1. Confirmar branch atual e upstream: `git branch -vv`.
2. `git status` — working tree limpo ou mudanças intencionais.
3. `git fetch origin main <sua-branch>`.
4. Comparar SHAs e ahead/behind:
   - `git rev-parse HEAD` vs `git rev-parse origin/<branch>`.
   - `git rev-list --left-right --count origin/<branch>...HEAD`.
   - `git log HEAD..origin/<branch> --oneline` (commits remotos que você não tem).
5. Ler diffs/commits remotos novos **antes** de continuar.

Script auxiliar (não substitui julgamento):

```bash
./scripts/git_concurrency_check.sh
```

## Revalidação antes de `push`

```bash
python3 scripts/validate_skills.py
python3 scripts/scan_policy.py
python3 -m unittest discover -s tests -p 'test_*.py' -q
./scripts/git_concurrency_check.sh
```

## Proibido para evitar apagar trabalho alheio

- `git reset --hard` para “resolver” concorrência.
- `git push --force` / `--force-with-lease` (salvo ordem explícita do mantenedor).
- `git commit --amend` ou rebase de commits **já publicados** no remoto.
- Descartar arquivos modificados sem ler o diff (incluindo mudanças da outra IDE).

## Integração de mudanças remotas

- Preferir `git pull --no-rebase origin <branch>` (merge) ou `git merge origin/<branch>` após fetch.
- Se houver conflito com impacto em política, skills ou CI: **parar**, documentar arquivos em conflito e pedir resolução humana — não escolher lados arbitrariamente em conteúdo sensível.

## Branch principal

`main` permanece a branch principal; trabalho de PR em branch dedicada até merge aprovado por revisor ≠ autor.
