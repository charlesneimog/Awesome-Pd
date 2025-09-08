# phaseshift~

`phaseshift~` is a 2nd allpass filter, which keeps the gain and only alters the phase from 0 (at 0 hz) to 360º (at the Nyquist frequency). The frequency at which it shifts to 180º is specified as the filter's frequency (minimum 1o hz) and the steepness of the curve is determined by the Q parameter - see graph below.


---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ via [Deken](../deken.md).  <p style="font-size: 14px">_Open `Pd` and go to `Tools`:material-arrow-right:`Find Externals`. Search for <code>cyclone</code> and install it. Then create an object with `declare -lib cyclone -path cyclone`. Finally, use `phaseshift~` or any other object from `cyclone`._</p>
- :fontawesome-brands-dev: Library developed mainly by **Alexandre Porres**.
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
    