# Objects

In this section we list all the objects submit for the project. Note that, if there is some great object is missing, please submit it using [Submit](submit.md) form. It is very simple and easy. If you did some piece, publish article or recorded a Video for some object and it is not listed here also submit it. 

!!! tip "AI Classification"
    These libraries are extensive, and the first step involves AI-based classification. If you notice an error, please click "Submit" enter the object name, and update its description and classification.

<h2 align="center"><b>Random Objects</b></h2>

<div class="grid cards ">
    <ul id="random-objects"></ul>
</div>


<script>
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // troca
    }
    return array;
}

async function addObjects() {
    const url = new URL('../all_objects.json', window.location.href);
    const response = await fetch(url);
    if (!response.ok) throw new Error("Failed to load JSON");

    const categories = await response.json(); 
    const randomObjects = document.getElementById("random-objects");
    const randomVideos = document.getElementById("random-videos");
    const randomArticles = document.getElementById("random-article");

    // Shuffle and pick 6
    const selected = shuffleArray([...categories]).slice(0, 4);

    let videos = []
    let articles = []

    for (const item of selected) {
        const li = document.createElement("li");

        // Span with twemoji class
        const span = document.createElement("span");
        span.classList.add("twemoji");

        // Fetch individual object JSON
        const objurl = new URL(`../objects/${item}.json`, window.location.href);
        const objjson = await fetch(objurl);
        if (!objjson.ok) throw new Error("Failed to load JSON for " + item);
        const objresult = await objjson.json();
        let description = objresult["description"];
        let firstSentence = description.split(". ")[0];

        // Create link
        const a = document.createElement("a");
        const objmdurl = new URL(`${item}`, window.location.href);
        a.href = objmdurl;
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
