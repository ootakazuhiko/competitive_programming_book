// Add copy buttons to code blocks
(function() {
  'use strict';
  function findBlocks() {
    const blocks = [];
    document.querySelectorAll('div.highlight pre > code, pre > code').forEach(code => {
      blocks.push(code);
    });
    return blocks;
  }

  function addButtons() {
    const blocks = findBlocks();
    blocks.forEach(code => {
      const pre = code.closest('pre');
      if (pre.dataset.copyBound) return;
      pre.dataset.copyBound = '1';

      const wrapper = document.createElement('div');
      wrapper.className = 'codeblock-wrapper';
      const container = pre.parentElement.classList.contains('highlight') ? pre.parentElement : pre.parentNode;
      container.parentNode.insertBefore(wrapper, container);
      wrapper.appendChild(container);

      const btn = document.createElement('button');
      btn.className = 'copy-button';
      btn.type = 'button';
      btn.innerText = 'Copy';
      btn.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(code.innerText);
          btn.innerText = 'Copied!';
          btn.classList.add('copied');
          setTimeout(() => { btn.innerText = 'Copy'; btn.classList.remove('copied'); }, 1200);
        } catch (_) {
          btn.innerText = 'Error';
          setTimeout(() => { btn.innerText = 'Copy'; }, 1200);
        }
      });

      const bar = document.createElement('div');
      bar.className = 'codeblock-toolbar';
      bar.appendChild(btn);
      wrapper.insertBefore(bar, pre);
    });
  }

  const css = `
  .codeblock-wrapper { position: relative; }
  .codeblock-toolbar { position: absolute; top: 8px; right: 8px; }
  .copy-button { font-size: 12px; padding: 4px 8px; border: 1px solid var(--border-color); background: var(--bg-primary); color: var(--text-primary); border-radius: 4px; cursor: pointer; }
  .copy-button:hover { border-color: var(--primary-color); }
  .copy-button.copied { background: #10b981; color: #fff; border-color: #10b981; }
  [data-theme="dark"] .copy-button { background: var(--bg-secondary); }
  `;
  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addButtons);
  } else {
    addButtons();
  }
})();
