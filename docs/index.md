---
hide:
 - navigation
 - toc
---
<style>
  .md-typeset h1,
  .md-content__button {
    display: none;
  }
</style>

# Home

<p align="center">
  WebSite that tries to list, with descriptiors, music examples, and links, all the objects, externals, and libraries available for PureData.
</p>


--- 
<h2 align="center"><b>Check some objects</b></h2>

<div class="grid cards">
    <ul id="random-objects"></ul>
</div>

<script>
async function addObjects() {
    const response = await fetch("../all_objects.json");
    if (!response.ok) throw new Error("Failed to load JSON");

    const categories = await response.json(); 
    const randomObjects = document.getElementById("random-objects");

    // Shuffle and pick 6
    const shuffled = categories.sort(() => 0.5 - Math.random());
    const selected = shuffled.slice(0, 6);

    for (const item of selected) {
        const li = document.createElement("li");

        // Span with twemoji class
        const span = document.createElement("span");
        span.classList.add("twemoji");

        // Fetch individual object JSON
        const objjson = await fetch(`../objects/${item}.json`);
        if (!objjson.ok) throw new Error("Failed to load JSON for " + item);
        const objresult = await objjson.json();
        let description = objresult["description"];
        let firstSentence = description.split(". ")[0];

        // Create link
        const a = document.createElement("a");
        a.href = `./../objects/${item}`;
        a.innerHTML = `<strong><code>${item}</code></strong>`;

        span.appendChild(a);

        let html = firstSentence.replace(/`([^`]+)`/g, "<code>$1</code>");
        html = html.replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");

        const p = document.createElement("p");
        p.innerHTML = `${html}.`
        li.appendChild(span);
        li.appendChild(p);
        randomObjects.appendChild(li);
    }
}

addObjects();

</script>

