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

---

<div align="center">
    <a class="md-button " id="new-object">New Object</a>
    <a class="md-button " id="new-piece">New Piece</a>
</div>

---

<iframe 
  id="submit-frame"
  style="width: 100%; border: none; border-radius: 6px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); overflow:hidden;">
</iframe>


<script>
  var newObjectBtn = document.getElementById('new-object');
  var newPieceBtn = document.getElementById('new-piece');

  // Adiciona listener de clique
    newObjectBtn.addEventListener('click', (event) => {
        event.preventDefault();
        var iframe = document.getElementById('submit-frame');
        iframe.src = "../submit-external/index.html";

        iframe.onload = function () {
            // Get the content height
            const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
            const height = iframeDocument.body.scrollHeight;

            iframe.style.width = "100%";
            iframe.style.height = height + "px";
        }
    });

  newPieceBtn.addEventListener('click', (event) => {
    event.preventDefault();
        var iframe = document.getElementById('submit-frame');
        iframe.src = "../submit-piece/index.html";

        iframe.onload = function () {
            // Get the content height
            const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
            const height = iframeDocument.body.scrollHeight;

            iframe.style.width = "100%";
            iframe.style.height = height + "px";
        }
    // Coloque aqui a ação que deseja
  });
</script>
