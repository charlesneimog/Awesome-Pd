# vstplugin~

`vstplugin~` is part of vstplugin v0.6.0, a project that enables the use of VST2 and VST3 plugins in Pure Data (Pd) on Windows, macOS, and Linux. It supports audio, MIDI, and instrument plugins; parameter automation (sample accurate for VST3); multi-bus input/output; native or generic GUIs; preset management; MIDI I/O; tempo and transport sync; offline rendering; and plugin discovery in standard or custom paths. Additional features include bit-bridging, sandboxing, Windows plugin support on Linux via Wine, and optional multithreaded processing.

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ Use [Deken](../deken.md).
- :fontawesome-brands-dev: Developed by **Christof Ressi**.
- :fontawesome-brands-github: __Report Bugs/Errors__ [here](https://git.iem.at/pd/vstplugin/issues)!
- :fontawesome-solid-computer: __Available__ for :fontawesome-brands-apple: :fontawesome-brands-linux: :fontawesome-brands-windows:.
</div>

<h3>Articles</h3>

<div class="grid cards" markdown>
- :octicons-book-24: 
    <h4>[vstplugin~] – A Pd external for hosting VST plugins</h4>
    *by Christof Ressi*

    [Link](https://doi.org/10.33871/23179937.2021.9.2.20)
</div>

---
<h3>Videos</h3>

<div style="display: flex; justify-content: center; gap: 20px;">
    <iframe style="border-radius: 8px" width="560" height="315"
        src="https://www.youtube.com/embed/Cs0NPime0kU"
        title="YouTube video player" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
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
    