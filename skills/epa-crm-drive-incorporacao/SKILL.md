---
name: epa-crm-drive-incorporacao
description: Prepara vinculação autorizada entre recursos documentais Drive e o módulo Drives do CRM EPA. Use antes de criar ou atualizar vínculos, sem supor compartilhamento ampliado.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.2.0"
  domain: crm
  language: pt-BR
---

# CRM ↔ Drive (incorporação)

## Entradas

Contexto CRM, recurso documental autorizado, entidade-alvo e operação pretendida. Nem todo arquivo acessível pode ser compartilhado.

## Passos

1. Confirmar acesso CRM e Drive pelos conectores suportados.
2. No CRM, módulo estrutural `/admin/crm/drives-incorporadoras` — não inventar esquema.
3. Confirmar entidade-alvo e tipo de vínculo (referência, pasta, etc.); sem identificadores reais na skill.
4. Conferir permissões e visibilidade via CRM; se modelo incerto, **parar**.
5. Apresentar alteração e confirmar se ainda não autorizada; só o vínculo solicitado.
6. Reabrir vínculo com acesso autorizado; não testar com credencial de terceiro.

## Saída

Resultado da vinculação e limites de acesso conhecidos — sem dados documentais no artefato compartilhado. Sem promessa de sync automático.

## Runtime

[Guardrails EPA](../../docs/runtime-guardrails.md) · [Privacidade](../../docs/privacidade.md)
