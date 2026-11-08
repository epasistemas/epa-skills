---
name: epa-crm-operacao-revisao
description: Prepara e revisa operações de CRM EPA (criação, atualização, follow-up) com checklist de consistência, riscos e aprovações. Use antes de executar mudanças em registros, pipelines ou tarefas, sem depender de API específica.
license: Proprietary. See repository LICENSE
metadata:
  author: epasistemas
  version: "0.1.0"
  domain: crm
  language: pt-BR
---

# Preparação e revisão de operações CRM

## Objetivo

Transformar um pedido vago em um **plano de operação CRM** revisável, com riscos explícitos e pontos de parada para aprovação.

## Entrada esperada

- Intenção do usuário (ex.: “mover lead para negociação”, “abrir tarefa de retorno”).
- Contexto disponível (IDs fictícios ou descrições; nunca exponha dados reais em logs públicos).
- Ferramentas que o agente **sabe** que tem nesta sessão (listar honestamente).

## Checklist de preparação

1. **Escopo** — qual objeto CRM (lead, conta, oportunidade, atividade)?
2. **Estado atual vs desejado** — descreva a transição.
3. **Pré-requisitos** — campos obrigatórios, estágios válidos, regras de negócio conhecidas.
4. **Efeitos colaterais** — notificações, SLAs, integrações (marcar “desconhecido” se incerto).
5. **Rollback conceitual** — como desfazer manualmente se a ferramenta permitir.
6. **Aprovação** — o que exige OK humano antes da execução.

## Modo revisão (pós-rascunho)

Compare o plano com:

- Duplicação acidental (mesmo registro, mesma ação duas vezes).
- Mudança de estágio sem motivo registrado.
- Datas incoerentes (follow-up no passado).
- Linguagem inadequada em notas visíveis ao cliente.

Produza lista **bloqueadores** vs **avisos**.

## Saída padrão

```markdown
## Operação proposta
(resumo em uma frase)

## Passos
1. ...
2. ...

## Riscos
- ...

## Aprovações necessárias
- ...

## Bloqueadores
- (vazio ou lista)
```

## Limites

- Não execute gravação em CRM sem aprovação explícita na conversa.
- Não invente integrações ou campos customizados — pergunte ou marque como gap.
