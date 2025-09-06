# abs.pd~

The `abs.pd~` object in Pure Data loads a `.pd` file into a subprocess, providing two signal inlets and two signal outlets. It allows sending messages to the subprocess, starting it with `start <symbol>`, stopping it with `stop`, and opening its GUI with a click or the `show` message. If given a symbol argument, it automatically loads and starts the subprocess with DSP enabled; otherwise, it can be started manually. It also supports receiving MIDI data from devices connected to the parent process.

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ Use [Deken](../deken.md).  <p>_Found inside <code>else</code> library._</p>
- :fontawesome-brands-dev: Developed by **Alexandre Porres**.
- :fontawesome-brands-github: __Report Bugs/Errors__ [here](https://github.com/porres/else/issues)!
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
    