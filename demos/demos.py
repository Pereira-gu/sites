"""Briefing condensado das 12 demos (dados fictícios). Cada demo tem src/<slug>.html e <slug>/tema.css."""

def H(*dias):
    return list(dias)

DEMOS = [
 dict(slug="studio-bella-fios", name="Studio Bella Fios", brand="Bella <span>Fios</span>", nicho="Salão de beleza",
      bairro="Savassi", cidade="Belo Horizonte", uf="MG", rua="Rua Antônio de Albuquerque, 412 — sala 3",
      title="Studio Bella Fios · Salão de beleza na Savassi, BH (demo)",
      desc="Salão de beleza na Savassi, em Belo Horizonte: corte, coloração, mechas e tratamentos com hora marcada. Agende pelo WhatsApp.",
      cor="#8C6A35", fav_fg="#FBF6F1", fonts="family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@400;500;600;700",
      schema="BeautySalon", insta="studiobellafios", cta="Agendar horário",
      wa="Olá! Vi o site do Studio Bella Fios e quero agendar um horário.",
      horas=H("Ter a sex: 9h às 20h", "Sábado: 8h às 17h", "Dom e seg: fechado"), horas_schema=["Tu-Fr 09:00-20:00", "Sa 08:00-17:00"],
      nav=[("servicos", "Serviços"), ("galeria", "Antes e depois"), ("equipe", "Equipe"), ("localizacao", "Onde estamos")]),
 dict(slug="navalha-club", name="Navalha Club", brand="Navalha<span>.</span>Club", nicho="Barbearia",
      bairro="Centro", cidade="Curitiba", uf="PR", rua="Rua Riachuelo, 233",
      title="Navalha Club · Barbearia no Centro de Curitiba com clube de assinatura (demo)",
      desc="Barbearia no Centro de Curitiba: corte, barba e plano mensal com cortes ilimitados. Marque seu corte pelo WhatsApp.",
      cor="#141210", fav_fg="#C8963E", fav_font="Impact", fonts="family=Bebas+Neue&family=Barlow:wght@400;500;600;700",
      schema="HairSalon", insta="navalhaclub", cta="Marcar corte",
      wa="Fala! Vi o site da Navalha Club e quero marcar um corte.",
      horas=H("Seg a sex: 9h às 21h", "Sábado: 8h às 18h"), horas_schema=["Mo-Fr 09:00-21:00", "Sa 08:00-18:00"],
      nav=[("cortes", "Cortes"), ("precos", "Preços"), ("barbeiros", "Barbeiros"), ("clube", "Clube")]),
 dict(slug="forno-da-vila", name="Forno da Vila", brand="Forno <span>da</span> Vila", nicho="Pizzaria",
      bairro="Cidade Baixa", cidade="Porto Alegre", uf="RS", rua="Rua da República, 518",
      title="Forno da Vila · Pizzaria a lenha na Cidade Baixa, Porto Alegre (demo)",
      desc="Pizzaria a lenha na Cidade Baixa, em Porto Alegre: massa de fermentação natural, combos e delivery. Peça pelo WhatsApp.",
      cor="#B3261E", fav_fg="#FBF3E4", fonts="family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Nunito+Sans:wght@400;600;700;800",
      schema="Restaurant", insta="fornodavila", cta="Pedir pelo WhatsApp",
      wa="Oi! Quero fazer um pedido no Forno da Vila.",
      horas=H("Ter a qui: 18h às 23h", "Sex e sáb: 18h à 0h", "Domingo: 18h às 23h"), horas_schema=["Tu-Th 18:00-23:00", "Fr-Sa 18:00-00:00", "Su 18:00-23:00"],
      nav=[("cardapio", "Cardápio"), ("combos", "Combos"), ("delivery", "Delivery"), ("horarios", "Horários")]),
 dict(slug="patas-e-cia", name="Patas & Cia", brand="Patas <span>&amp;</span> Cia", nicho="Pet shop, banho e tosa",
      bairro="Pituba", cidade="Salvador", uf="BA", rua="Rua Paraíba, 190",
      title="Patas & Cia · Banho e tosa na Pituba, Salvador (demo)",
      desc="Banho e tosa na Pituba, em Salvador, com leva-e-traz. Calcule o preço pelo porte do seu pet e agende pelo WhatsApp.",
      cor="#6A35D9", fav_fg="#FFC93C", fonts="family=Baloo+2:wght@600;700;800&family=Nunito:wght@400;600;700;800",
      schema="PetStore", insta="patasecia", cta="Agendar banho",
      wa="Oi! Quero agendar um banho na Patas & Cia.",
      horas=H("Seg a sex: 8h às 18h", "Sábado: 8h às 14h"), horas_schema=["Mo-Fr 08:00-18:00", "Sa 08:00-14:00"],
      nav=[("servicos", "Serviços"), ("calculadora", "Calcular preço"), ("pacotes", "Pacotes"), ("duvidas", "Dúvidas")]),
 dict(slug="clinica-lumiere", name="Clínica Lumière", brand="Lumière", nicho="Estética facial",
      bairro="Meireles", cidade="Fortaleza", uf="CE", rua="Av. Desembargador Moreira, 1020 — sala 704",
      title="Clínica Lumière · Estética facial no Meireles, Fortaleza (demo)",
      desc="Estética facial no Meireles, em Fortaleza: limpeza de pele, peeling, microagulhamento e LED. Faça o quiz e marque sua avaliação gratuita.",
      cor="#4F6B55", fav_fg="#FFFFFF", fonts="family=Marcellus&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700",
      schema="HealthAndBeautyBusiness", insta="clinicalumiere", cta="Avaliação gratuita",
      wa="Olá! Gostaria de marcar uma avaliação gratuita na Clínica Lumière.",
      horas=H("Seg a sex: 9h às 19h", "Sábado: 9h às 13h"), horas_schema=["Mo-Fr 09:00-19:00", "Sa 09:00-13:00"],
      nav=[("tratamentos", "Tratamentos"), ("quiz", "Qual é pra mim?"), ("especialista", "Especialista"), ("duvidas", "Dúvidas")]),
 dict(slug="auto-center-pistao", name="Auto Center Pistão", brand="PISTÃO<span>/</span>auto", nicho="Oficina mecânica",
      bairro="Setor Pedro Ludovico", cidade="Goiânia", uf="GO", rua="Av. Quinta Radial, 840",
      title="Auto Center Pistão · Oficina mecânica no Pedro Ludovico, Goiânia (demo)",
      desc="Oficina mecânica em Goiânia: revisão, freios, suspensão, injeção e ar-condicionado com garantia. Peça orçamento rápido pelo WhatsApp.",
      cor="#FFC20E", fav_fg="#111111", fav_font="Arial Black", fonts="family=Archivo:wght@400;500;700;800;900",
      schema="AutoRepair", insta="autocenterpistao", cta="Pedir orçamento",
      wa="Olá! Quero um orçamento no Auto Center Pistão.",
      horas=H("Seg a sex: 7h30 às 18h", "Sábado: 7h30 às 12h"), horas_schema=["Mo-Fr 07:30-18:00", "Sa 07:30-12:00"],
      nav=[("servicos", "Serviços"), ("marcas", "Marcas"), ("garantia", "Garantia"), ("orcamento", "Orçamento")]),
 dict(slug="doce-atelie-lu", name="Doce Ateliê Lu", brand="Doce Ateliê <span>Lu</span>", nicho="Confeitaria",
      bairro="Boa Viagem", cidade="Recife", uf="PE", rua="Rua Ribeiro de Brito, 655",
      title="Doce Ateliê Lu · Bolos e encomendas em Boa Viagem, Recife (demo)",
      desc="Confeitaria em Boa Viagem, Recife: bolos de festa, docinhos e encomendas. Monte seu bolo no site e encomende pelo WhatsApp.",
      cor="#B0405F", fav_fg="#FFF5F7", fonts="family=Lora:ital,wght@0,500;0,600;1,500&family=Quicksand:wght@400;500;600;700",
      schema="Bakery", insta="doceatelielu", cta="Encomendar",
      wa="Oi, Lu! Vi o site e quero fazer uma encomenda.",
      horas=H("Ter a sáb: 9h às 19h", "Retiradas com hora marcada"), horas_schema=["Tu-Sa 09:00-19:00"],
      nav=[("bolos", "Bolos"), ("monte", "Monte seu bolo"), ("festas", "Festas"), ("encomendas", "Como encomendar")]),
 dict(slug="iron-fit", name="Iron Fit", brand="IRON<span>FIT</span>", nicho="Academia",
      bairro="Asa Sul", cidade="Brasília", uf="DF", rua="SCLS 410, Bloco C, loja 12",
      title="Iron Fit · Academia na Asa Sul, Brasília (demo)",
      desc="Academia na Asa Sul, em Brasília: musculação, funcional, spinning, HIIT, muay thai e yoga. Veja os horários e marque uma aula experimental.",
      cor="#0B0D12", fav_fg="#C6FF00", fav_font="Arial Black", fonts="family=Chakra+Petch:wght@600;700&family=Inter:wght@400;500;600;700",
      schema="ExerciseGym", insta="ironfit", cta="Aula experimental",
      wa="Fala! Quero marcar uma aula experimental na Iron Fit.",
      horas=H("Seg a sex: 5h às 23h", "Sábado: 7h às 14h", "Domingo: 8h às 12h"), horas_schema=["Mo-Fr 05:00-23:00", "Sa 07:00-14:00", "Su 08:00-12:00"],
      nav=[("modalidades", "Modalidades"), ("planos", "Planos"), ("horarios", "Horários"), ("professores", "Professores")]),
 dict(slug="sorriso-prime", name="Sorriso Prime", brand="Sorriso <span>Prime</span>", nicho="Clínica odontológica",
      bairro="Centro", cidade="Florianópolis", uf="SC", rua="Rua Felipe Schmidt, 390 — sala 1102",
      title="Sorriso Prime · Dentista no Centro de Florianópolis (demo)",
      desc="Clínica odontológica no Centro de Florianópolis: clínico geral, clareamento, alinhadores, implantes e atendimento por convênio. Agende sua consulta.",
      cor="#1557B0", fav_fg="#FFFFFF", fav_font="Arial", fonts="family=Plus+Jakarta+Sans:wght@400;500;600;700;800",
      schema="Dentist", insta="sorrisoprime", cta="Agendar consulta",
      wa="Olá! Gostaria de agendar uma consulta na Sorriso Prime.",
      horas=H("Seg a sex: 8h às 19h", "Sábado: 8h às 12h"), horas_schema=["Mo-Fr 08:00-19:00", "Sa 08:00-12:00"],
      nav=[("tratamentos", "Tratamentos"), ("resultados", "Antes e depois"), ("convenios", "Convênios"), ("equipe", "Equipe")]),
 dict(slug="ink-raiz-tattoo", name="Ink Raiz Tattoo", brand="INK RAIZ<span>*</span>", nicho="Estúdio de tatuagem",
      bairro="Lapa", cidade="Rio de Janeiro", uf="RJ", rua="Rua do Lavradio, 147 — 2º andar",
      title="Ink Raiz Tattoo · Estúdio de tatuagem na Lapa, Rio de Janeiro (demo)",
      desc="Estúdio de tatuagem na Lapa, Rio de Janeiro: fineline, blackwork, realismo, old school e pontilhismo. Veja o portfólio e faça seu orçamento.",
      cor="#0A0A0A", fav_fg="#FFFFFF", fav_font="Arial Black", fonts="family=Syne:wght@600;700;800&family=Space+Grotesk:wght@400;500;600;700",
      schema="TattooParlor", insta="inkraiz", cta="Fazer orçamento",
      wa="Salve! Quero fazer um orçamento de tatuagem na Ink Raiz.",
      horas=H("Ter a sáb: 11h às 20h", "Só com hora marcada"), horas_schema=["Tu-Sa 11:00-20:00"],
      nav=[("portfolio", "Portfólio"), ("artistas", "Artistas"), ("orcamento", "Orçamento"), ("cuidados", "Cuidados")]),
 dict(slug="sabor-de-casa", name="Sabor de Casa", brand="Sabor <span>de</span> Casa", nicho="Marmitaria",
      bairro="Santa Mônica", cidade="Uberlândia", uf="MG", rua="Av. Segismundo Pereira, 1340",
      title="Sabor de Casa · Marmitas caseiras no Santa Mônica, Uberlândia (demo)",
      desc="Marmitas caseiras no Santa Mônica, em Uberlândia: cardápio da semana, planos de assinatura e entrega no almoço. Assine pelo WhatsApp.",
      cor="#2F7D32", fav_fg="#FFFBF2", fonts="family=Bitter:wght@600;700;800&family=Nunito:wght@400;600;700",
      schema="FoodEstablishment", insta="sabordecasa", cta="Assinar marmitas",
      wa="Oi! Quero assinar as marmitas da Sabor de Casa.",
      horas=H("Seg a sex: 9h às 14h", "Entregas: 11h às 13h30"), horas_schema=["Mo-Fr 09:00-14:00"],
      nav=[("cardapio", "Cardápio da semana"), ("planos", "Planos"), ("entrega", "Entrega"), ("duvidas", "Dúvidas")]),
 dict(slug="brilho-lar", name="Brilho Lar", brand="Brilho<span>Lar</span>", nicho="Limpeza residencial e diaristas",
      bairro="Jardim da Penha", cidade="Vitória", uf="ES", rua="Atendimento a domicílio",
      title="Brilho Lar · Diaristas e limpeza residencial em Vitória, ES (demo)",
      desc="Diaristas e limpeza residencial em Vitória: limpeza padrão, pesada e pós-obra. Simule o preço por cômodo e solicite sua diária.",
      cor="#0B6FB8", fav_fg="#FFFFFF", fav_font="Arial", fonts="family=Outfit:wght@400;500;600;700",
      schema="LocalBusiness", insta="brilholar", cta="Solicitar diária",
      wa="Olá! Quero solicitar uma diária com a Brilho Lar.",
      horas=H("Seg a sáb: 7h às 18h", "Atendimento: 8h às 20h"), horas_schema=["Mo-Sa 07:00-18:00"],
      nav=[("servicos", "Serviços"), ("simulador", "Simular preço"), ("como-funciona", "Como funciona"), ("areas", "Áreas atendidas")]),
]

