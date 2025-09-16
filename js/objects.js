function getOriginUrl() {
    let rawUrl = window.location.origin;
    if (rawUrl.includes("charlesneimog.github.io")) {
        rawUrl += "/Awesome-Pd/";
    } else {
        rawUrl = "";
    }
    return rawUrl;
}


function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // troca
    }
    return array;
}

async function addObjects(render_videos) {
    const response = await fetch(`${getOriginUrl()}/all_objects.json`);
    if (!response.ok) throw new Error("Failed to load JSON");

    const categories = await response.json();
    const randomObjects = document.getElementById("random-objects");
    const randomVideos = document.getElementById("random-videos");
    const randomArticles = document.getElementById("random-article");
    while (randomObjects.firstChild) {
        randomObjects.removeChild(randomObjects.firstChild);
    }

    // Shuffle and pick 6
    const selected = shuffleArray([...categories]).slice(0, 4);
    if (selected.length !== 4){
        addObjects(render_videos);
        return;
    }
    for (const item of selected) {
        const li = document.createElement("li");
        const span = document.createElement("span");
        span.classList.add("twemoji");

        // Fetch individual object JSON
        const objjson = await fetch(`${getOriginUrl()}/objects_raw/${item}.json`);
        if (!objjson.ok) throw new Error("Failed to load JSON for " + item);
        const objresult = await objjson.json();
        let description = objresult["description"];
        if (objresult["categories"].length == 0) {
            continue;
        }
        let categories = objresult["categories"][0]
            .replace(/ |\//g, "_") // substitui espaço e barra por "_"
            .toLowerCase(); // converte para minúsculas

        let firstSentence = description.split(". ")[0];

        // Create link
        const a = document.createElement("a");
        a.href = `${getOriginUrl()}objects/${categories}/${item}`;
        a.innerHTML = `<strong><code>${item}</code></strong>`;

        span.appendChild(a);

        let html = firstSentence.replace(/`([^`]+)`/g, "<code>$1</code>");
        html = html.replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");

        const p = document.createElement("p");
        p.innerHTML = `${html}.`;
        li.appendChild(span);
        li.appendChild(p);

        randomObjects.appendChild(li);
    }

    if (!render_videos) {
        return;
    }

    const jsonvideos = await fetch(`${getOriginUrl()}/all_videos.json`);
    if (!jsonvideos.ok) throw new Error("Failed to load JSON");
    const jsonmusic = await fetch(`${getOriginUrl()}/all_music.json`);
    if (!jsonmusic.ok) throw new Error("Failed to load JSON");

    const videos = await jsonvideos.json();
    const music = await jsonmusic.json();
    const media = [...videos, ...music];
    const shuffled = shuffleArray(media);
    const selectedVideos = shuffled.slice(0, 2);
    selectedVideos.forEach((v) => {
        let url = v.link || v;
        let videoId = null;

        const match1 = url.match(/v=([^&]+)/);
        if (match1) videoId = match1[1];

        const match2 = url.match(/youtu\.be\/([^?&]+)/);
        if (match2) videoId = match2[1];

        if (videoId) {
            url = `https://www.youtube-nocookie.com/embed/${videoId}`;
            const iframe = document.createElement("iframe");
            iframe.width = "45%"; // overridden by CSS on small screens
            iframe.height = "350px"; // overridden by CSS on small screens
            iframe.src = url;
            iframe.frameBorder = "0";
            iframe.allowFullscreen = true;
            randomVideos.appendChild(iframe);
        }
    });
}

async function addSimilar(objname) {
    const response = await fetch(`${getOriginUrl()}/objects_raw/${objname}.json`);
    if (!response.ok) throw new Error("Failed to load JSON");
    const obj = await response.json();
    const randomObjects = document.getElementById("random-objects");
    while (randomObjects.firstChild) {
        randomObjects.removeChild(randomObjects.firstChild);
    }

    let similar = obj["similar"];

    for (const item of similar) {
        const li = document.createElement("li");
        const span = document.createElement("span");
        span.classList.add("twemoji");

        // Fetch individual object JSON
        const objjson = await fetch(`${getOriginUrl()}/objects_raw/${item}.json`);
        if (!objjson.ok) throw new Error("Failed to load JSON for " + item);
        const objresult = await objjson.json();
        let description = objresult["description"];
        if (objresult["categories"].length == 0) {
            continue;
        }
        let categories = objresult["categories"][0]
            .replace(/ |\//g, "_") // substitui espaço e barra por "_"
            .toLowerCase(); // converte para minúsculas

        let firstSentence = description.split(". ")[0];

        // Create link
        const a = document.createElement("a");
        a.href = `${getOriginUrl()}/objects/${categories}/${item}`;
        a.innerHTML = `<strong><code>${item}</code></strong>`;

        span.appendChild(a);

        let html = firstSentence.replace(/`([^`]+)`/g, "<code>$1</code>");
        html = html.replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");

        const p = document.createElement("p");
        p.innerHTML = `${html}.`;
        li.appendChild(span);
        li.appendChild(p);

        randomObjects.appendChild(li);
    }
}
