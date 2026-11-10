/* ==========================================================================
   EDITE AQUI: preços, textos dos planos, contatos e portfólio.
   Depois de salvar, é só recarregar a página. Não precisa mexer no resto.
   ========================================================================== */
const CONFIG = {
  marca: 'Gustavo Pereira · Sites',
  whatsapp: '5511915072940',       // só números, com 55 e DDD
  mensagem: 'Oi, Gustavo! Vi seu site e quero um orçamento.',
  instagram: 'dev.gustavop',       // sem o @

  // Planos principais. "destaque: true" deixa o plano laranja, com o selo.
  planos: [
    {
      nome: 'Essencial',
      tipo: 'Vitrine',
      preco: 400,
      itens: ['1 página responsiva', 'Apresentação', 'Fotos', 'Horário', 'Mapa', 'Botão de WhatsApp'],
    },
    {
      nome: 'Catálogo',
      tipo: 'Para vender mais fácil',
      preco: 700,
      destaque: true,
      selo: 'Mais escolhido',
      itens: ['Até 5 seções', 'Catálogo de produtos com fotos e preços', 'Botão de pedido pelo WhatsApp', 'Instagram integrado'],
    },
    {
      nome: 'Completo',
      tipo: 'Para organizar o negócio',
      preco: 1100,
      itens: ['Tudo do Catálogo', 'Agendamento ou formulário de pedidos', 'Cadastro de clientes', 'Painel simples para o dono'],
    },
  ],

  manutencao: {
    nome: 'Manutenção',
    preco: 60,
    itens: ['Pequenas alterações', 'Atualização de preços e fotos', 'Suporte'],
  },

  // Faixa laranja abaixo dos planos.
  oferta: {
    titulo: 'Oferta de lançamento',
    numero: '10%',
    texto: 'de desconto para os 3 primeiros clientes por indicação',
  },

  // Texto pequeno abaixo dos planos.
  condicoes: [
    'Sinal de 50% para começar e 50% na entrega.',
    'Até 2 rodadas de ajustes.',
    'Domínio próprio por conta do cliente.',
  ],

  // Frase embaixo do botão da chamada final.
  fraseConfianca: 'Orçamento sem compromisso',

  // Para adicionar um case, copie um bloco, troque os dados e coloque a imagem em assets/.
  portfolio: [
    {
      nome: 'Fio Reto',
      tipo: 'Barbearia fictícia',
      url: 'https://pereira-gu.github.io/barbearia-demo',
      imagem: 'assets/case-fio-reto.jpg',
      alt: 'Tela inicial do site da barbearia fictícia Fio Reto, com fundo verde-escuro e título em creme.',
    },
    {
      nome: 'Soprô',
      tipo: 'Salão de festas fictício',
      url: 'https://pereira-gu.github.io/sopro/',
      imagem: 'assets/case-sopro.jpg',
      alt: 'Tela inicial do site do salão de festas fictício Soprô, com fundo amarelo e balões coloridos.',
    },
  ],
};

/* ==========================================================================
   Daqui para baixo é o funcionamento da página.
   ========================================================================== */
const reais = (valor) => valor.toLocaleString('pt-BR');
const linkWhats = `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(CONFIG.mensagem)}`;
const iconeWhats = '<svg class="btn__ico" aria-hidden="true"><use href="#i-wa"/></svg>';
const preencher = (seletor, html) => document.querySelectorAll(seletor).forEach((el) => { el.innerHTML = html; });

/* Etiquetas dos planos */
document.querySelector('[data-planos]').innerHTML = CONFIG.planos.map((plano) => `
  <article class="plano ${plano.destaque ? 'plano--destaque' : ''} reveal">
    <span class="plano__furo" aria-hidden="true"></span>
    ${plano.selo ? `<p class="plano__selo">${plano.selo}</p>` : ''}
    <h3>${plano.nome}</h3>
    <p class="plano__tipo">${plano.tipo}</p>
    <p class="plano__preco"><small>R$</small> ${reais(plano.preco)}</p>
    <ul>${plano.itens.map((item) => `<li>${item}</li>`).join('')}</ul>
    <a class="btn ${plano.destaque ? 'btn--tinta' : 'btn--laranja'}" data-wa href="#" aria-label="Chamar no WhatsApp sobre o plano ${plano.nome}">
      ${iconeWhats} Chamar no WhatsApp
    </a>
  </article>`).join('');

