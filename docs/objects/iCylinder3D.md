# iCylinder3D

The `iCylinder3D` object simulates the interaction between a 'mass' and a 3D cylinder. It allows users to define the cylinder's geometry (center, orientation, radius, height) and configure various physical interaction properties such as normal and tangential forces, rigidity, damping, and displacement. These properties can be constant or proportional to distance, enabling detailed physical modeling within a 3D space.

---

!!! info "AI Generated"
    This content was generated with the assistance of AI. If you notice any errors, please report them or submit a fix using [Submit](../submit.md). Check the prompt used [here](../prompts/helppatchai.md).

---

<div class="grid cards" markdown>
- :octicons-download-16: __Download__ via [Deken](../deken.md).  <p style="font-size: 14px">_Open `Pd` and go to `Tools`:material-arrow-right:`Find Externals`. Search for <code>pmpd</code> and install it. Then create an object with `declare -lib pmpd -path pmpd`. Finally, use `iCylinder3D` or any other object from `pmpd`._</p>
- :fontawesome-brands-dev: Library developed mainly by **Cyrille Henry**.
- :fontawesome-solid-bug-slash: __Report Bugs/Errors__ [here](https://github.com/ch-nry/pd-pmpd/issues)!
- :fontawesome-solid-computer: __Available__ for :fontawesome-brands-apple: :fontawesome-brands-linux: :fontawesome-brands-windows:.
</div><h3>Articles</h3>

<div class="grid cards" markdown>
- :octicons-book-24: 
    <h4>Physical modeling for pure data (PMPD) and real-time interaction with an audio synthesis</h4>
    *by Cyrille Henry*

    [Link](https://hal.science/hal-03354371/)
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
    