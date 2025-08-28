function setCategoryData(data) {
    if (!data?.selected?.length) return;
    document.querySelectorAll("#categories input[type='checkbox']").forEach((cb) => (cb.checked = false));
    data.selected.forEach((cat) => {
        const checkbox = document.querySelector(`#categories input[type="checkbox"][value="${cat}"]`);
        if (checkbox) checkbox.checked = true;
    });

    // Optional: ensure parents are checked if any child is selected
    Object.entries(data.parents || {}).forEach(([child, parent]) => {
        const childCheckbox = document.querySelector(`#categories input[type="checkbox"][value="${child}"]`);
        const parentCheckbox = document.querySelector(`#categories input[type="checkbox"][value="${parent}"]`);
        if (childCheckbox?.checked && parentCheckbox && !parentCheckbox.checked) {
            parentCheckbox.checked = true;
        }
    });
}

function getCategoryData() {
    const selected = [];
    const groups = [];
    const parents = {};

    document.querySelectorAll("#categories .subcategory, #categories .checkbox-group").forEach((container) => {
        const parentHeading = container.querySelector("h5");
        const parentName = parentHeading?.textContent || null;

        const parentCheckbox = container.querySelector('input[type="checkbox"]');
        const parentSelected = parentCheckbox?.checked || false;

        const children = [];
        const selectedChildren = [];

        container.querySelectorAll('input[type="checkbox"]').forEach((cb) => {
            const val = cb.value;
            if (val !== parentName) {
                children.push(val);
                parents[val] = parentName;
                if (cb.checked) selectedChildren.push(val);
            } else if (parentSelected) {
                selected.push(val);
            }
        });

        if (parentName) {
            groups.push({
                parent: parentName,
                parent_selected: parentSelected,
                children,
                selected_children: selectedChildren,
            });
        }

        // Add selected children to flat list
        selected.push(...selectedChildren);
    });

    return { selected, groups, parents };
}

