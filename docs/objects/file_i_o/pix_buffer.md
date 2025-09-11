---
search:
    exclude: true
---

# pix_buffer

`pix_buffer` is a named storage object for images, functioning similarly to a table but without direct visual access to its contents. It can store images of varying dimensions and color spaces, dynamically allocating memory or pre-allocating it via the `allocate` message. Images can be written to or read from the buffer using associated objects like `pix_buffer_write` and `pix_buffer_read`, and it supports loading from and saving to files.

---

!!! info "AI Generated"
    This content was generated with the assistance of AI. If you notice any errors, please report them or submit a fix using [Submit](../../submit.md). Check the prompt used [here](../../prompts/helppatchai.md).

---

<div class="grid cards" markdown>
- :octicons-download-16: __Download__ via [Deken](../../deken.md).  <p style="font-size: 14px">_Open `Pd` and go to `Tools`:material-arrow-right:`Find Externals`. Search for <code>zexy</code> and install it. Then create an object with `declare -lib zexy -path zexy`. Finally, use `pix_buffer` or any other object from `zexy`._</p>
- :fontawesome-brands-dev: Library developed mainly by **Johannes M. Zmölnig**.
- :fontawesome-solid-bug-slash: __Report Bugs/Errors__ [here](https://github.com/umlaeute/Gem/issues)!
- :fontawesome-solid-computer: __Available__ for :fontawesome-brands-apple: :fontawesome-brands-linux: :fontawesome-brands-windows:.
</div>

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
    