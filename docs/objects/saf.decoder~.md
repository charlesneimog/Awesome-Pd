# saf.decoder~

The `saf.decoder~` object in Pure Data implements a frequency-dependent Ambisonic decoder for loudspeakers and headphones. It supports up to 128 user-defined loudspeaker directions or presets for common 2D and 3D layouts. For headphones, it performs virtual loudspeaker decoding using interpolated HRTFs, with support for importing custom HRIRs via the SOFA standard. The decoder allows different settings for low and high frequencies with a user-defined crossover, offering integrated methods such as AllRAD, EPAD, and Mode-Matching, along with max-rE spatial weighting. It also provides options for adjusting decoding order and normalization (EP/AP) to maintain consistent loudness, which is useful for both practical and creative applications.

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ via [Deken](../deken.md).  <p style="font-size: 14px">_Open `Pd` and go to `Tools`:material-arrow-right:`Find Externals`. Search for <code>neimog</code> and install it. Then create an object with `declare -lib neimog -path neimog`. Finally, use `saf.decoder~` or any other object from `neimog`._</p>
- :fontawesome-brands-dev: Library developed mainly by **Charles K. Neimog**.
- :fontawesome-solid-bug-slash: __Report Bugs/Errors__ [here](https://github.com/charlesneimog/pd-neimog/issues)!
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
    