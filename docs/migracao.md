# Checklist de migração (sanitização)

**Status:** pacote sanitizado de **10 skills** integrado na PR (reescritas genéricas). Continua valendo revisão humana por commit; não equivale a teste em CRM/Drive/WhatsApp real. Agentes **não** devem buscar fontes legadas fora do repositório.

Use este checklist ao **importar** skills de ambientes internos (inventário candidato: `wa-bot-ops`, `epa-browser-ops`, `epa-mapa`, `crm-knowledge-map`, `epa-coleta-conversacional`, `epa-visitas-ops`, `epa-visitas-validacao`, `epa-wa-*`, onboarding, etc.). **Não** buscar nem commitar arquivos de origem não entregues neste repositório.

## Antes de copiar conteúdo

- [ ] Remover `contatos.md`, `tenants.md`, históricos de chat e exports de CRM.
- [ ] Substituir URLs internas por `example.invalid` ou descrição genérica.
- [ ] Remover JWT, Bearer, API keys e IDs de tenant reais.
- [ ] Unificar slugs duplicados (ex.: `epa-visitas-validacao` vs `epa-visitas-valida-o`).
- [ ] Confirmar que o texto não viola termos de skills de **plugin** de terceiros (não redistribuir).

## Adaptação ao formato EPA

- [ ] Criar `skills/<slug>/SKILL.md` com `name` = `<slug>`.
- [ ] Preencher `description` com gatilhos de uso (português ou inglês técnico, consistente).
- [ ] Definir `metadata.version` inicial `0.1.0`.
- [ ] Mover referências longas para `references/` com links relativos.
- [ ] Registrar em `catalog.json`.
- [ ] Rodar `python3 scripts/validate_skills.py` e testes.

## Revisão de segurança

- [ ] Revisor diferente do autor da PR.
- [ ] Passar `scripts/scan_secrets.py` sem achados reais.
- [ ] Confirmar ausência de PII em exemplos.

## Ativação

- [ ] Documentar no PR qual runtime receberá a skill.
- [ ] Teste com dados **fictícios** apenas.

## O que não migrar automaticamente

Skills gerenciadas por marketplace/plugin do produto permanecem lá; este repo guarda apenas conteúdo **original** ou **reescrito** com direitos claros.
