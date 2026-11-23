"""Monta as 12 demos: junta cabeçalho, rodapé, SEO e WhatsApp fixo ao conteúdo de src/<slug>.html.
Uso: python3 build.py  (gera <slug>/index.html)"""
import json, random, re, pathlib
from urllib.parse import quote
from demos import DEMOS, HUB

ROOT = pathlib.Path(__file__).parent
WA_ICON = '<svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.26-.47-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.28-.2-.57-.35M12.05 21.8h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.83 9.83 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.88 9.88m8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.69 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.17-3.48-8.41z"/></svg>'


def fav(bg, fg, letter, font="Georgia"):
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='{bg}'/><text x='32' y='44' text-anchor='middle' font-family='{font}' font-weight='700' font-size='34' fill='{fg}'>{letter}</text></svg>"
    return "data:image/svg+xml," + quote(svg)


# ---------- geradores de arte (sem fotos de terceiros) ----------
def hair(seed, cores, frizz, fundo):
    """Mechas de cabelo em SVG: frizz alto = antes; liso e brilhante = depois."""
    rnd = random.Random(seed)
    gid = f"g{seed}{int(frizz*10)}"
    paths = []
    liso = frizz <= 4
    n = 34 if liso else 46
    for i in range(n):
        x = -30 + i * (470 / n)
        pts = [f"M{x:.1f},-10"]
        for k in range(1, 7):
            y = k * 55
            if liso:
                pts.append(f"Q{x + 10:.1f},{y - 27} {x + 4 * k:.1f},{y}")
            else:
                pts.append(f"Q{x + rnd.uniform(-frizz, frizz) * 3:.1f},{y - 27} {x + rnd.uniform(-frizz, frizz) * 1.5:.1f},{y}")
        w = 16 if liso else rnd.uniform(2, 6)
        op = rnd.uniform(.85, 1) if liso else rnd.uniform(.4, .8)
        paths.append(f'<path d="{" ".join(pts)}" stroke="url(#{gid})" stroke-width="{w:.1f}" fill="none" stroke-linecap="round" opacity="{op:.2f}"/>')
    brilho = '<path d="M-20,110 Q200,70 420,120" stroke="#fff" stroke-width="22" opacity=".28" fill="none"/><path d="M-20,128 Q200,88 420,138" stroke="#fff" stroke-width="5" opacity=".35" fill="none"/>' if liso else ''
    return (f'<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true">'
            f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{cores[0]}"/><stop offset="1" stop-color="{cores[1]}"/></linearGradient></defs>'
            f'<rect width="400" height="300" fill="{fundo}"/>{"".join(paths)}{brilho}</svg>')


def teeth(cor, alinhado, seed, gengiva="#C95C6E", boca="#5A1E2A"):
    """Sorriso estilizado em SVG para o antes/depois do dentista."""
    rnd = random.Random(seed)
    out = [f'<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="400" height="300" fill="#F1D3C4"/>',
           f'<path d="M40,150 Q200,40 360,150 Q200,270 40,150Z" fill="{boca}"/>',
           f'<path d="M60,140 Q200,70 340,140 L340,152 Q200,92 60,152Z" fill="{gengiva}"/>']
    xs = [70, 104, 136, 168, 200, 232, 264, 296]
    for i, x in enumerate(xs):
        mid = abs(i - 3.5)
        h = 46 - mid * 3.5
        y = 108 + mid * mid * 2.2
        dy = 0 if alinhado else rnd.uniform(-6, 7)
        rot = 0 if alinhado else rnd.uniform(-7, 7)
        w = 30 if alinhado else rnd.uniform(24, 30)
        out.append(f'<rect x="{x - w/2 + 16:.1f}" y="{y + dy:.1f}" width="{w:.1f}" height="{h:.1f}" rx="9" fill="{cor}" transform="rotate({rot:.1f} {x+16} {y+h/2})"/>')
    for i, x in enumerate(xs[1:-1]):
        mid = abs(i - 2.5)
        y = 170 - mid * mid * 1.6
        dy = 0 if alinhado else rnd.uniform(-5, 6)
        out.append(f'<rect x="{x + 4:.1f}" y="{y + dy:.1f}" width="28" height="{30 - mid*2:.1f}" rx="8" fill="{cor}" opacity=".92"/>')
    if alinhado:
        out.append('<path d="M110,118 Q170,104 230,112" stroke="#fff" stroke-width="6" opacity=".55" fill="none" stroke-linecap="round"/>')
    out.append('<path d="M40,150 Q200,40 360,150" stroke="#C77D7D" stroke-width="16" fill="none"/><path d="M40,150 Q200,270 360,150" stroke="#C77D7D" stroke-width="20" fill="none"/></svg>')
    return "".join(out)