DESTAQUES = {
 "studio-bella-fios": "Galeria antes/depois", "navalha-club": "Clube de assinatura", "forno-da-vila": "Cardápio filtrável",
 "patas-e-cia": "Calculadora por porte", "clinica-lumiere": "Quiz de tratamento", "auto-center-pistao": "Orçamento rápido",
 "doce-atelie-lu": "Monte seu bolo", "iron-fit": "Horários interativos", "sorriso-prime": "Antes/depois deslizante",
 "ink-raiz-tattoo": "Portfólio por estilo", "sabor-de-casa": "Cardápio por dia", "brilho-lar": "Simulador por cômodo",
}


def HUB(demos):
    cards = "".join(
        f'<a class="demo" href="{d["slug"]}/" style="--c:{d["cor"]}"><span class="sw"></span><span class="n">{i:02d}</span>'
        f'<strong>{d["name"]}</strong><span>{d["nicho"]} · {d["cidade"]}/{d["uf"]}</span><em>{DESTAQUES[d["slug"]]}</em></a>'
        for i, d in enumerate(demos, 1))
    falta = 12 - len(demos)
    return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Demos de sites para negócios locais · Gustavo Pereira · Sites</title>
<meta name="description" content="12 sites de demonstração para negócios locais: salão, barbearia, pizzaria, pet shop, estética, oficina, confeitaria, academia, dentista, tatuagem, marmitaria e limpeza.">
<meta name="theme-color" content="#0E0E0E">
<style>
*{{box-sizing:border-box}}body{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:#0E0E0E;color:#F4F1EC;line-height:1.55}}
.w{{width:min(100% - 2.5rem,1140px);margin:auto}}header{{padding:4.5rem 0 2.5rem}}
.k{{color:#FF7A1A;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:.8rem}}
h1{{font-size:clamp(2.2rem,6vw,3.8rem);line-height:1.05;margin:.5rem 0 1rem;max-width:18ch}}
p{{color:#BDB6AC;max-width:58ch}}a{{color:inherit}}
.g{{display:grid;gap:1rem;grid-template-columns:repeat(auto-fill,minmax(min(100%,250px),1fr));padding-bottom:4rem}}
.demo{{position:relative;display:flex;flex-direction:column;gap:.25rem;padding:1.4rem;border:1px solid #2A2A2A;border-radius:14px;text-decoration:none;background:#151515;transition:border-color .2s,transform .2s}}
.demo:hover,.demo:focus-visible{{border-color:#FF7A1A;transform:translateY(-3px)}}:focus-visible{{outline:3px solid #FF7A1A;outline-offset:3px}}
.sw{{height:70px;border-radius:9px;background:var(--c);margin-bottom:.9rem;border:1px solid #333}}
.n{{position:absolute;top:1.9rem;right:2rem;font-size:.8rem;font-weight:700;color:#fff;mix-blend-mode:difference}}
.demo strong{{font-size:1.15rem}}.demo span{{color:#A8A197;font-size:.9rem}}.demo em{{font-style:normal;color:#FF9A4D;font-size:.85rem;font-weight:600;margin-top:.4rem}}
footer{{border-top:1px solid #262626;padding:2rem 0 3rem;font-size:.88rem;color:#A8A197}}
</style></head><body>
<header class="w"><span class="k">Portfólio · demonstrações</span><h1>Sites de demonstração para negócios locais</h1>
<p>Cada demo mostra um tipo de site com uma função que ajuda a vender: agenda pelo WhatsApp, cardápio, calculadora de preço, orçamento rápido. Todos os negócios são fictícios.</p></header>
<main class="w g">{cards}</main>{'<p class="w" style="padding-bottom:3rem">Mais ' + str(falta) + ' demos chegando em breve.</p>' if falta else ''}
<footer class="w"><p><strong>Sites demonstrativos — negócios fictícios.</strong> Nomes, preços, avaliações e números são exemplos. Feito por <a href="https://pereira-gu.github.io/sites/">Gustavo Pereira · Sites</a> · <a href="https://www.instagram.com/dev.gustavop/">@dev.gustavop</a></p></footer>
</body></html>'''
