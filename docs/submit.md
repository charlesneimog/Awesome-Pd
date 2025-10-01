---
hide:
 - navigation
 - toc
---
<style>
  .md-typeset h1,
  .md-content__button {
    display: none;
  }
  .md-button {
      margin: auto 40px;
  }
</style>

<h3 align="center"> Submit Objects, Libraries and Pieces</h3>

We, Pd users, are a large and diverse community. Many artistic and research projects are developed by Pd users, programmers, and people from different backgrounds. However, we are missing a centralized place to share these contributions --- a space where people can submit their objects, pieces, and patches, and where the community can truly grow and be nourished by them.

---

<div align="center">
    <a class="md-button " id="new-object">New/Edit Object</a>
    <a class="md-button " id="new-piece">New/Edit Piece</a>
</div>




---
<iframe 
  id="submit-frame"
  scrolling="no"
  style="
    display: block;          /* sempre block para transição funcionar */
    width: 100%;
    height: 200px;            /* altura inicial */
    border: none;
    border-radius: 6px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    overflow: hidden;
    opacity: 0;               /* inicia invisível */
    transition: opacity 0.5s ease, height 0.5s ease;
  ">
</iframe>

<script>
var newObjectBtn = document.getElementById('new-object');
var newPieceBtn = document.getElementById('new-piece');
var iframe = document.getElementById('submit-frame');

function loadIframe(url) {
    iframe.style.opacity = 0;   // esconde antes de carregar
    iframe.src = url;
    iframe.style.height = "200px"; // altura inicial mínima
}

// Botões
newObjectBtn.addEventListener('click', (e) => {
    e.preventDefault();
    loadIframe("../submit-external/index.html");
});

newPieceBtn.addEventListener('click', (e) => {
    e.preventDefault();
    loadIframe("../submit-piece/index.html");
});

// Recebe altura do iframe e faz fade-in
window.addEventListener('message', function(event) {
    if (event.data.type === 'resize-iframe') {
        iframe.style.height = event.data.height + 'px';
        // Aplica fade-in suave
        setTimeout(() => {
            iframe.style.opacity = 1;
        }, 50); // curto delay para garantir renderização
    }
});
</script>

