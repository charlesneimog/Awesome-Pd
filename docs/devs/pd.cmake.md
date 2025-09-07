# pd.cmake

`pd.cmake` is a collection of CMake scripts designed to simplify the process of creating build projects for Pure Data (Pd) externals.  
It provides a unified, cross-platform way to generate build files (Makefiles, Xcode projects, Visual Studio solutions, etc.) for Pd externals using CMake.  


### Purpose
    
- Automates the setup of CMake projects for Pd external development.  
- Ensures compatibility across multiple operating systems and IDEs.  
- Reduces boilerplate by providing reusable CMake modules specific to Pd.  

### Use case 
Instead of manually writing platform-specific build scripts, developers can use `pd.cmake` to quickly generate the necessary build environment for compiling Pd externals.

<h2>Contributors</h2>

<div id="libcontributors"></div>

<script>
async function updateList() {
    const repoOwner = 'pure-data';
    const repoName = 'pd.cmake';
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
    <iframe style="border-radius: 8px" width="560" height="315" src="https://www.youtube.com/embed/hSrqAE56J0g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
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
