# asr~

The `asr~` object in Pure Data is an attack/sustain/release envelope generator, simplified compared to `adsr~`. It can be triggered by gate values, bangs, or impulses: a gate on starts the attack phase and a gate off triggers the release phase, with an optional immediate release mode via the `-rel` flag. Attack and release times are set in milliseconds, and the curve parameter controls the envelope shape, allowing exponential, linear (`-lin`), or lag-filter (`-lag`) behavior. The object accepts both control and signal inputs, with gate values mapped to the MIDI velocity range or beyond. Its right outlet outputs a status signal (1 when active, 0 when inactive), useful for managing DSP switches in subpatches or abstractions. While typically used for amplitude shaping, `asr~` can modulate any parameter in real time.

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ Use [Deken](../deken.md).  <p>_Found inside <code>else</code> library._</p>
- :fontawesome-brands-dev: Developed by **Alexandre Porres**.
- :fontawesome-brands-github: __Report Bugs/Errors__ [here](https://github.com/porres/else)!
- :fontawesome-solid-computer: __Available__ for :fontawesome-brands-apple: :fontawesome-brands-linux: :fontawesome-brands-windows:.
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
