# bend.in

The `bend.in` object in Pure Data extracts MIDI Pitch Bend information from either a connected MIDI device (internal source) or raw MIDI input (external source). By default, it outputs normalized values from -1 to 1, but with the `-raw` flag it outputs integers in the range 0–16383. It supports MIDI channel selection via argument or right inlet, with channel 0 as omni mode, and can be set to listen exclusively to external sources using the `-ext` flag. Port numbers are encoded into channel numbers, extending the channel mapping across multiple ports.

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ via [Deken](../deken.md).  <p style="font-size: 14px">_Open `Pd` and go to `Tools`:material-arrow-right:`Find Externals`. Search for <code>else</code> and install it. Then create an object with `declare -lib else -path else`. Finally, use `bend.in` or any other object from `else`._</p>
- :fontawesome-brands-dev: Library developed mainly by **Alexandre Porres**.
- :fontawesome-solid-bug-slash: __Report Bugs/Errors__ [here](https://github.com/porres/pd-else/issues)!
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
    