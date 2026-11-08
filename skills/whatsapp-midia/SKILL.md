---
name: whatsapp-midia
description: Analisa mídia recebida por transporte autorizado e produz transcrição ou resumo privado. Use para áudio, imagem ou documento anexo, sem publicar mídia na biblioteca.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.2.0"
  domain: whatsapp
  language: pt-BR
---

# Mídia WhatsApp

## Passos

1. Confirmar autorização, origem e arquivo; preferir download oficial do conector.
2. Não buscar caminho em servidor remoto nem extrair sessão. Links: validar domínio e tamanho; não acessar rede privada.
3. Temporário isolado; validar tipo e tamanho; não executar anexos.
4. Transcrever/descarregar conforme pedido; não base64 no contexto público.
5. Marcar incertezas; não inventar identidade ou fala ilegível.
6. Retenção mínima no privado; remover temporários sem apagar originais.

## Saída

Resumo ou transcrição com incertezas — sem anexo real na skill.

## Runtime

[Guardrails EPA](../../docs/runtime-guardrails.md) · [Privacidade](../../docs/privacidade.md)
