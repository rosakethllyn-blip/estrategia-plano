(() => {
  const dialog = document.getElementById('roteiroDialog');
  const content = document.getElementById('roteiroContent');
  const title = document.getElementById('roteiroTitle');
  const download = document.getElementById('roteiroDownload');
  const close = document.getElementById('roteiroClose');
  let trigger, controller, previousOverflow;
  document.querySelectorAll('[data-roteiro]').forEach(link => {
    link.addEventListener('click', async event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      trigger = link;
      controller?.abort();
      controller = new AbortController();
      const request = controller;
      title.textContent = `Roteiro · Episódio ${link.dataset.roteiro}`;
      download.href = link.href;
      download.download = `EstrategIA-ep${link.dataset.roteiro}.pdf`;
      content.textContent = 'Carregando roteiro completo…';
      content.setAttribute('aria-busy', 'true');
      previousOverflow = document.body.style.overflow;
      document.body.style.overflow = 'hidden';
      dialog.showModal();
      close.focus();
      try {
        const response = await fetch(`roteiros/preview/ep${link.dataset.roteiro}.html`, { signal: request.signal });
        if (!response.ok) throw new Error('Preview unavailable');
        const markup = await response.text();
        if (request.signal.aborted) return;
        // Generated locally from the repository's trusted editorial sources.
        content.innerHTML = markup;
        content.scrollTop = 0;
      } catch (error) {
        if (error.name !== 'AbortError') content.textContent = 'Não foi possível carregar a prévia. Você ainda pode baixar o roteiro completo em PDF pelo botão acima.';
      } finally {
        if (request === controller) content.setAttribute('aria-busy', 'false');
      }
    });
  });
  close.addEventListener('click', () => dialog.close());
  let backdropDown = false;
  dialog.addEventListener('pointerdown', e => { backdropDown = e.target === dialog; });
  dialog.addEventListener('click', e => {
    if (e.target === dialog && backdropDown) {
      const r = dialog.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dialog.close();
    }
  });
  dialog.addEventListener('close', () => {
    controller?.abort();
    document.body.style.overflow = previousOverflow;
    trigger?.focus({ preventScroll: true });
  });
  // Native modal dialog makes the page inert and handles Escape; keep Tab in its controls.
  dialog.addEventListener('keydown', event => {
    if (event.key !== 'Tab') return;
    const focusable = [...dialog.querySelectorAll('a[href], button, [tabindex="0"]')];
    const first = focusable[0], last = focusable.at(-1);
    if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
    else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
  });
})();