(function () {
    const $ = (sel, ctx = document) => ctx.querySelector(sel);
    const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

    const state = {
        articles: [],
        videos: [],
        musics: [], // musical works
        theme: "auto", // auto | light | dark
    };

    document.addEventListener("DOMContentLoaded", () => {
        // Elements
        const themeToggle = $("#themeToggle");
        const isPartOfLib = $("#isPartOfLib");
        const libraryField = $("#libraryField");
        const description = $("#description");
        const charCount = $("#char-count");

        // Repeaters
        const addArticleBtn = $("#addArticle");
        const articleTitle = $("#articleTitle");
        const articleAuthors = $("#articleAuthors");
        const articleLink = $("#articleLink");
        const articleList = $("#articleList");

        const addVideoBtn = $("#addVideo");
        const videoTitle = $("#videoTitle");
        const videoAuthors = $("#videoAuthors");
        const videoLink = $("#videoLink");
        const videoList = $("#videoList");

        const addMusicBtn = $("#addMusic");
        const musicTitle = $("#musicTitle");
        const musicComposer = $("#musicComposer");
        const musicLink = $("#musicLink");
        const musicList = $("#musicList");

        const saveSend = $("#saveSend");

        // Theme toggle (persist in localStorage)
        try {
            const savedTheme = localStorage.getItem("theme-preference");
            if (savedTheme) {
                state.theme = savedTheme;
                applyTheme(savedTheme);
            }
        } catch {}
        themeToggle?.addEventListener("click", () => {
            const next = getNextTheme(state.theme);
            state.theme = next;
            try {
                localStorage.setItem("theme-preference", next);
            } catch {}
            applyTheme(next);
        });

        function getNextTheme(current) {
            if (current === "auto") return "dark";
            if (current === "dark") return "light";
            return "auto";
        }
        function applyTheme(mode) {
            document.documentElement.dataset.theme = mode;
            const icon = mode === "dark" ? "light_mode" : mode === "light" ? "dark_mode" : "contrast";
            // themeToggle?.querySelector?.(".material-symbols-rounded")?.textContent = icon;
        }

        // Toggle library field
        isPartOfLib.addEventListener("change", () => {
            libraryField.hidden = !isPartOfLib.checked;
            if (!isPartOfLib.checked) {
                $("#libraryName").value = "";
            }
        });

        // Character count (include spaces to match minlength behavior)
        const updateCharCount = () => {
            const len = description.value.length;
            charCount.textContent = `${len} / 100 characters`;
            charCount.style.color = len < 100 ? "#d64545" : "var(--muted)";
        };
        description.addEventListener("input", updateCharCount);
        updateCharCount();

        // Helpers
        const parseList = (val) =>
            val
                .split(",")
                .map((s) => s.trim())
                .filter(Boolean);

        const isValidUrl = (val) => {
            if (!val) return false;
            try {
                new URL(val);
                return true;
            } catch {
                return false;
            }
        };

        // Build category hierarchy from DOM structure
        function getCategoryData() {
            const selected = $$('input[name="category"]:checked').map((cb) => cb.value);

            const groups = [];
            const parentsMap = {};

            // For each subcategory block, find its parent and its children
            $$(".subcategory").forEach((sc) => {
                // parent checkbox is the direct label under .subcategory
                const parentInput = sc.querySelector(':scope > label.checkbox input[name="category"]');
                if (!parentInput) return;
                const parent = parentInput.value;
                const parent_selected = parentInput.checked;

                // children are inside .nested-checkboxes
                const childInputs = Array.from(sc.querySelectorAll('.nested-checkboxes input[name="category"]'));
                const children = childInputs.map((i) => i.value);
                const selected_children = childInputs.filter((i) => i.checked).map((i) => i.value);

                // record parent for each child
                children.forEach((c) => {
                    parentsMap[c] = parent;
                });

                groups.push({ parent, parent_selected, children, selected_children });
            });

            return { selected, groups, parents: parentsMap };
        }

        // Renderers
        function renderList(listEl, items, type) {
            listEl.innerHTML = "";
            items.forEach((item, idx) => {
                const li = document.createElement("li");

                const titleEl = document.createElement("strong");
                titleEl.textContent = item.title;

                const meta = document.createElement("span");
                meta.className = "meta";
                const by = type === "music" ? "composer(s)" : "author(s)";
                const people = (type === "music" ? item.composers : item.authors).join(", ");
                meta.textContent = ` — ${by}: ${people} `;

                const link = document.createElement("a");
                link.href = item.link;
                link.target = "_blank";
                link.rel = "noopener noreferrer";
                link.textContent = "(link)";

                const actions = document.createElement("div");
                actions.className = "actions";

                const removeBtn = document.createElement("button");
                removeBtn.type = "button";
                removeBtn.className = "icon-button";
                removeBtn.title = "Remove";
                removeBtn.innerHTML = '<span class="material-symbols-rounded" aria-hidden="true">delete</span>';
                removeBtn.addEventListener("click", () => {
                    if (type === "article") state.articles.splice(idx, 1);
                    if (type === "video") state.videos.splice(idx, 1);
                    if (type === "music") state.musics.splice(idx, 1);
                    renderAll();
                });

                actions.appendChild(removeBtn);

                li.appendChild(titleEl);
                li.appendChild(meta);
                li.appendChild(link);
                li.appendChild(actions);
                listEl.appendChild(li);
            });
        }

        function renderAll() {
            renderList(articleList, state.articles, "article");
            renderList(videoList, state.videos, "video");
            renderList(musicList, state.musics, "music");
        }

        document.getElementById("title").addEventListener("blur", async function (event) {
            const value = event.target.value.trim();
            if (!value) return;

            try {
                const response = await fetch("../all_objects.json");
                if (!response.ok) throw new Error("Failed to load JSON");
                const objects = await response.json();

                if (objects.includes(value)) {
                    const response_obj = await fetch(`../objects/${value}.json`);
                    if (!response_obj.ok) throw new Error("Failed to load object JSON");
                    const obj_info = await response_obj.json();

                    console.log("Loaded object data:", obj_info);

                    // Fill basic form fields if empty
                    const setIfEmpty = (selector, val) => {
                        const el = document.querySelector(selector);
                        if (!el) return;

                        if (el.type === "checkbox") {
                            if (!el.checked && typeof val === "boolean") el.checked = val;
                        } else {
                            if (!el.value) el.value = val ?? "";
                        }
                    };

                    setIfEmpty("#title", obj_info.title);
                    setIfEmpty("#description", obj_info.description);
                    setIfEmpty("#download", obj_info.download_link);
                    setIfEmpty("#bugs", obj_info.bug_reports);
                    setIfEmpty("#developers", obj_info.developers?.join(", "));
                    setIfEmpty("#dekenAvailable", obj_info.available_on_deken);
                    setIfEmpty("#isPartOfLib", obj_info.part_of_library);
                    setIfEmpty("#libraryName", obj_info.library_name);

                    // Platforms checkboxes
                    if (obj_info.runs_on?.length) {
                        obj_info.runs_on.forEach((platform) => {
                            const cb = document.querySelector(`input[name="platform"][value="${platform}"]`);
                            if (cb && !cb.checked) cb.checked = true;
                        });
                    }

                    // Categories: merge existing with JSON
                    if (obj_info.categories?.length) {
                        const currentCategories = getCategoryData()?.selected || [];
                        const mergedCategories = [...new Set([...currentCategories, ...obj_info.categories])];
                        const parentsMap = {};
                        document.querySelectorAll("#categories .subcategory").forEach((sc) => {
                            const parentInput = sc.querySelector(":scope > h5");
                            const parentName = parentInput?.textContent;
                            if (!parentName) return;

                            sc.querySelectorAll('.nested-checkboxes input[name="category"]').forEach((childCb) => {
                                parentsMap[childCb.value] = parentName;
                            });
                        });
                        setCategoryData({ selected: mergedCategories, parents: parentsMap });
                    }

                    const mergeItems = (stateArray, jsonItems, type) => {
                        if (!jsonItems?.length) return;
                        jsonItems.forEach((item) => {
                            if (!stateArray.some((existing) => existing.title === item.title)) {
                                stateArray.push(item);
                            }
                        });
                        renderAll();
                    };

                    // Inside your blur listener after loading obj_info
                    mergeItems(state.articles, obj_info.articles, "article");
                    mergeItems(state.videos, obj_info.videos, "video");
                    mergeItems(state.musics, obj_info.musics, "music");

                    const description = document.getElementById("description");
                    const charCount = document.getElementById("char-count");
                    const len = description.value.length;
                    charCount.textContent = `${len} / 100 characters`;
                    charCount.style.color = len < 100 ? "#d64545" : "var(--muted)";

                } else {
                    console.log("❌ Not found:", value);
                }
            } catch (err) {
                console.error(err);
            }
        });
        // Adders
        addArticleBtn.addEventListener("click", () => {
            const title = articleTitle.value.trim();
            const authors = parseList(articleAuthors.value);
            const link = articleLink.value.trim();
            if (!title || !authors.length || !isValidUrl(link)) {
                alert("Please provide a title, author(s), and a valid link for the article.");
                return;
            }
            state.articles.push({ title, authors, link });
            articleTitle.value = "";
            articleAuthors.value = "";
            articleLink.value = "";
            renderAll();
        });

        addVideoBtn.addEventListener("click", () => {
            const title = videoTitle.value.trim();
            const authors = parseList(videoAuthors.value);
            const link = videoLink.value.trim();
            if (!title || !authors.length || !isValidUrl(link)) {
                alert("Please provide a title, author(s), and a valid link for the video.");
                return;
            }
            state.videos.push({ title, authors, link });
            videoTitle.value = "";
            videoAuthors.value = "";
            videoLink.value = "";
            renderAll();
        });

        addMusicBtn.addEventListener("click", () => {
            const title = musicTitle.value.trim();
            const composers = parseList(musicComposer.value);
            const link = musicLink.value.trim();
            if (!title || !composers.length || !isValidUrl(link)) {
                alert("Please provide a work title, composer(s), and a valid link for the musical work.");
                return;
            }
            state.musics.push({ title, composers, link });
            musicTitle.value = "";
            musicComposer.value = "";
            musicLink.value = "";
            renderAll();
        });

        // Time parser for YouTube "t" param (e.g., 1m23s, 90)
        function parseYouTubeTime(t) {
            if (!t) return "";
            if (/^\d+$/.test(t)) return t; // seconds
            const m = /(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?/i.exec(t);
            if (!m) return "";
            const h = parseInt(m[1] || "0", 10);
            const mi = parseInt(m[2] || "0", 10);
            const s = parseInt(m[3] || "0", 10);
            return String(h * 3600 + mi * 60 + s);
        }

        // YouTube embed (iframe) exactly like the requested style
        function youtubeEmbed(url) {
            try {
                const u = new URL(url);
                const host = u.hostname.replace(/^www\./, "");
                let videoId = "";
                let start = "";
                let si = "";
                let list = "";
                let index = "";

                if (host.includes("youtube.com")) {
                    videoId = u.searchParams.get("v") || "";
                    start = u.searchParams.get("start") || u.searchParams.get("t") || "";
                    if (start) start = parseYouTubeTime(start);
                    si = u.searchParams.get("si") || "";
                    list = u.searchParams.get("list") || "";
                    index = u.searchParams.get("index") || "";
                } else if (host === "youtu.be" || host === "m.youtube.com") {
                    videoId = u.pathname.slice(1);
                    start = u.searchParams.get("start") || u.searchParams.get("t") || "";
                    if (start) start = parseYouTubeTime(start);
                    si = u.searchParams.get("si") || "";
                    list = u.searchParams.get("list") || "";
                    index = u.searchParams.get("index") || "";
                }

                if (!videoId) return url;

                const qs = new URLSearchParams();
                if (si) qs.set("si", si);
                if (start) qs.set("start", start);
                if (list) qs.set("list", list);
                if (index) qs.set("index", index);

                const src = `https://www.youtube.com/embed/${videoId}${qs.toString() ? `?${qs}` : ""}`;
                return `<iframe style="border-radius: 8px" width="560" height="315" src="${src}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>`;
            } catch {
                return url;
            }
        }

        // GitHub issue generation (do not change the markdown generation)
        saveSend.addEventListener("click", () => {
            const title = $("#title").value.trim();
            const desc = $("#description").value.trim();
            const runs_on = $$('input[name="platform"]:checked').map((cb) => cb.value);
            const download_link = $("#download").value.trim();
            const bug_reports = $("#bugs").value.trim();
            const developers = parseList($("#developers").value);
            const available_on_deken = $("#dekenAvailable").checked;
            const part_of_lib = $("#isPartOfLib").checked;
            const library_name = $("#libraryName").value.trim();

            // NEW: collect categories with hierarchy
            const categoryData = getCategoryData();
            const categories = categoryData.selected;

            // Basic validation
            const errors = [];
            if (!title) errors.push("Title is required.");
            if (desc.length < 100) errors.push("Description must be at least 100 characters.");
            if (download_link && !isValidUrl(download_link)) errors.push("Download link must be a valid URL.");
            if (bug_reports && !isValidUrl(bug_reports)) errors.push("Bug reports link must be a valid URL.");
            if (errors.length) {
                alert(errors.join("\n"));
                return;
            }

            const project = {
                title,
                description: desc,
                runs_on,
                download_link,
                available_on_deken,
                bug_reports,
                developers,
                part_of_library: part_of_lib,
                library_name: part_of_lib ? library_name : "",
                // Categories: add flat selection and hierarchy so you know which are subcategories
                categories, // flat list of selected values
                category_groups: categoryData.groups, // [{ parent, parent_selected, children, selected_children }]
                category_parents: categoryData.parents, // { childValue: parentValue }
                articles: state.articles,
                videos: state.videos,
                musics: state.musics,
            };

            // JSON block
            const jsonBlock = "```json\n" + JSON.stringify(project, null, 2) + "\n```";

            // OS icons mapping
            const osIconMap = {
                Windows: ":fontawesome-brands-windows:",
                Mac: ":fontawesome-brands-apple:",
                Linux: ":fontawesome-brands-linux:",
            };
            const osIcons = project.runs_on.map((os) => osIconMap[os] || os).join(" ");

            // Build requested Markdown (unchanged)
            let md = `# ${project.title}

${project.description}

---
`;

            const lines = [];
            if (project.download_link || project.available_on_deken) {
                const dekenText = project.available_on_deken ? " or use [Deken](../deken.md)" : "";
                const dlText = project.download_link ? `[here](${project.download_link})` : "";
                const downloadLine = project.download_link
                    ? `:octicons-download-16: __Download__ ${dlText}${dekenText}.`
                    : `:octicons-download-16: __Download__ Use [Deken](../deken.md).`;
                lines.push(`- ${downloadLine}`);
            }
            if (project.developers.length) {
                lines.push(`- :fontawesome-brands-dev: Developed by **${project.developers.join(", ")}**.`);
            }
            if (project.bug_reports) {
                lines.push(`- :fontawesome-brands-github: __Report Bugs/Errors__ [here](${project.bug_reports})!`);
            }
            if (project.runs_on.length) {
                lines.push(`- :fontawesome-solid-computer: __Available__ for ${osIcons}.`);
            }
            if (lines.length) {
                md += `<div class="grid cards" markdown>
${lines.join("\n")}
</div>

`;
            }

            if (project.articles.length) {
                md += `<h3>Articles</h3>

<div class="grid cards" markdown>
`;
                project.articles.forEach((a) => {
                    md += `- :octicons-book-24: 
    <h4>${escapeHtml(a.title)}</h4>
    *by ${a.authors.map(escapeHtml).join(", ")}*

    [Link](${a.link})
`;
                });
                md += `</div>

`;
            }

            if (project.videos.length) {
                md += `---
<h3>Videos</h3>

<div style="display: flex; justify-content: center; gap: 20px;">
`;
                project.videos.forEach((v) => {
                    md += `    ${youtubeEmbed(v.link)}
`;
                });
                md += `</div>

`;
            }

            if (project.musics.length) {
                md += `---
<h3>Music</h3>

<div style="display: flex; justify-content: center; gap: 20px;">
`;
                project.musics.forEach((m) => {
                    md += `    ${youtubeEmbed(m.link)}
`;
                });
                md += `</div>

---
`;
            }

            const markdownBlock = "```markdown\n" + md + "\n```";

            // Open GitHub issue prefilled
            const repoURL = "https://github.com/charlesneimog/Awesome-Pd";
            const issueTitle = `Request to add library: ${project.title}`;
            const body = `${jsonBlock}\n\n${markdownBlock}`;
            const issueURL = `${repoURL}/issues/new?title=${encodeURIComponent(issueTitle)}&body=${encodeURIComponent(body)}`;

            window.open(issueURL, "_blank", "noopener,noreferrer");
        });

        function escapeHtml(str) {
            return String(str).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
        }
    });
})();

//╭─────────────────────────────────────╮
//│          BUILD CATEGORIES           │
//╰─────────────────────────────────────╯
function buildCategories(container, data) {
    for (const key in data) {
        const value = data[key];
        if (
            !value ||
            typeof value !== "object" ||
            (Array.isArray(value) && value.length === 0) ||
            (Object.keys(value).length === 0 && !Array.isArray(value))
        ) {
            if (key !== "Object of day") {
                container.appendChild(createCheckbox(key));
            }
        } else if (Array.isArray(value)) {
            if (key !== "Object of day") {
                container.appendChild(createCheckbox(key));
            }
        } else {
            const subDiv = document.createElement("div");
            subDiv.className = "subcategory";
            const h5 = document.createElement("h5");
            h5.textContent = key;
            subDiv.appendChild(h5);

            const nestedDiv = document.createElement("div");
            nestedDiv.className = "nested-checkboxes";

            buildCategories(nestedDiv, value);

            subDiv.appendChild(nestedDiv);
            container.appendChild(subDiv);
        }
    }
}

function createCheckbox(name) {
    const label = document.createElement("label");
    label.className = "checkbox pretty";

    const input = document.createElement("input");
    input.type = "checkbox";
    input.name = "category";
    input.value = name;

    const span = document.createElement("span");
    span.textContent = name;

    label.appendChild(input);
    label.appendChild(span);
    return label;
}

async function loadCategories() {
    try {
        const response = await fetch("categories.json");
        if (!response.ok) throw new Error("Failed to load JSON");
        const categories = await response.json();

        const container = document.getElementById("categories");
        const checkboxGroup = document.createElement("div");
        checkboxGroup.className = "checkbox-group";

        buildCategories(checkboxGroup, categories);

        container.appendChild(checkboxGroup);
    } catch (err) {
        console.error(err);
    }
}

// Start loading the JSON
loadCategories();

function sendHeight() {
    const height = document.documentElement.scrollHeight; // total height of the content
    window.parent.postMessage({ type: "resize-iframe", height }, "*");
}
window.addEventListener("load", sendHeight);
const observer = new MutationObserver(sendHeight);
observer.observe(document.body, { childList: true, subtree: true });

