/* ==========================================================================
   MOVIMENTO E 3D (opcional). Apagar este arquivo não quebra nada.
   ========================================================================== */
(() => {
  const menosMovimento = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (menosMovimento) return; // fica tudo parado e visível

  /* --- Entrada das seções: título, texto e imagem em sequência --- */
  const blocos = [...document.querySelectorAll('.reveal')];
  if ('IntersectionObserver' in window) {
    document.documentElement.classList.add('revela');
    const porSecao = new Map();
    blocos.forEach((el) => {
      const secao = el.closest('section, footer') || document.body;
      const n = porSecao.get(secao) || 0;
      el.style.setProperty('--atraso', `${Math.min(n, 5) * 80}ms`);
      porSecao.set(secao, n + 1);
    });
    const obs = new IntersectionObserver((entradas) => {
      entradas.forEach((e) => {
        if (!e.isIntersecting) return;
        e.target.classList.add('visivel');
        obs.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    blocos.forEach((el) => obs.observe(el));
  }

  /* --- Celular 3D: liga depois que a página carregou, sem atrasar o conteúdo --- */
  const celular = document.querySelector('[data-celular]');
  const economia = navigator.connection && navigator.connection.saveData;
  const temSuporte = window.CSS && CSS.supports('transform-style', 'preserve-3d');
  if (!celular || economia || !temSuporte) return; // fica a imagem inclinada

  const ligar3D = () => {
    const corpo = celular.querySelector('.celular__corpo');
    const camadas = document.createDocumentFragment();
    for (let z = 1; z <= 16; z++) {
      const c = document.createElement('span');
      c.className = 'celular__camada';
      c.setAttribute('aria-hidden', 'true');
      c.style.setProperty('--z', z);
      c.style.setProperty('--cor', z % 2 ? '#2A2620' : '#3A342C');
      camadas.appendChild(c);
    }
    corpo.prepend(camadas);
    celular.classList.add('tem-3d');

    /* Ângulo de repouso e quanto mouse, giro do aparelho e rolagem mexem */
    const base = { x: 8, y: -26 };
    const alvo = { x: 0, y: 0 };
    const atual = { x: 0, y: 0 };
    let rolagem = 0;
    let giro = 0;
    let visivel = true;
    let rodando = false;

    const passo = () => {
      atual.x += (alvo.x - atual.x) * 0.08;
      atual.y += (alvo.y - atual.y) * 0.08;
      corpo.style.setProperty('--rx', `${(base.x + atual.x).toFixed(2)}deg`);
      giro += (rolagem - giro) * 0.15;
      corpo.style.setProperty('--ry', `${(base.y + atual.y + giro).toFixed(2)}deg`);
      const parado = Math.abs(alvo.x - atual.x) < 0.02 && Math.abs(alvo.y - atual.y) < 0.02 && Math.abs(rolagem - giro) < 0.02;
      if (visivel && !parado) requestAnimationFrame(passo);
      else rodando = false;
    };
    const acordar = () => {
      if (rodando || !visivel || document.hidden) return;
      rodando = true;
      requestAnimationFrame(passo);
    };

    /* Mouse: o celular olha para o ponteiro */
    if (matchMedia('(pointer: fine)').matches) {
      addEventListener('pointermove', (e) => {
        alvo.y = ((e.clientX / innerWidth) - 0.5) * 28;
        alvo.x = -((e.clientY / innerHeight) - 0.5) * 18;
        acordar();
      }, { passive: true });
    }

    /* Celular (Android): inclina com o aparelho, sem pedir permissão */
    addEventListener('deviceorientation', (e) => {
      if (e.gamma == null) return;
      alvo.y = Math.max(-20, Math.min(20, e.gamma)) * 0.8;
      alvo.x = Math.max(-15, Math.min(15, (e.beta || 45) - 45)) * -0.5;
      acordar();
    }, { passive: true });

    /* Rolagem: gira um pouco enquanto o topo sai da tela */
    const heroi = document.querySelector('.heroi');
    addEventListener('scroll', () => {
      const r = heroi.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, -r.top / r.height));
      rolagem = p * 32;
      acordar();
    }, { passive: true });

    /* Pausa quando o topo não está na tela */
    new IntersectionObserver(([e]) => { visivel = e.isIntersecting; acordar(); }).observe(heroi);
    document.addEventListener('visibilitychange', acordar);
    acordar();
  };

  const depois = () => ('requestIdleCallback' in window ? requestIdleCallback(ligar3D, { timeout: 1500 }) : setTimeout(ligar3D, 300));
  if (document.readyState === 'complete') depois();
  else addEventListener('load', depois, { once: true });
})();
