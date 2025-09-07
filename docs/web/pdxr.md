# PdXR

`PdXR` is an open-source implementation of PureData for multiuser Metaverse environments. Use a Pd patch with your VR or AR devices together with other people in a shared virtual environment.
    


<div id="libcontributors"></div>

<script>
async function updateList() {
    // not work for some reason
    const repoOwner = 'AudioGroupCologne';
    const repoName = 'PdXR';
    try {
        const res = await fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/contributors`);
        const contributors = await res.json();
        const container = document.getElementById('libcontributors');
        console.log(contributors);
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
- :octicons-download-16: __Download__ [here](https://github.com/charlesneimog/purr-data).
- :fontawesome-brands-github: __Report Bugs/Errors__ [here](https://github.com/charlesneimog/purr-data/issues)!
- :fontawesome-solid-computer: __Available__ for :material-web:.
</div>

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



