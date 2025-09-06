# nn~

`nn~` is a bridge between **Max/MSP** or **PureData** and **LibTorch** (PyTorch C++ interface) for deep learning. It does not work alone and requires pretrained models.

### Key Points

- **Purpose:** Allows deep learning models to run inside Max/MSP or PureData.  
- **Dependencies:** Pretrained models in **TorchScript (`.ts`) format**.  
- **Model Management:**
  - Place `.ts` files in `nn_tilde/models` or any folder accessible through Max/Pd filesystem:
    - **Max:** Options → File Preferences  
    - **PureData:** File → Preferences → Path
  - Since v1.6.0, some models can be downloaded via **IRCAM Forum API**.  
- **Usage:** Load a model by specifying its name as the first argument to `nn~`:

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ [here](https://github.com/acids-ircam/nn_tilde) or use [Deken](../deken.md)..
- :fontawesome-brands-dev: Developed by **ACIDS/Ircam**.
- :fontawesome-brands-github: __Report Bugs/Errors__ [here](https://github.com/acids-ircam/nn_tilde/issues)!
- :fontawesome-solid-computer: __Available__ for :fontawesome-brands-apple: :fontawesome-brands-linux: :fontawesome-brands-windows:.
</div>

<h3>Articles</h3>

<div class="grid cards" markdown>
- :octicons-book-24: 
    <h4>Hierarchical temporal learning for multi-instrument and orchestral audio synthesis</h4>
    *by Hierarchical temporal learning for multi-instrument and orchestral audio synthesis*

    [Link](https://theses.hal.science/tel-04137258)
</div>

---
<h3>Videos</h3>

<div style="display: flex; justify-content: center; gap: 20px;">
    <iframe style="border-radius: 8px" width="560" height="315"
        src="https://www.youtube.com/embed/Dy1WTc022rQ"
        title="YouTube video player" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <iframe style="border-radius: 8px" width="560" height="315"
        src="https://www.youtube.com/embed/zBkDPgTyVCY"
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
    