/* Tira da manutenção */
const m = CONFIG.manutencao;
document.querySelector('[data-manutencao]').innerHTML = `
  <aside class="manutencao reveal" aria-label="Plano opcional de ${m.nome}">
    <div>
      <p class="manutencao__opcional">Opcional</p>
      <h3>${m.nome}</h3>
    </div>
    <p class="manutencao__preco"><small>R$</small> ${reais(m.preco)}<small> por mês</small></p>
    <ul>${m.itens.map((item) => `<li>${item}</li>`).join('')}</ul>
  </aside>`;

/* Oferta: o número aparece grande, mas o leitor de tela lê a frase na ordem certa */
const o = CONFIG.oferta;
document.querySelector('[data-oferta]').innerHTML = `
  <p class="oferta reveal">
    <span class="oferta__titulo">${o.titulo}:</span>
    <strong class="oferta__num">${o.numero}</strong>
    <span class="oferta__texto">${o.texto}</span>
  </p>`;

document.querySelector('[data-condicoes]').innerHTML = CONFIG.condicoes.map((c) => `<li>${c}</li>`).join('');

/* Cartões do portfólio, mais o espaço reservado para o próximo case */
document.querySelector('[data-portfolio]').innerHTML = CONFIG.portfolio.map((c) => `
  <article class="case reveal">
    <img src="${c.imagem}" alt="${c.alt}" width="800" height="600" loading="lazy" decoding="async">
    <div class="case__texto">
      <div><h3>${c.nome}</h3><p>${c.tipo} · demonstração</p></div>
      <a class="btn btn--laranja btn--curto" href="${c.url}" target="_blank" rel="noopener" aria-label="Ver site ${c.nome} (abre em nova aba)">Ver site</a>
    </div>
  </article>`).join('') + `
  <article class="case case--proximo reveal">
    <h3>O próximo pode ser o da sua loja</h3>
    <a class="btn btn--laranja" data-wa href="#">${iconeWhats} Chamar no WhatsApp</a>
  </article>`;

/* Valores repetidos em outras partes da página */
preencher('[data-menor-preco]', reais(Math.min(...CONFIG.planos.map((p) => p.preco))));
preencher('[data-preco-manutencao]', reais(m.preco));
preencher('[data-texto="marca"]', CONFIG.marca);
preencher('[data-texto="confianca"]', CONFIG.fraseConfianca);
preencher('[data-ano]', new Date().getFullYear());

/* Links de contato */
document.querySelectorAll('[data-wa]').forEach((a) => {
  a.href = linkWhats;
  a.target = '_blank';
  a.rel = 'noopener';
});
document.querySelectorAll('[data-insta]').forEach((a) => {
  a.href = `https://www.instagram.com/${CONFIG.instagram}/`;
  a.target = '_blank';
  a.rel = 'noopener';
  a.textContent = `Instagram @${CONFIG.instagram}`;
});

/* Animação ao rolar: cada bloco anima uma vez, ao entrar na tela */
const reveals = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const observador = new IntersectionObserver((entradas) => {
    entradas.forEach((entrada) => {
      if (!entrada.isIntersecting) return;
      entrada.target.classList.add('visivel');
      observador.unobserve(entrada.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  reveals.forEach((el) => observador.observe(el));

  /* Esconde o botão flutuante quando outro botão de WhatsApp passa embaixo dele */
  const flutuante = document.querySelector('.flutuante');
  const naZona = new Set();
  const zona = new IntersectionObserver((entradas) => {
    entradas.forEach((e) => (e.isIntersecting ? naZona.add(e.target) : naZona.delete(e.target)));
    flutuante.classList.toggle('flutuante--oculto', naZona.size > 0);
  }, { rootMargin: '-86% 0px 0px 0px' });
  document.querySelectorAll('[data-wa]:not(.flutuante)').forEach((el) => zona.observe(el));
} else {
  reveals.forEach((el) => el.classList.add('visivel'));
}
