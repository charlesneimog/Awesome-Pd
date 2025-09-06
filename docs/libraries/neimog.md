---
search:
    exclude: true
---

# neimog
**pd-neimog** is a collection of objects, tools, and integrations for **Pure Data (Pd)** that I use in my work. It focus on Signal Manipulation, Statistics, Music Information Retrieval (MIR), Python/Lua scripting, and include all my libraries: `pd-partialtrack`, `pd-saf`, `pd-vamp`, `pd-server`, `pd-ambi`, `pd-upic`, and also some libraries I fork, update or simply use: `kalman-pd` `SOFAlizer-for-pd` `earplug~`, and more
<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>


<script>
async function updateList() {
    const repoOwner = 'charlesneimog';
    const repoName = 'pd-neimog';
    try {
        const res = await fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/contributors`);
        const contributors = await res.json();
        const container = document.getElementById('libcontributors');
        contributors.forEach(user => {
            const link = document.createElement('a');
            link.href = `https://github.com/${user.login}`;
            link.target = '_blank';
            const img = document.createElement('img');
            img.src = `https://github.com/${user.login}.png?size=100`;
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


<h2>Objects</h2>

<div class="grid cards" markdown>
- :material-tune: [__l.readsvg__](../objects/l.readsvg.md) `l.readsvg` is a `pdlua` object designed to read SVG files created or edited in Inkscape.
- :material-tune: [__l.attrfilter__](../objects/l.attrfilter.md) The `l.attrfilter` object in Pure Data (using `pdlua`) filters elements from an SVG file loaded with `l.readsvg` based on attributes such as stroke, fill, or ID.
- :material-tune: [__a.sum__](../objects/a.sum.md) The `a.sum` object in Pure Data sums the last `x` numbers of an array.
- :material-tune: [__a.rotate__](../objects/a.rotate.md) The `a.rotate` object in Pure Data appends a number to the end of an array, making it useful for tracking or visualizing the history of sound parameters over time..
</div>