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
        musics: [],
    };

    document.addEventListener("DOMContentLoaded", () => {
        // Elements
        const titleEl = $("#title");
        const description = $("#description");
        const charCount = $("#char-count");
        const yearEl = $("#year");

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
            (val || "")
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

        // Build categories from JSON structure
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

                // buildCategories(checkboxGroup, categories);
                container.appendChild(checkboxGroup);
            } catch (err) {
                console.error(err);
            }
        }

        // Category data extraction (hierarchy awareness)
        function getCategoryData() {
            // Flat selected list
            const selected = $$('input[name="category"]:checked').map((cb) => cb.value);

            const groups = [];
            const parentsMap = {};

            // For each subcategory block, capture parent heading and children
            $$(".subcategory").forEach((sc) => {
                const parentHeading = sc.querySelector(":scope > h5");
                const parent = parentHeading?.textContent || null;
                const parent_selected = false; // no parent checkbox rendered

                const childInputs = Array.from(sc.querySelectorAll('.nested-checkboxes input[name="category"]'));
                const children = childInputs.map((i) => i.value);
                const selected_children = childInputs.filter((i) => i.checked).map((i) => i.value);

                // Record parent for each child
                children.forEach((c) => (parentsMap[c] = parent));

                if (parent) {
                    groups.push({ parent, parent_selected, children, selected_children });
                }
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

        // Save & Send (open GitHub issue with JSON block)
        saveSend.addEventListener("click", () => {
            const title = titleEl.value.trim();
            const desc = description.value.trim();
            const developers = parseList($("#developers")?.value || ""); // Composer(s)
            const performers = parseList($("#performers")?.value || "");
            const contributors = parseList($("#contributors")?.value || "");
            const year = yearEl?.value.trim() || "";

            // Categories
            const categoryData = getCategoryData();
            const categories = categoryData.selected;

            // Basic validation
            const errors = [];
            if (!title) errors.push("Name is required.");
            if (desc.length < 100) errors.push("Description must be at least 100 characters.");
            if (year && !/^\d{4}$/.test(year)) errors.push("Year must be a 4-digit number (e.g., 2019).");
            if (errors.length) {
                alert(errors.join("\n"));
                return;
            }

            const project = {
                title,
                whatiam: "piece",
                description: desc,
                developers, // composers
                performers,
                year, // NEW: included in payload
                // Categories: flat selection and hierarchy
                categories, // flat list of selected values
                category_groups: categoryData.groups, // [{ parent, parent_selected, children, selected_children }]
                category_parents: categoryData.parents, // { childValue: parentValue }
                articles: state.articles,
                videos: state.videos,
                musics: state.musics,
                contributors,
            };

            // JSON block (do not change the markdown generation)
            const jsonBlock =
                "\n\n*Don't delete the next lines please*\n```json\n" + JSON.stringify(project, null, 2) + "\n```";
            const repoURL = "https://github.com/charlesneimog/Awesome-Pd";
            const issueTitle = `Request to add piece: ${project.title}`;
            const body = `${jsonBlock}`;
            const issueURL = `${repoURL}/issues/new?title=${encodeURIComponent(issueTitle)}&body=${encodeURIComponent(body)}`;

            window.open(issueURL, "_blank", "noopener,noreferrer");
        });

        // Load category tree
        loadCategories();
    });
})();

//╭─────────────────────────────────────╮
//│          BUILD CATEGORIES           │
//╰─────────────────────────────────────╯
function buildCategories(container, data) {
    for (const key in data) {
        container.appendChild(createCheckbox(key));
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
