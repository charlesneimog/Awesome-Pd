# Pieces

!!! warning "This is not ready yet!"

In this section we list all the pieces submit for the project. Note that, if there is some great piece is missing, please submit it using [Submit](submit.md) form. 

<h2 align="center"><b>Pieces</b></h2>

<div class="grid cards ">
    <ul id="random-pieces"></ul>
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
    const url = new URL('../all_pieces.json', window.location.href);
    const response = await fetch(url);
    if (!response.ok) throw new Error("Failed to load JSON");

    const categories = await response.json(); 
    const randomArticles = document.getElementById("random-pieces");

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

addPieces();

</script>
