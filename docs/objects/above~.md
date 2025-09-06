# above~

The `above~` object in Pure Data monitors a signal input and outputs impulses based on a threshold. Its **left outlet** sends an impulse when the input signal rises above the set threshold, and its **right outlet** sends an impulse when the signal falls back to or below the threshold. The threshold can be specified as an argument when creating the object or via the **second inlet**. If no threshold is set, `above~` behaves similarly to `zerocross~`. It accepts both float and signal inputs and is useful for detecting crossings in audio-rate signals.

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
