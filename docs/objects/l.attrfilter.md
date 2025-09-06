# l.attrfilter

The `l.attrfilter` object in Pure Data (using `pdlua`) filters elements from an SVG file loaded with [`l.readsvg`](l.readsvg.md) based on attributes such as stroke, fill, or ID. For example, `l.attrfilter fill #ff0000` outputs only the elements with red fill (#ff0000). It allows selective processing and visualization of SVG content in Pd.

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ Use [Deken](../deken.md).  <p>_Found inside <code>neimog</code> library._</p>
- :fontawesome-brands-dev: Developed by **Charles K. Neimog**.
- :fontawesome-brands-github: __Report Bugs/Errors__ [here](https://github.com/charlesneimog/pd-neimog/issues)!
- :fontawesome-solid-computer: __Available__ for :fontawesome-brands-apple: :fontawesome-brands-linux: :fontawesome-brands-windows:.
</div>

---
<h3>Music</h3>

<div style="display: flex; justify-content: center; gap: 20px;">
    <iframe style="border-radius: 8px" width="560" height="315"
        src="https://www.youtube.com/embed/CuJsBlbFBeM"
        title="YouTube video player" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

---


---

<h3>Comments</h3>

<script src="https://giscus.app/client.js"
    data-repo="charlesneimog/Awesome-PD"
    data-repo-id="R_kgDOLaunFg"
    data-category="Comments"
    data-category-id="DIC_kwDOLaunFs4CnXHy"
    data-mapping="title"
    data-strict="0"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="preferred_color_scheme"
    data-lang="en"
    data-loading="lazy"
    crossorigin="anonymous"
    async>
</script>
    
<h3>Contributors</h3>

<div id="avatars"></div>

<script>
const nicknames = ["charlesneimog"];
const container = document.getElementById('avatars');
nicknames.forEach(nick => {
  const link = document.createElement('a');
  link.href = `https://github.com/${nick}`;
  link.target = '_blank'; // opens in new tab
  const img = document.createElement('img');
  img.src = `https://github.com/${nick}.png`;
  img.alt = nick;
  img.className = 'avatar';
  link.appendChild(img);
  container.appendChild(link);
});
</script>
    