---
search:
    exclude: true
---

# else
`ELSE` is a big library of externals that extends the performance of Pd. `ELSE` provides a cohesive system for computer music; it also serves as a basis for a Live Electronics Tutorial by the same author, yours truly, Alexandre Torres Porres. This library's repository resides at https://github.com/porres/pd-else/. This tutorial is also included as part of the `ELSE` library download. Look for the 'Live-Electronics-Tutorial' folder inside it, and also check its README file for instructions on how to install it.
 `ELSE` is also part of [PlugData](https://plugdata.org/) by Timothy Schoen, which is a fork of Pd that loads as a standalone or VST with a revamped GUI. `ELSE` has received collaboration from Tim and others involved with PlugData, and many objects have been included in `ELSE` just so they are supported in PlugData.
`ELSE` also ships a modification of [pdlua](https://github.com/agraef/pd-lua), which is needed for a couple of GUI objects.
<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>


<script>
async function updateList() {
    const repoOwner = 'porres';
    const repoName = 'pd-else';
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
- :material-tune: [__bend.in__](../objects/bend.in.md) The `bend.in` object in Pure Data extracts MIDI Pitch Bend information from either a connected MIDI device (internal source) or raw MIDI input (external source).
- :material-tune: [__above~__](../objects/above~.md) The `above~` object in Pure Data monitors a signal input and outputs impulses based on a threshold.
- :material-tune: [__dust~__](../objects/dust~.md) The `dust~` object in Pure Data is a pseudo-random impulse generator that outputs positive random impulses (up to 1) according to a configurable density (rate) parameter.
- :material-tune: [__add__](../objects/add.md) The `add` object in Pure Data accumulates input values to a running sum, starting from a configurable initial value (0 by default).
- :material-tune: [__asr~__](../objects/asr~.md) The `asr~` object in Pure Data is an attack/sustain/release envelope generator, simplified compared to `adsr~`.
- :material-tune: [__above__](../objects/above.md) The `above` object in Pure Data monitors a float input and triggers events based on a threshold.
- :material-tune: [__plaits~__](../objects/plaits~.md) `plaits~` is a Pure Data external based on the "Plaits" macro-oscillator module by Mutable Instruments.
- :material-tune: [__abs.pd~__](../objects/abs.pd~.md) The `abs.pd~` object in Pure Data loads a `.pd` file into a subprocess, providing two signal inlets and two signal outlets.
- :material-tune: [__gendyn~__](../objects/gendyn~.md) `gendyn~` implements "Dynamic Strochastic Synthesis" based on Xenakis' GenDyn algorithm.
- :material-tune: [__giga.rev~__](../objects/giga.rev~.md) `giga.rev~` is a stereo reverb in Else based on Juhana Sadeharju’s *Gigaverb* algorithm, known for producing large, spacious, and dense reverberation tails.
- :material-tune: [__args__](../objects/args.md) The `args` object in Pure Data loads and manages the arguments of an abstraction, allowing them to be queried or changed dynamically.
- :material-tune: [__dispatch__](../objects/dispatch.md) The `dispatch` object in Pure Data takes a list and sends each element to specified receive addresses in left-to-right order.
- :material-tune: [__dir__](../objects/dir.md) The `dir` object in Pure Data is used to access and manage files from directories.
- :material-tune: [__changed~__](../objects/changed~.md) The `changed~` object in Pure Data monitors an input signal and outputs an impulse whenever the signal changes by an amount equal to or greater than a specified threshold.
</div>