def ba(titulo, sub, antes, depois):
    return (f'<figure class="ba-card"><div class="ba"><div class="ba-img">{antes}</div><div class="ba-img ba-after">{depois}</div>'
            f'<span class="ba-label l">Antes</span><span class="ba-label r">Depois</span><span class="ba-knob" aria-hidden="true">‹ ›</span>'
            f'<input type="range" min="0" max="100" value="50" aria-label="Comparar antes e depois: {titulo}"></div>'
            f'<figcaption><strong>{titulo}</strong><span>{sub}</span></figcaption></figure>')


ARTS = {
    "BA_SALAO_1": lambda: ba("Morena iluminada", "Mechas finas e tonalização · 4 h", hair(1, ("#5e534b", "#7d7168"), 9, "#cfc8c1"), hair(1, ("#3b2418", "#e0b072"), 1, "#3b2418")),
    "BA_SALAO_2": lambda: ba("Progressiva sem formol", "Alinhamento e brilho · 3 h", hair(2, ("#4a423d", "#6a615b"), 12, "#c9c2bb"), hair(2, ("#1f140f", "#6b4630"), 0.5, "#1f140f")),
    "BA_SALAO_3": lambda: ba("Corte e hidratação", "Pontas renovadas · 1 h 30", hair(3, ("#7d6650", "#a08b77"), 8, "#d9d0c7"), hair(3, ("#5a361d", "#c48b52"), 1.5, "#5a361d")),
    "BA_DENTE_1": lambda: ba("Clareamento supervisionado", "Consultório + caseiro · 3 semanas", teeth("#E2CE98", True, 5), teeth("#FBFAF5", True, 5)),
    "BA_DENTE_2": lambda: ba("Alinhadores transparentes", "Tratamento planejado · 10 meses", teeth("#F1EBDD", False, 7), teeth("#F7F5EF", True, 7)),
    "BA_DENTE_3": lambda: ba("Facetas em resina", "Forma e cor · 2 sessões", teeth("#D9C493", False, 11), teeth("#FAF8F2", True, 11)),
}


