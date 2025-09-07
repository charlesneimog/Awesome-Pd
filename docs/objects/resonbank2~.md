# resonbank2~

`resonbank2~` is a bank of resonators made of `resonator2~` objects. The design and structure here is different than `resonator2~` in order to make it better suited for sound synthesis. It has the same design as `resonbank~` and has a list of partials for each resonator and a frequency multiplier in the left inlet, kinda like `oscbank~`. The mid inlet the trigger (or excitation) signal (kinda like `pluck~`) - this must be an impulse since noise sources and noise bursts generate very loud outputs! The rightmost inlet is a time multiplier for the decay times. The number of filters is set via the parameter list size (such as the partial list). There's also support for multichannel output.


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
    