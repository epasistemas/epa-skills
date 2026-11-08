---
name: whatsapp-onboarding
description: Configura com segurança o contexto de um novo agente WhatsApp sem dados pessoais na biblioteca. Use na primeira conexão ou revisão de limites antes de envio ou escuta.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.2.0"
  domain: whatsapp
  language: pt-BR
---

# Onboarding WhatsApp

## Passos

1. Explicar capacidades e limites; pessoal vs comercial; onde ficam dados operacionais privados.
2. Fluxo oficial de conexão do runtime — sem segredo em chat comum.
3. Verificar conector e escopo com consulta não mutante.
4. Falha de autenticação: parar e reconectar; não gravar segredo em arquivo.
5. Políticas de envio, destinatários permitidos e retenção mínima.
6. Início com leitura ou rascunho; sem mensagem, webhook ou inscrição sem autorização explícita.

## Saída

Checklist de prontidão e pendências — sem credenciais nem identidade pessoal.

## Runtime

[Guardrails EPA](../../docs/runtime-guardrails.md) · [Privacidade](../../docs/privacidade.md)
