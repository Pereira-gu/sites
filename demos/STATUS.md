# STATUS · 12 demos de portfólio

Publicado em: https://pereira-gu.github.io/sites/demos/

## Decisão de processo
O Gustavo pediu para pular perguntas e a porta do plano em PDF: o briefing da tabela virou o plano aprovado.
Arquitetura enxuta para 12 sites: `shared/` (base.css, app.js, motion) + por demo `src/<slug>.html` (conteúdo) e `<slug>/tema.css` (tokens e estilo).
`python3 build.py` gera `<slug>/index.html` com cabeçalho, rodapé, SEO, WhatsApp fixo e aviso de demo. O índice `index.html` lista só as demos prontas.

## Feitas (12/12) — publicadas
1. studio-bella-fios · galeria antes/depois
2. navalha-club · clube de assinatura
3. forno-da-vila · cardápio filtrável
4. patas-e-cia · calculadora por porte
5. clinica-lumiere · quiz de tratamento
6. auto-center-pistao · orçamento rápido (formulário vira mensagem de WhatsApp)
7. doce-atelie-lu · monte seu bolo
8. iron-fit · grade de horários por dia + filtro por modalidade
9. sorriso-prime · antes/depois deslizante
10. ink-raiz-tattoo · portfólio filtrável por estilo
11. sabor-de-casa · cardápio semanal (abre no dia de hoje)
12. brilho-lar · simulador de preço por cômodo

Testado: 390 px e 1280 px sem rolagem lateral nem erros; calculadoras, filtros, abas e formulário conferidos.

## Próximos passos possíveis
- Trocar as ilustrações por fotos reais com licença livre (anotar no CREDITOS.md).
- Linkar a página demos/ na página de serviços.

## Regras que valem para todas
- pt-BR, sem lorem ipsum; preços, avaliações e números com selo `<span class="ficticio">`.
- Rodapé com "Site demonstrativo — negócio fictício" (o build já coloca).
- `noindex` nas demos: negócio fictício não deve aparecer no Google como se fosse real.
- Sem fotos de terceiros: arte em CSS/SVG. Nada de São Paulo/SP nos textos.

## Componentes prontos (shared/app.js)
`data-wa="msg"` link de WhatsApp · `data-filter="#alvo"` + itens `data-cat` · abas `role=tablist` (`data-today`) · `.ba` antes/depois · `data-calc` (data-price soma, data-mult multiplica, data-flat soma no fim, number com data-unit; `data-total`, `data-summary`, `data-calc-wa`) · `data-wa-form` (form vira mensagem).
