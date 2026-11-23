/* Movimento leve: revela blocos ao rolar. Apagar este arquivo e motion.css não quebra o site. */
(() => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) return;
  document.documentElement.classList.add('motion');
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
  document.querySelectorAll('.sec .sec-head, .sec .card, .sec .reveal, .sec figure').forEach(el => io.observe(el));
})();