def horarios():
    """Grade da Iron Fit: abas por dia + filtro por modalidade."""
    dias = [("seg", "Seg", 1), ("ter", "Ter", 2), ("qua", "Qua", 3), ("qui", "Qui", 4), ("sex", "Sex", 5), ("sab", "Sáb", 6)]
    base = {
        "seg": [("06:00", "Funcional", "funcional", "Rafa", "Box"), ("07:00", "Spinning", "spinning", "Léo", "Bike"), ("12:15", "HIIT 30", "hiit", "Rafa", "Box"), ("18:00", "Muay thai", "luta", "Mestre Jonas", "Tatame"), ("19:00", "Spinning", "spinning", "Carol", "Bike"), ("20:00", "Funcional", "funcional", "Rafa", "Box")],
        "ter": [("06:30", "HIIT 30", "hiit", "Carol", "Box"), ("07:00", "Yoga flow", "yoga", "Ana", "Sala 2"), ("12:15", "Spinning", "spinning", "Léo", "Bike"), ("18:30", "Funcional", "funcional", "Rafa", "Box"), ("19:30", "Muay thai", "luta", "Mestre Jonas", "Tatame")],
        "qua": [("06:00", "Funcional", "funcional", "Rafa", "Box"), ("07:00", "Spinning", "spinning", "Léo", "Bike"), ("12:15", "HIIT 30", "hiit", "Carol", "Box"), ("18:00", "Muay thai", "luta", "Mestre Jonas", "Tatame"), ("19:00", "Yoga flow", "yoga", "Ana", "Sala 2"), ("20:00", "Spinning", "spinning", "Carol", "Bike")],
        "qui": [("06:30", "HIIT 30", "hiit", "Carol", "Box"), ("07:00", "Yoga flow", "yoga", "Ana", "Sala 2"), ("12:15", "Spinning", "spinning", "Léo", "Bike"), ("18:30", "Funcional", "funcional", "Rafa", "Box"), ("19:30", "Muay thai", "luta", "Mestre Jonas", "Tatame")],
        "sex": [("06:00", "Funcional", "funcional", "Rafa", "Box"), ("07:00", "Spinning", "spinning", "Léo", "Bike"), ("12:15", "HIIT 30", "hiit", "Rafa", "Box"), ("18:00", "Spinning", "spinning", "Carol", "Bike"), ("19:00", "Muay thai", "luta", "Mestre Jonas", "Tatame")],
        "sab": [("08:00", "Aulão funcional", "funcional", "Rafa e Carol", "Box"), ("09:00", "Yoga flow", "yoga", "Ana", "Sala 2"), ("10:00", "Spinning", "spinning", "Léo", "Bike")],
    }
    tabs, panels = [], []
    for i, (k, nome, n) in enumerate(dias):
        on = i == 0
        tabs.append(f'<button class="chip" role="tab" id="t-{k}" data-day="{n}" aria-controls="p-{k}" aria-selected="{str(on).lower()}" tabindex="{0 if on else -1}">{nome}</button>')
        rows = "".join(f'<tr data-cat="{c}"><td class="num">{h}</td><td><strong>{a}</strong></td><td>{p}</td><td>{s}</td></tr>' for h, a, c, p, s in base[k])
        panels.append(f'<div role="tabpanel" id="p-{k}" aria-labelledby="t-{k}"{"" if on else " hidden"}><div class="table-wrap"><table><caption class="sr-only">Aulas de {nome}</caption><thead><tr><th>Horário</th><th>Aula</th><th>Professor</th><th>Espaço</th></tr></thead><tbody>{rows}</tbody></table></div></div>')
    return f'<div class="chips" role="tablist" aria-label="Dia da semana" data-today>{"".join(tabs)}</div><div id="grade">{"".join(panels)}</div>'


def cardapio():
    """Cardápio semanal da Sabor de Casa (abre no dia de hoje)."""
    dias = [
        ("seg", "Segunda", 1, [("Tradicional", "Frango ensopado com batata, arroz, feijão carioca e couve refogada"), ("Leve", "Filé de tilápia grelhado, arroz integral e legumes no vapor"), ("Vegetariana", "Escondidinho de mandioca com shimeji e salada de folhas")]),
        ("ter", "Terça", 2, [("Tradicional", "Carne moída com abóbora, arroz, feijão e farofa de ovos"), ("Leve", "Peito de frango ao limão, purê de abóbora e vagem"), ("Vegetariana", "Lasanha de berinjela com molho de tomate da casa")]),
        ("qua", "Quarta", 3, [("Tradicional", "Feijoada leve com arroz, couve, farofa e laranja"), ("Leve", "Carne magra de panela, arroz integral e brócolis"), ("Vegetariana", "Feijoada de feijão preto com legumes defumados")]),
        ("qui", "Quinta", 4, [("Tradicional", "Strogonoff de frango, arroz branco e batata palha"), ("Leve", "Omelete de forno com espinafre, arroz integral e salada"), ("Vegetariana", "Strogonoff de grão-de-bico com cogumelos")]),
        ("sex", "Sexta", 5, [("Tradicional", "Peixe ao molho de coco, arroz, pirão e vinagrete"), ("Leve", "Escondidinho de frango com batata-doce e salada"), ("Vegetariana", "Moqueca de banana-da-terra com arroz e farofa")]),
    ]
    tabs, panels = [], []
    for i, (k, nome, n, pratos) in enumerate(dias):
        on = i == 0
        tabs.append(f'<button class="chip" role="tab" id="t-{k}" data-day="{n}" aria-controls="p-{k}" aria-selected="{str(on).lower()}" tabindex="{0 if on else -1}">{nome}</button>')
        cards = "".join(f'<article class="card prato"><span class="tipo">{t}</span><h3>{d}</h3></article>' for t, d in pratos)
        panels.append(f'<div role="tabpanel" id="p-{k}" aria-labelledby="t-{k}"{"" if on else " hidden"}><div class="grid" style="--min:230px">{cards}</div></div>')
    return f'<div class="chips" role="tablist" aria-label="Dia da semana" data-today>{"".join(tabs)}</div>{"".join(panels)}'


