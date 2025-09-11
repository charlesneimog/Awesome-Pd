---
search:
    exclude: true
---

# buffer~

The `buffer~` object stores audio data in memory as a multichannel array, supporting up to 64 channels. It enables reading from and writing to audio files (`.wav`, `.aif`, `.caf`), and its contents can be manipulated through messages for operations like waveform generation, gain adjustment, or applying windowing functions. It integrates with other Cyclone objects for playback and processing, and its internal arrays are accessible by vanilla Pd objects.

---

!!! info "AI Generated"
    This content was generated with the assistance of AI. If you notice any errors, please report them or submit a fix using [Submit](../../submit.md). Check the prompt used [here](../../prompts/helppatchai.md).

---

<div class="grid cards" markdown>
- :octicons-download-16: __Download__ via [Deken](../../deken.md).  <p style="font-size: 14px">_Open `Pd` and go to `Tools`:material-arrow-right:`Find Externals`. Search for <code>cyclone</code> and install it. Then create an object with `declare -lib cyclone -path cyclone`. Finally, use `buffer~` or any other object from `cyclone`._</p>
- :fontawesome-brands-dev: Library developed mainly by **Alexandre Torres Porres**.
- :fontawesome-solid-bug-slash: __Report Bugs/Errors__ [here](https://github.com/porres/pd-cyclone/issues)!
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
    