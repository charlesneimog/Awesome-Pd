# Objects

In this section we list all the objects submit for the project. Note that, if there is some great object is missing, please submit it using [Submit](../submit.md) form. It is very simple and easy. If you did some piece, publish article or recorded a Video for some object and it is not listed here also submit it. 

!!! tip "AI Classification"
    These libraries are extensive, and the first step involves AI-based classification. If you notice an error, please click "Submit" enter the object name, and update its description and classification.

<h2 align="center"><b>Random Objects</b></h2>

<div class="grid cards ">
    <ul id="random-objects"></ul>
</div>


<script>
document.addEventListener("DOMContentLoaded", () => {
    const response = await fetch(`${window.location.href}/../all_objects.json`);
    addObjects(false, response);
});
</script>

