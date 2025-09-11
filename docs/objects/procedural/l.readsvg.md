# l.readsvg

`l.readsvg` is a `pdlua` object designed to read SVG files created or edited in Inkscape.  
It belongs to the `pdlua` project **pd-upic**, which—as the name suggests—is related to the **UPIC** system developed by Iannis Xenakis.  

The object can **read** and **play** drawings, provided they follow specific rules explained in this [guide](https://charlesneimog.github.io/blog/posts/pd-upic.html).

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ via [Deken](../../deken.md).  <p style="font-size: 14px">_Open `Pd` and go to `Tools`:material-arrow-right:`Find Externals`. Search for <code>neimog</code> and install it. Then create an object with `declare -lib neimog -path neimog`. Finally, use `l.readsvg` or any other object from `neimog`._</p>
- :fontawesome-brands-dev: Library developed mainly by **Charles K. Neimog**.
- :fontawesome-solid-bug-slash: __Report Bugs/Errors__ [here](https://github.com/charlesneimog/pd-neimog/issues)!
- :fontawesome-solid-computer: __Available__ for :fontawesome-brands-apple: :fontawesome-brands-linux: :fontawesome-brands-windows:.
</div>---
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
    