---
search:
    exclude: true
---

# piro
`piro` is Pd-port of `irmeasure~` and `multiconvolve~` from the HISSTools Impulse Response Toolbox (HIRT) · Stands for *Pd Impulse Response Objects*, or "fire" (ancient Greek), or sounds like "Pirro" (Pyrrhus) – since this port took a very long period!
<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>

<script>
async function updateList() {
    let repoOwner = 'd-i-s';
    let repoName = 'piro';
    try {
        let res = await fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/contributors`);
        let contributors = await res.json();
        let container = document.getElementById('libcontributors');
        contributors.forEach(user => {
            let link = document.createElement('a');
            link.href = `https://github.com/${user.login}`;
            link.target = '_blank';
            let img = document.createElement('img');
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
- :material-tune: [__irmanip__](../objects/general_utilities/irmanip.md) `irmanip` is a utility object designed for comprehensive manipulation of Impulse Response (IR) data stored in buffers.
- :material-tune: [__irmeasure~__](../objects/descriptors/irmeasure~.md) The `irmeasure~` object is designed for measuring Impulse Responses (IRs) of acoustic systems using various test signals like Exponential Sine Sweeps (ESS), maximum length sequences, or different types of noise.
- :material-tune: [__multiconvolve~__](../objects/reverb/multiconvolve~.md) The `multiconvolve~` object performs real-time convolution with configurable zero- or low-latency modes.
</div>