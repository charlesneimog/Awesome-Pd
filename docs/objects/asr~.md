# asr~

The `asr~` object in Pure Data is an attack/sustain/release envelope generator, simplified compared to `adsr~`. It can be triggered by gate values, bangs, or impulses: a gate on starts the attack phase and a gate off triggers the release phase, with an optional immediate release mode via the `-rel` flag. Attack and release times are set in milliseconds, and the curve parameter controls the envelope shape, allowing exponential, linear (`-lin`), or lag-filter (`-lag`) behavior. The object accepts both control and signal inputs, with gate values mapped to the MIDI velocity range or beyond. Its right outlet outputs a status signal (1 when active, 0 when inactive), useful for managing DSP switches in subpatches or abstractions. While typically used for amplitude shaping, `asr~` can modulate any parameter in real time.

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ via [Deken](../deken.md).  <p style="font-size: 14px">_Open `Pd` and go to `Tools`:material-arrow-right:`Find Externals`. Search for <code>else</code> and install it. Then create an object with `declare -lib else -path else`. Finally, use `asr~` or any other object from `else`._</p>
- :fontawesome-brands-dev: Library developed mainly by **Alexandre Porres**.
- :fontawesome-solid-bug-slash: __Report Bugs/Errors__ [here](https://github.com/porres/else)!
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
    