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
<h2 align="center"><b>Random Objects</b></h2>

<div class="grid cards adaptable">
    <ul id="random-objects"></ul>
</div>

---
<h2 align="center"><b>Random Videos</b></h2>

<div id="random-videos" class="videos-container"></div>

--- 

<script>
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // troca
    }
    return array;
}

async function addObjects() {
    const response = await fetch(`${window.location.href}/all_objects.json`);
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
        const objjson = await fetch(`${window.location.href}/objects/${item}.json`);
        if (!objjson.ok) throw new Error("Failed to load JSON for " + item);
        const objresult = await objjson.json();
        let description = objresult["description"];
        let firstSentence = description.split(". ")[0];

        // Create link
        const a = document.createElement("a");
        a.href = `${window.location.href}/objects/${item}`;
        a.innerHTML = `<strong><code>${item}</code></strong>`;

        span.appendChild(a);

        let html = firstSentence.replace(/`([^`]+)`/g, "<code>$1</code>");
        html = html.replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");

        const p = document.createElement("p");
        p.innerHTML = `${html}.`
        li.appendChild(span);
        li.appendChild(p);

        randomObjects.appendChild(li);

        if (objresult["videos"]) videos.push(...objresult["videos"]);
        if (objresult["musics"]) videos.push(...objresult["musics"]);
        if (objresult["articles"]) articles.push(...objresult["articles"]);
    }

    // filter to avoid tendencies
    videos = videos.filter(
      (item, index, self) =>
        index === self.findIndex((v) => v.link === item.link)
    );


    // random videos
    const selectedVideos = shuffleArray([...videos]).slice(0, 2);

    selectedVideos.forEach(v => {
        let url = v.link || v; 
        let videoId = null;

        const match1 = url.match(/v=([^&]+)/);
        if (match1) videoId = match1[1];

        const match2 = url.match(/youtu\.be\/([^?&]+)/);
        if (match2) videoId = match2[1];

        if (videoId) {
            url = `https://www.youtube.com/embed/${videoId}`;
            const iframe = document.createElement("iframe");
            iframe.width = "45%";  // overridden by CSS on small screens
            iframe.height = "350px"; // overridden by CSS on small screens
            iframe.src = url;
            iframe.frameBorder = "0";
            iframe.allowFullscreen = true;
            randomVideos.appendChild(iframe);
        }
    });

    // // random articles
    // const selectedArticles = shuffleArray([...articles]).slice(0, 4);
    // selectedArticles.forEach(v => {
    //     let url = v.link || v; 
    //
    //     const li = document.createElement("li");
    //     li.style.marginBottom = "1.5em";       // space between list items
    //
    //     // Link container (title)
    //     const a = document.createElement("a");
    //     a.href = url;
    //     a.innerHTML = `<strong><code>${v.title}</code></strong>`;
    //     a.classList.add("twemoji");
    //     a.style.display = "block";             // ensures full width
    //     a.style.wordWrap = "break-word";       // prevent overflow for long titles
    //
    //     li.appendChild(a);
    //     randomArticles.appendChild(li);
    // });
}

addObjects();

</script>

