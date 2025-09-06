# saf.encoder~

The `saf.encoder~` object in Pure Data implements the Ambisonic encoder from the SPARTA VST3 plugins suite. It encodes up to 128 input channels into Ambisonic signals at specified directions, creating a synthetic sound scene whose spatial resolution depends on the encoding order. Presets are included for common multichannel formats (e.g., 22.x) to 1st–10th order Ambisonics. The object also provides a mouse-driven panning window with an equirectangular sphere representation for visualizing and adjusting azimuth and elevation of sources.

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ Use [Deken](../deken.md).  <p>_Found inside <code>neimog</code> library._</p>
- :fontawesome-brands-dev: Developed by **Charles K. Neimog**.
- :fontawesome-brands-github: __Report Bugs/Errors__ [here](https://github.com/charlesneimog/pd-neimog)!
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
    