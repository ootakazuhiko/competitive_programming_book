// Lightweight Mermaid initializer (temporary: for prototyping only)
(function(){
  'use strict';
  if (!document.querySelector('code.language-mermaid, .language-mermaid')) return;
  function init(){
    if (window.mermaid && window.mermaid.initialize){
      window.mermaid.initialize({ startOnLoad: true, theme: 'default' });
      return;
    }
    setTimeout(init, 300);
  }
  var s = document.createElement('script');
  s.src = 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js';
  s.defer = true;
  s.onload = init;
  document.head.appendChild(s);
})();

