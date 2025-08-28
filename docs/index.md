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

# Home

<p align="center">
  WebSite that tries to list, with descriptiors, music examples, and links, all the objects, externals, and libraries available for PureData.
</p>


--- 

<h2 align="center"><b>Check some objects</b></h2>


<div class="grid cards" >
    <ul>
        <li><span class="twemoji"></span></li>
        <li><span class="twemoji">segundo teste</span></li>
        <li><span class="twemoji">terceiro teste</span></li>
        <li><span class="twemoji">quarto teste</span></li>
    </ul>
</div>



<script>
async function addobjects(){
    const response = await fetch("../submit/categories.json");
    if (!response.ok) throw new Error("Failed to load JSON");
    const categories = await response.json();
}

addobjects();

</script>