ARTS["HORARIOS"] = horarios
ARTS["CARDAPIO"] = cardapio


def wa_link(msg):
    return "https://wa.me/?text=" + quote(msg)


def page(d):
    body = (ROOT / "src" / f"{d['slug']}.html").read_text(encoding="utf-8")
    body = re.sub(r"\{\{(\w+)\}\}", lambda m: ARTS[m.group(1)](), body)
    wa = wa_link(d["wa"])
    nav = "".join(f'<a href="#{h}">{t}</a>' for h, t in d["nav"])
    schema = {
        "@context": "https://schema.org", "@type": d["schema"], "name": d["name"],
        "description": d["desc"] + " Negócio fictício para demonstração.",
        "address": {"@type": "PostalAddress", "streetAddress": d["rua"], "addressLocality": d["cidade"], "addressRegion": d["uf"], "addressCountry": "BR"},
        "areaServed": d["cidade"], "openingHours": d["horas_schema"], "priceRange": "$$",
    }
    horas = "<br>".join(d["horas"])
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d["title"]}</title>
<meta name="description" content="{d["desc"]}">
<meta name="robots" content="noindex, follow">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{d["name"]} · {d["nicho"]} em {d["bairro"]}">
<meta property="og:description" content="{d["desc"]}">
<meta name="theme-color" content="{d["cor"]}">
<link rel="icon" href="{fav(d["cor"], d["fav_fg"], d["name"][0], d.get("fav_font", "Georgia"))}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{d["fonts"]}&display=swap">
<link rel="stylesheet" href="../shared/base.css">
<link rel="stylesheet" href="tema.css">
<link rel="stylesheet" href="../shared/motion.css">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<div class="demo-bar">Site demonstrativo · negócio, preços e avaliações fictícios</div>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="#inicio">{d["brand"]}</a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="menu">Menu</button>
    <nav id="menu" class="menu" aria-label="Principal">{nav}<a class="btn btn-primary" href="{wa}" target="_blank" rel="noopener">{d["cta"]}</a></nav>
  </div>
</header>
<main id="conteudo">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div><p class="brand">{d["brand"]}</p><p>{d["nicho"]} em {d["bairro"]}, {d["cidade"]}/{d["uf"]}.</p></div>
      <div><h3>Endereço</h3><p>{d["rua"]}<br>{d["bairro"]}, {d["cidade"]}/{d["uf"]}<br><small>endereço fictício</small></p></div>
      <div><h3>Horários</h3><p>{horas}</p></div>
      <div><h3>Contato</h3><p><a href="{wa}" target="_blank" rel="noopener">Chamar no WhatsApp</a><br>Instagram @{d["insta"]} <small>(fictício)</small></p></div>
    </div>
    <p class="aviso"><strong>Site demonstrativo — negócio fictício.</strong>Nome, endereço, preços, avaliações e números são exemplos criados para portfólio. Demo feita por <a href="https://pereira-gu.github.io/sites/">Gustavo Pereira · Sites</a> · Instagram <a href="https://www.instagram.com/dev.gustavop/">@dev.gustavop</a></p>
  </div>
</footer>
<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="{d["cta"]} pelo WhatsApp">{WA_ICON}<span>{d["cta"]}</span></a>
<script src="../shared/app.js" defer></script>
<script src="../shared/motion.js" defer></script>
</body>
</html>
'''


if __name__ == "__main__":
    prontas = [d for d in DEMOS if (ROOT / "src" / f"{d['slug']}.html").exists() and (ROOT / d["slug"] / "tema.css").exists()]
    for d in prontas:
        out = ROOT / d["slug"]
        out.mkdir(exist_ok=True)
        (out / "index.html").write_text(page(d), encoding="utf-8")
        print("ok", d["slug"])
    (ROOT / "index.html").write_text(HUB(prontas), encoding="utf-8")
    print("ok hub")
