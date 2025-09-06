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
</style>

<iframe 
  id="submit-frame"
  src="../submit-external/index.html"
  style="width: 100%; border: none; border-radius: 6px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); overflow:hidden;">
</iframe>


<script>
window.addEventListener("message", (event) => {
    const submitframe = document.getElementById("submit-frame");
    if (event.data.type === "resize-iframe") {
        submitframe.style.height = event.data.height + "px";
    }
});
</script>
