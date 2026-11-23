# STATUS · 12 demos de portfólio

Publicado em: https://pereira-gu.github.io/sites/demos/

## Decisão de processo
O Gustavo pediu para pular perguntas e a porta do plano em PDF: o briefing da tabela virou o plano aprovado.
Arquitetura enxuta para 12 sites: `shared/` (base.css, app.js, motion) + por demo `src/<slug>.html` (conteúdo) e `<slug>/tema.css` (tokens e estilo).
`python3 build.py` gera `<slug>/index.html` com cabeçalho, rodapé, SEO, WhatsApp fixo e aviso de demo. O índice `index.html` lista só as demos prontas.

## Feitas (5/12)
1. studio-bella-fios · galeria antes/depois
2. navalha-club · clube de assinatura
3. forno-da-vila · cardápio filtrável
4. patas-e-cia · calculadora por porte
5. clinica-lumiere · quiz de tratamento

## Faltam (7/12) — dados já estão em demos.py
6. auto-center-pistao · formulário de orçamento rápido (usar `data-wa-form`) · preto e amarelo, Archivo
7. doce-atelie-lu · monte seu bolo (usar `data-calc`) · rosa pastel, Lora + Quicksand
8. iron-fit · horários interativos (usar `{{HORARIOS}}` já pronto no build) · neon lima no escuro, Chakra Petch + Inter
9. sorriso-prime · antes/depois deslizante (usar `{{BA_DENTE_1}}` a `{{BA_DENTE_3}}` já prontos) · azul e branco, Plus Jakarta Sans
10. ink-raiz-tattoo · portfólio filtrável por estilo (`data-filter`, arte em CSS por estilo) · preto e branco, Syne + Space Grotesk
11. sabor-de-casa · cardápio semanal por dia (usar `{{CARDAPIO}}` já pronto, abre no dia de hoje) · verde e laranja, Bitter + Nunito
12. brilho-lar · simulador por cômodo (`data-calc` com inputs number `data-unit`) · azul-claro, Outfit

## Regras que valem para todas
- pt-BR, sem lorem ipsum; preços, avaliações e números com selo `<span class="ficticio">`.
- Rodapé com "Site demonstrativo — negócio fictício" (o build já coloca).
- `noindex` nas demos: negócio fictício não deve aparecer no Google como se fosse real.
- Sem fotos de terceiros: arte em CSS/SVG. Nada de São Paulo/SP nos textos.

## Componentes prontos (shared/app.js)
`data-wa="msg"` link de WhatsApp · `data-filter="#alvo"` + itens `data-cat` · abas `role=tablist` (`data-today`) · `.ba` antes/depois · `data-calc` (data-price soma, data-mult multiplica, data-flat soma no fim, number com data-unit; `data-total`, `data-summary`, `data-calc-wa`) · `data-wa-form` (form vira mensagem).
