# neuralnet

`neuralnet` is an artificial neural network Pd external, written in pure C, without any dependencies. It is inspired by the book "Neural Networks from Scratch in Python" by Harrison Kinsley & Daniel Kukieła. It is an attempt to translate the Python code to C with the Pure Data API, to run neural networks within Pd.

`neuralnet` creates densely connected neural networks for classification, regression, and binary logistic regression. There are different activation functions and optimizers you can set, and various other settable parameters. The object's help patch and the examples found in the examples directory should cover all the necessary information.

---
<div class="grid cards" markdown>
- :octicons-download-16: __Download__ via [Deken](../deken.md).
- :fontawesome-brands-dev: Library developed mainly by **Alexandros Drymonitis**.
- :fontawesome-solid-bug-slash: __Report Bugs/Errors__ [here](https://github.com/alexdrymonitis/neuralnet/issues)!
- :fontawesome-solid-computer: __Available__ for :fontawesome-brands-apple: :fontawesome-brands-linux: :fontawesome-brands-windows:.
</div><h3>Articles</h3>

<div class="grid cards" markdown>
- :octicons-book-24: 
    <h4>[neuralnet]: A Pure Data External for the Creation of Neural Networks Written in Pure C</h4>
    *by Alexandros Drymonitis*

    [Link](https://aimc2023.pubpub.org/pub/3j3fx7y1/release/1)
</div>



---

<h3>Comments</h3>

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
    
<h3>Contributors</h3>

<div id="avatars"></div>

<script>
const nicknames = ["charlesneimog"];
const container = document.getElementById('avatars');
nicknames.forEach(nick => {
  const link = document.createElement('a');
  link.href = `https://github.com/${nick}`;
  link.target = '_blank'; // opens in new tab
  const img = document.createElement('img');
  img.src = `https://github.com/${nick}.png`;
  img.alt = nick;
  img.className = 'avatar';
  link.appendChild(img);
  container.appendChild(link);
});
</script>
    