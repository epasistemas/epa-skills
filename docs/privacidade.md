# Política de privacidade do conteúdo

Política **central e mandatória** para toda contribuição, revisão e operação neste repositório.

## Proibido (não negociável)

- Dados pessoais ou de cliente (nomes reais, endereços, documentos).
- Contatos: telefone, e-mail pessoal, JID WhatsApp (`@s.whatsapp.net`, `@c.us`, etc.).
- Nome de titular de WhatsApp pessoal, instância, tenant, URLs privadas, históricos de conversa.
- Credenciais (tokens, JWT, chaves PEM, PAT).
- Configuração **por cliente** (deve ficar **fora** desta biblioteca, em repo/env dedicado).

Skills de WhatsApp aqui são **fluxo genérico** apenas — sem referência a pessoas reais (incluindo mantenedores).

## Dados públicos (exceção estreita)

Só inclua dados publicamente acessíveis quando **todos** forem verdadeiros:

1. Realmente públicos e verificáveis.
2. Relevantes ao texto técnico.
3. Sem segredo embutido e sem PII desnecessária.
4. Com **fonte** e **licença/uso** citados no mesmo PR.

Registrar exceção em `scripts/privacy_allowlist.json` (caminho, linha, regra, justificativa). **Não** use allowlist ampla por arquivo inteiro.

O fato de um dado ter sido publicado antes **não** autoriza PII neste repo privado.

## Exemplos sintéticos

- Marcar claramente: prefixo `SINTÉTICO`, `SYNTHETIC`, ou bloco «exemplo fictício».
- Domínios: preferir `example.invalid`, `example.com`, `example.org`.
- IDs: `00000000-0000-0000-0000-000000000099` ou valores obviamente fictícios.
- Nunca copiar exports (`contatos.md`, `tenants.md`, históricos) mesmo “anonimizados parcialmente”.

## Revisão humana obrigatória

Checks em `scripts/scan_policy.py` são **heurísticos**. Não substituem:

- Leitura do diff completo (skills, `catalog.json`, docs, workflows, scripts).
- Julgamento do revisor sobre contexto e exceções públicas.

## CI

O scanner roda na CI **apenas** para PRs cujo head está no mesmo repositório (sem executar código de fork). Ver [seguranca.md](seguranca.md).

## Migração futura

Pacotes sanitizados de skills CRM/Drive/WhatsApp serão anexados pelo mantenedor. Até lá, **não** declarar migração concluída. Agentes não devem buscar fontes legadas em outros ambientes.
