# slice~

`slice~` splits a multichannel signal. The 'n' split point is set via argument or float input. If you slice at 'n', the left outlet spits the first 'n' channels and the right outlet sends the remaining channels. If you slice at '-n', the right outlet spits the last 'n' channels and the left outlet sends the first channels. If the number of channels is less than the split point, the whole signal is output to the left if 'n' is positive (and the right outlet outputs zeros), and to the right if negative (and the left outlet outputs zeros).


---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ Use [Deken](../deken.md).  <p>_Found inside <code>else</code> library._</p>
- :fontawesome-brands-dev: Developed by **Alexandre Porres**.
- :fontawesome-brands-github: __Report Bugs/Errors__ [here](https://github.com/porres/pd-else/issues)!
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
    