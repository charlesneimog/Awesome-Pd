# pd4web

`pd4web` enables PureData functionality directly in web browsers. Not just the vanilla Pd, but Pd with all the externals!

<h2>Contributors</h2>

<div id="libcontributors"></div>

<script>
async function updateList() {
    const repoOwner = 'charlesneimog';
    const repoName = 'pd4web';
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

<h2>Key Features</h2>

* Streamlined Development: Create fully online audio applications with a visual approach.
* Easy Access: Performers can access compositions without complex PureData setups or library dependencies.
* Live Electronic Music Preservation: Explore the potential of WebAudioApps to maintain the integrity of live electronic works. `pd4web` will download and make a repository for all code you need to run your music.

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ [here](https://github.com/charlesneimog/pd4web).
- :fontawesome-brands-dev: Developed by **Charles K. Neimog**.
- :fontawesome-brands-github: __Report Bugs/Errors__ [here](https://github.com/charlesneimog/pd4web/issues)!
- :fontawesome-solid-computer: __Available__ for :material-web:.
</div>

---
<h3>Music</h3>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; justify-items: start;">
    <iframe style="border-radius: 8px" width="560" height="315" src="https://www.youtube.com/embed/ym5nmBIzyh0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
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
