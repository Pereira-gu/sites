/* Interações compartilhadas das demos: menu, WhatsApp, filtros, abas, antes/depois, calculadoras e formulários */
(() => {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const brl = v => v.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
  const wa = t => 'https://wa.me/?text=' + encodeURIComponent(t);

  // Menu mobile
  const tg = $('.menu-toggle'), menu = $('#menu');
  if (tg && menu) {
    const set = o => { tg.setAttribute('aria-expanded', o); menu.classList.toggle('open', o); tg.textContent = o ? 'Fechar' : 'Menu'; };
    tg.addEventListener('click', () => set(tg.getAttribute('aria-expanded') !== 'true'));
    $$('a', menu).forEach(a => a.addEventListener('click', () => set(false)));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') set(false); });
  }

  // Links de WhatsApp com mensagem pronta
  $$('[data-wa]').forEach(a => { a.href = wa(a.dataset.wa); a.target = '_blank'; a.rel = 'noopener'; });

  // Filtros por categoria (cardápio, portfólio, horários)
  $$('[data-filter]').forEach(g => {
    const scope = $(g.dataset.filter);
    const status = g.nextElementSibling && g.nextElementSibling.classList.contains('filter-status') ? g.nextElementSibling : null;
    g.addEventListener('click', e => {
      const b = e.target.closest('button'); if (!b) return;
      $$('button', g).forEach(x => x.setAttribute('aria-pressed', x === b));
      const f = b.dataset.value; let n = 0;
      $$('[data-cat]', scope).forEach(i => { const ok = f === 'todos' || i.dataset.cat.split(' ').includes(f); i.hidden = !ok; if (ok) n++; });
      if (status) status.textContent = `${n} ${n === 1 ? (g.dataset.one || 'item') : (g.dataset.many || 'itens')} ${b.textContent.trim() === 'Todos' || b.textContent.trim() === 'Todas' ? 'no total' : 'em ' + b.textContent.trim()}`;
    });
  });

  // Abas acessíveis (setas do teclado)
  $$('[role=tablist]').forEach(list => {
    const tabs = $$('[role=tab]', list);
    const sel = t => tabs.forEach(x => { const on = x === t; x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1; document.getElementById(x.getAttribute('aria-controls')).hidden = !on; });
    tabs.forEach((x, i) => {
      x.addEventListener('click', () => sel(x));
      x.addEventListener('keydown', e => {
        let j = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : null; if (j === null) return;
        e.preventDefault(); j = (j + tabs.length) % tabs.length; tabs[j].focus(); sel(tabs[j]);
      });
    });
    if ('today' in list.dataset) { const t = tabs.find(x => +x.dataset.day === new Date().getDay()); if (t) sel(t); }
  });

  // Antes/depois com controle deslizante
  $$('.ba').forEach(b => { const r = $('input', b); const u = () => b.style.setProperty('--pos', r.value + '%'); r.addEventListener('input', u); u(); });

  // Calculadoras: data-price soma, data-mult multiplica, data-flat soma no fim, number usa data-unit
  $$('[data-calc]').forEach(f => {
    const out = $('[data-total]', f), btn = $('[data-calc-wa]', f), sum = $('[data-summary]', f);
    const run = () => {
      let add = 0, mult = 1, flat = 0; const items = [];
      $$('input,select', f).forEach(el => {
        if (el.type === 'number') { const q = Math.max(0, +el.value || 0); if (q) { add += q * (+el.dataset.unit || 0); items.push(`${q} ${el.dataset.label}`); } return; }
        let src = null;
        if (el.type === 'checkbox' || el.type === 'radio') { if (el.checked) src = el; }
        else if (el.tagName === 'SELECT') src = el.selectedOptions[0];
        else if (el.value && el.dataset.label) { items.push(`${el.dataset.label}: ${el.value}`); return; }
        if (!src) return;
        const d = src.dataset;
        if (d.price) add += +d.price; if (d.mult) mult *= +d.mult; if (d.flat) flat += +d.flat;
        const lab = d.label || (src.tagName === 'OPTION' ? src.textContent.trim() : '');
        if (lab) items.push(lab);
      });
      const total = Math.round(add * mult + flat);
      if (out) out.textContent = brl(total);
      if (sum) sum.textContent = items.join(' · ');
      if (btn) { btn.href = wa(`${btn.dataset.calcWa}\n${items.map(i => '• ' + i).join('\n')}\nEstimativa do site: ${brl(total)}`); btn.target = '_blank'; btn.rel = 'noopener'; }
    };
    f.addEventListener('input', run); f.addEventListener('change', run); f.addEventListener('submit', e => e.preventDefault()); run();
  });

  // Formulários que viram mensagem de WhatsApp
  $$('[data-wa-form]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    const lines = [f.dataset.waForm];
    $$('input,select,textarea', f).forEach(el => {
      if (!el.name || !el.value || ((el.type === 'radio' || el.type === 'checkbox') && !el.checked)) return;
      const lab = el.dataset.label || (f.querySelector(`label[for="${el.id}"]`) || {}).textContent || el.name;
      lines.push(`${lab.trim()}: ${el.value}`);
    });
    window.open(wa(lines.join('\n')), '_blank', 'noopener');
  }));
})();
