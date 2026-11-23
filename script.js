/* ==========================================================================
   EDITE AQUI: contatos e textos de cada tipo de negócio.
   Depois de salvar, é só recarregar a página. Não precisa mexer no resto.
   ========================================================================== */
const CONFIG = {
  marca: 'Gustavo Pereira · Sites',
  whatsapp: '5511915072940',       // só números, com 55 e DDD
  instagram: 'dev.gustavop',       // sem o @
  mensagemPadrao: 'Oi, Gustavo! Vi seu site e quero um orçamento.',

  // Seção "Site pra sua ...": o que o site mostra para cada ramo.
  negocios: {
    barbearia: {
      palavra: 'barbearia', artigo: 'uma barbearia',
      itens: ['Serviços e preços à vista', 'Botão de agendar horário', 'WhatsApp com mensagem pronta'],
      exemplo: { texto: 'Ver o exemplo da Fio Reto (demonstração)', url: 'https://pereira-gu.github.io/barbearia-demo' },
    },
    salao: {
      palavra: 'salão', artigo: 'um salão de beleza',
      itens: ['Serviços com preço, por categoria', 'Fotos dos trabalhos', 'Agendamento pelo celular'],
    },
    buffet: {
      palavra: 'buffet', artigo: 'um buffet',
      itens: ['Pacotes e o que cada um inclui', 'Fotos do espaço', 'Pedido de orçamento com a data da festa'],
      exemplo: { texto: 'Ver o exemplo da Soprô (demonstração)', url: 'https://pereira-gu.github.io/sopro/' },
    },
    loja: {
      palavra: 'loja', artigo: 'uma loja',
      itens: ['Catálogo com foto e preço', 'Pedido direto no WhatsApp', 'Endereço, horário e mapa'],
    },
    outro: { artigo: 'um negócio' },
  },
};

/* ==========================================================================
   Daqui para baixo é o funcionamento da página.
   ========================================================================== */
const linkWhats = (texto) => `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(texto)}`;
const linkDirect = `https://www.instagram.com/${CONFIG.instagram}/`;
const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];

/* Contatos (os links já estão no HTML; aqui só garantem os dados do CONFIG) */
$$('[data-wa]:not([data-wa-pedido])').forEach((a) => { a.href = linkWhats(CONFIG.mensagemPadrao); });
$$('[data-direct]').forEach((a) => { a.href = linkDirect; });
$$('[data-texto="marca"]').forEach((el) => { el.textContent = CONFIG.marca; });
$$('[data-ano]').forEach((el) => { el.textContent = new Date().getFullYear(); });

/* --- Pedido de orçamento em 3 toques --- */
const pedido = $('[data-pedido]');
let mensagemPedido = CONFIG.mensagemPadrao;

function atualizarPedido() {
  if (!pedido) return;
  const dados = new FormData(pedido);
  const negocio = CONFIG.negocios[dados.get('negocio')] || CONFIG.negocios.outro;
  const insta = dados.get('insta') === 'sim' ? 'já tenho Instagram' : 'ainda não tenho Instagram';
  const agenda = {
    sim: 'preciso de agendamento online',
    nao: 'não preciso de agendamento',
    'nao-sei': 'não sei se preciso de agendamento',
  }[dados.get('agenda')];
  mensagemPedido = `Oi, Gustavo! Tenho ${negocio.artigo}, ${insta} e ${agenda}. Quero um orçamento.`;
  $('[data-pedido-texto]').textContent = mensagemPedido;
  $('[data-wa-pedido]').href = linkWhats(mensagemPedido);
}
if (pedido) {
  pedido.addEventListener('change', atualizarPedido);
  atualizarPedido();
}

/* No direct não dá para levar o texto pelo link: copiamos para a pessoa colar */
$$('[data-copiar]').forEach((a) => a.addEventListener('click', () => {
  if (!navigator.clipboard) return;
  navigator.clipboard.writeText(mensagemPedido).then(() => {
    const nota = $('[data-copiar-nota]');
    if (nota) nota.textContent = 'Mensagem copiada. No direct, é só colar e enviar.';
  }).catch(() => {});
}));

/* --- Seletor "Site pra sua ..." --- */
const secaoNegocio = $('[data-negocio-campo]');
const botoesNegocio = $$('[data-negocio]');

