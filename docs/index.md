# Home

<p align="center">
  WebSite that tries to list, with descriptiors, music examples, and links, all the objects, externals, and libraries available for PureData.
</p>

<div style="text-align: center; margin: 20px 0;">
    <a href="../submit" style="
        display: inline-block;
        padding: 10px 20px;
        background-color: #448aff;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
    ">
        ➝ Submit a new external
    </a>
</div>





--- 

<h2 align="center"><b>Check some objects</b></h2>


<div class="grid cards" >
    <ul>
        <li><span class="twemoji"></span></li>
        <li><span class="twemoji">segundo teste</span></li>
        <li><span class="twemoji">terceiro teste</span></li>
        <li><span class="twemoji">quarto teste</span></li>
    </ul>
</div>



<script>
async function addobjects(){
    const response = await fetch("../submit/categories.json");
    if (!response.ok) throw new Error("Failed to load JSON");
    const categories = await response.json();
}

addobjects();

</script>
