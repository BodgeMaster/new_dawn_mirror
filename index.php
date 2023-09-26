<!DOCTYPE html><html><head><title> &lt;Post Apocalypse Story&lt; </title><link rel="stylesheet" type="text/css" href="html_resources/style.css"></head><body><a href="index.php"><button class="back">&lt;</button></a>
<h1> &lt;Post Apocalypse Story&lt; </h1>
<p class="comment">
  Yeah, there is no real title yet.
</p>
<p>
  Table of Contents:
</p>
<ul>
  <?php
    //TODO: get list of all html files
    //TODO: get the chapter numbers from the filenames
    //TODO: get the chapter titles from within the files
    //TODO: build a list of links sorted by chapter number
  ?>
</ul>
<script>let spans = ["<span class=\"paper_green\">", "<span>"];let paper_sections = document.getElementsByClassName("paper");for (let i = 0; i < paper_sections.length; i++) {let lines = paper_sections[i].innerHTML.split("\n");let result = "";for (let j = 0; j < lines.length; j++) {result = result + spans[j%2] + lines[j] + " ".repeat(80-lines[j].length) + "</span>\n";}paper_sections[i].innerHTML = result;}</script></body></html>
