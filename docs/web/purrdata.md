# purr-data

`Purr Data` is the latest (2.x) branch of Ivica Ico Bukvic's Pd-l2ork. Pd-l2ork in turn was a fork of Hans-Christoph Steiner's Pd-extended, which has been the longest-running (and arguably the most popular) variant of Miller Puckette's Pd. Pd a.k.a. Pure Data, the common basis of all these variants, is Miller Puckette's interactive and graphical computer music and multimedia environment. Pd is also the premier open-source alternative to Cycling74's well-known commercial Max program (whose original version was also developed by Miller Puckette when he was at IRCAM in the 1980s). There are a few other popular and very capable applications in the realm of computer music and media art, most notably Csound and SuperCollider. But Max and Pd's special appeal is that you work in an intuitive graphical "patching" environment which allows you to put together advanced real-time signal processing applications without having to learn a "real" programming language.

!!! tip "You can use the web version [here](https://charlesneimog.github.io/purr-data/)"
    


<h2>Contributors</h2>

<div id="libcontributors"></div>

<script>
async function updateList() {
    // https://github.com/agraef/purr-data
    const repoOwner = 'agraef';
    const repoName = 'purr-data';
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


