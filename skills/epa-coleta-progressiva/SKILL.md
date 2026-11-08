---
name: epa-coleta-progressiva
description: Conduz coleta conversacional progressiva para CRM EPA ou validação de visitas, uma informação por vez, com confirmação e resumo. Use em cadastros incompletos, formulários conversacionais ou confirmação antes de persistir, sem assumir canal específico.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.2.0"
  domain: crm
  language: pt-BR
---

# Coleta progressiva (CRM EPA)

## Objetivo

Obter campos **em etapas**, com confirmação e separação entre resposta recebida e inferência.

## Quando ativar

- Cadastro ou atualização incompleta.
- Dados fora de ordem; necessidade de validar entendimento antes de persistir.
- Coleta ligada a visitas (ocorreu? interesse? coordenação?).

## Passos

1. Definir objetivo, campos mínimos e contexto; não revelar dados de terceiros.
2. Uma pergunta principal por mensagem; opções fechadas quando úteis.
3. **Visita:** perguntar se ocorreu; se sim, interesse e atendimento da coordenação; se não, ação desejada — sem prometer remarcação automática.
4. Confirmar interpretação ambígua antes de avançar; observação livre é opcional.
5. Ausência de resposta **não** significa não ocorrência.
6. Resumo parcial a cada 3–5 campos ou ao mudar de seção.
7. Envio e cada follow-up exigem autorização explícita para destinatário e conteúdo; sem isso, entregar **rascunho**. Não criar rotina ou inscrição por conta própria.
8. Entregar respostas confirmadas ao fluxo CRM somente com autorização de gravação; não declarar registro antes de salvar/verificar.

## Saída

Próxima pergunta, ou resumo confirmado com lacunas no contexto privado do atendimento.

```markdown
## Resumo da coleta
- Campo: valor confirmado

## Pendências
- (se houver)

## Próximo passo
- Aguardar aprovação para registrar / encaminhar
```

## Edge cases

- Campo obrigatório recusado: explicar impacto; oferecer alternativa.
- Bloco único de respostas: confirmar apenas campos críticos.
- Abandono: oferecer retomada com resumo parcial.

## Limites

Não coleta senhas, tokens ou cartão. Não assume CRM ou WhatsApp disponíveis.

## Runtime

[Guardrails EPA](../../docs/runtime-guardrails.md) · [Privacidade](../../docs/privacidade.md)
