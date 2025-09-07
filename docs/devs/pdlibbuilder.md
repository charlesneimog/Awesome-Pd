# pd-lib-builder

`Makefile.pdlibbuilder` is a helper **Makefile** designed to streamline the building of **Pure Data (Pd) external libraries**.  

### Key points
- Created by Katja Vetter (2015) and released to the public domain.  
- Developed further as a Pd community project.  
- Inspired by Hans Christoph Steiner’s *Makefile Template* and Stephan Beal’s *ShakeNMake*.  
- Requires **GNU make ≥ 3.81**.  

### Purpose

- Provides a standardized and portable way to compile Pd externals.  
- Handles platform differences (Linux, macOS, Windows) automatically.  
- Reduces complexity compared to writing custom Makefiles.


!!! tip "Use `msys2` on Windows"
    On windows it is easiear to use `msys2` to build objects with `pd-lib-builder`. You can install `msys2` running `winget install msys2.msys2` or check [https://www.msys2.org/](https://www.msys2.org/).
    
<h2>Contributors</h2>

<div id="libcontributors"></div>

<script>
async function updateList() {
    const repoOwner = 'pure-data';
    const repoName = 'pd-lib-builder';
    try {
        const res = await fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/contributors`);
        const contributors = await res.json();
        const container = document.getElementById('libcontributors');
        contributors.forEach(user => {
            console.log(user);
            const link = document.createElement('a');
            link.href = `https://github.com/${user.login}`;
            link.target = '_blank';
            const img = document.createElement('img');
            img.src = `${user.avatar_url}`;
            img.alt = user.login;
            img.className = 'libavatar';
            link.appendChild(img);
            container.appendChild(link);
        });
    } catch(err) {
        console.error(err);
    }
}
updateList();
</script>


---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ [here](https://github.com/pure-data/pd.cmake).
- :fontawesome-brands-dev: Developed by **Pierre Guiellot, Charles K. Neimog, and others**.
- :fontawesome-brands-github: __Report Bugs__ [here](https://github.com/pure-data/pd.cmake/issues)!
- :fontawesome-solid-computer: __Available__ for :fontawesome-brands-apple: :fontawesome-brands-linux: :fontawesome-brands-windows:.
</div>
---
<h3>Videos</h3>

<div style="display: flex; justify-content: center; gap: 20px;">
    <iframe style="border-radius: 8px" width="560" height="315" src="https://www.youtube.com/embed/XCs1uzWj2IA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

---

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