function escolherNegocio(chave, focar) {
  const n = CONFIG.negocios[chave];
  if (!n) return;
  botoesNegocio.forEach((b) => {
    const ativo = b.dataset.negocio === chave;
    b.setAttribute('aria-checked', ativo);
    b.tabIndex = ativo ? 0 : -1;
    if (ativo && focar) b.focus();
  });
  secaoNegocio.dataset.negocioCampo = chave;
  $('[data-negocio-palavra]').textContent = n.palavra;
  $('[data-negocio-lista]').innerHTML = n.itens.map((i) => `<li>${i}</li>`).join('');
  $('[data-negocio-exemplo]').innerHTML = n.exemplo
    ? `<a class="link-seta" href="${n.exemplo.url}" target="_blank" rel="noopener">${n.exemplo.texto}</a>`
    : 'Ainda não tenho uma demonstração desse ramo. Me chama que eu te mostro como ficaria.';

  /* Leva a escolha para o pedido de orçamento */
  const radio = pedido && pedido.querySelector(`input[name="negocio"][value="${chave}"]`);
  if (radio) { radio.checked = true; atualizarPedido(); }
}

botoesNegocio.forEach((b, i) => {
  b.tabIndex = i === 0 ? 0 : -1;
  b.addEventListener('click', () => escolherNegocio(b.dataset.negocio));
  /* Setas trocam a opção, como num grupo de rádio */
  b.addEventListener('keydown', (e) => {
    const passo = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
    if (!passo) return;
    e.preventDefault();
    const prox = botoesNegocio[(i + passo + botoesNegocio.length) % botoesNegocio.length];
    escolherNegocio(prox.dataset.negocio, true);
  });
});

/* --- Antes e depois --- */
$$('[data-comparar]').forEach((caixa) => {
  const controle = $('.comparar__controle', caixa);
  const aplicar = () => {
    const v = Number(controle.value);
    caixa.style.setProperty('--pos', `${v}%`);
    let texto = 'Metade antes, metade depois';
    if (v <= 5) texto = 'Mostrando só o depois';
    else if (v >= 95) texto = 'Mostrando só o antes';
    else if (v < 50) texto = `${100 - v}% depois`;
    else if (v > 50) texto = `${v}% antes`;
    controle.setAttribute('aria-valuetext', texto);
  };
  controle.addEventListener('input', aplicar);
  aplicar();

  /* Arrastar com o dedo ou o mouse (as setas do teclado vão direto no controle) */
  const moldura = $('.comparar__moldura', caixa);
  const mover = (e) => {
    const r = moldura.getBoundingClientRect();
    const v = Math.round(Math.min(100, Math.max(0, ((e.clientX - r.left) / r.width) * 100)));
    controle.value = v;
    aplicar();
  };
  moldura.addEventListener('pointerdown', (e) => {
    moldura.setPointerCapture(e.pointerId);
    mover(e);
    controle.focus({ preventScroll: true });
  });
  moldura.addEventListener('pointermove', (e) => { if (moldura.hasPointerCapture(e.pointerId)) mover(e); });
});

/* --- Como funciona: abre uma etapa por vez --- */
const etapas = $$('[data-etapas] .etapa');
etapas.forEach((etapa) => {
  $('button', etapa).addEventListener('click', () => {
    etapas.forEach((e) => {
      const abrir = e === etapa;
      e.classList.toggle('aberta', abrir);
      $('button', e).setAttribute('aria-expanded', abrir);
    });
  });
});

/* --- Botão flutuante: some quando outro botão de contato passa embaixo dele --- */
const flutuante = $('.flutuante');
if ('IntersectionObserver' in window && flutuante) {
  const naZona = new Set();
  const secoesNaTela = new Set();
  const atualizar = () => flutuante.classList.toggle('flutuante--oculto', secoesNaTela.size > 0 || naZona.size > 0);
  const zona = new IntersectionObserver((entradas) => {
    entradas.forEach((e) => (e.isIntersecting ? naZona.add(e.target) : naZona.delete(e.target)));
    atualizar();
  }, { rootMargin: '-80% 0px 0px 0px' });
  $$('.btn[data-direct], .btn[data-wa]').forEach((el) => zona.observe(el));
  /* No topo e no pedido de orçamento os botões de contato já estão à vista */
  const secoes = new IntersectionObserver((entradas) => {
    entradas.forEach((e) => (e.isIntersecting ? secoesNaTela.add(e.target) : secoesNaTela.delete(e.target)));
    atualizar();
  }, { threshold: 0.15 });
  $$('.heroi, .orcamento, .rodape').forEach((el) => secoes.observe(el));
}
