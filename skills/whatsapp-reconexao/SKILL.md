---
name: whatsapp-reconexao
description: Confere e reconecta uma instância WhatsApp (Evolution via MCP) preservando nome e token, guiando a pessoa pelo código no celular ou pelo QR em outra tela, com acompanhamento finito. Use quando pedirem para conectar, reconectar, gerar QR ou ver se o WhatsApp do robô está ligado.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.3.0"
  domain: whatsapp
  language: pt-BR
---

# Reconexão WhatsApp (MCP Evolution)

O celular do dono manda: a integração é só um aparelho conectado nele, como o WhatsApp Web. Esta skill guia a pessoa;
quem pareia é ela, com o celular na mão.

## Regras

- Usar só a instância já fixada no conector. Nunca criar, apagar, renomear nem trocar token.
- Nunca usar `restart_instance`, `set_webhook` ou `set_settings` para reconectar. Restart reaproveita a sessão antiga e
  não conserta sessão quebrada; webhook e settings derrubam as integrações que dependem da instância.
- Não mandar mensagem de teste, não marcar como lido, não mexer em grupos nem em perfil.
- Não mostrar token, JWT, conteúdo bruto do QR nem número completo. Número sempre mascarado (ex.: `55 •• •••• 1234`).
- Sem script, timer ou rotina própria para acompanhar o QR: o acompanhamento é do servidor do MCP ou sob demanda.

## 1. Estado

Use `instance_status` se o conector tiver; senão `connection_state`.

| Estado | Significa | Próximo passo |
| ------ | --------- | ------------- |
| `open` | Conectado | Informar e parar. Se a pessoa diz que não recebe mensagens, explicar que precisa de logout e novo pareamento e pedir confirmação |
| `connecting` | Pareamento em andamento | Seguir para o passo 3 sem logout |
| `close` | Desconectado; a sessão já caiu | Seguir para o passo 2 **sem logout** |
| erro ou timeout | Não confirmado | Dizer que não foi possível consultar; não tratar como `close` |

## 2. Antes de parear

1. Confirmar que a pessoa está com o celular do número e consegue concluir nos próximos 3 minutos.
2. Pedir que, no celular, em **WhatsApp › Aparelhos conectados**, remova só o aparelho antigo desta integração, se
   ainda aparecer. Nunca os outros aparelhos (WhatsApp Web pessoal etc.).
3. Logout (`logout_instance`) só com estado `open` **e** confirmação explícita da pessoa. Se a resposta disser que já
   estava desconectada, seguir sem insistir.

## 3. Código ou QR

Pergunte: "Você tem outra tela (computador ou outro celular) para mostrar o QR, ou só este celular?"

| Situação | Como parear |
| -------- | ----------- |
| Só o celular | **Código de 8 caracteres**: `pairing_start` com modo `codigo`. Instrução: Aparelhos conectados › Conectar um aparelho › Conectar com número de telefone › digitar o código. Se o conector não oferecer código, dizer que hoje só dá pelo QR em outra tela |
| Outra tela, conector com link | `pairing_start` com modo `link`: mandar o link **uma vez**; a página mostra o QR ao vivo e avisa quando conectar |
| Outra tela, sem link | `get_qr` e mostrar a imagem para escanear da outra tela |

- Nunca mandar o QR para o mesmo número que vai escanear: ninguém escaneia a própria tela.
- Campo `pairingCode`: só é código se tiver 8 letras/números. Texto longo é o conteúdo do QR; não mostrar.
- O QR do WhatsApp troca em menos de 1 minuto. Validade exata não é informada; se não der tempo, peça outro.

## 4. Acompanhar até o fim (finito)

- **Com `pairing_wait`:** chamar com o último `seq` até receber `fim`. Mostrar só QR novo e mudança de estado. O
  servidor encerra em no máximo 180 s; não abrir outra sessão sozinho.
- **Sem `pairing_wait`:** conferir o estado quando a pessoa disser que escaneou ou pedir QR novo. QR novo só se ela
  pedir ou o anterior não funcionar; no máximo 5 QRs e 3 minutos por tentativa; nunca reenviar imagem igual.

## 5. Conferir e encerrar

- Só dizer "conectado" ao ver `open`.
- Conferir o número com `instance_status` quando existir:
  - igual ao esperado: confirmar conexão e número (mascarado);
  - diferente: "Foi conectado um número diferente do esperado." Parar, sem logout automático, e chamar o responsável;
  - sem como conferir: "Conectado, mas o número não foi conferido."
- Fechar com os dois lembretes: celular sempre ligado e com internet; nunca remover o aparelho da integração em
  Aparelhos conectados.

## Runtime

[Guardrails EPA](../../docs/runtime-guardrails.md) · [Privacidade](../../docs/privacidade.md)
