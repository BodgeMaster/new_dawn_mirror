#!/usr/bin/env bash
cp html_resources/index_template.html index.html

function genlinks {
  for FILE in $(find . -maxdepth 1 -type f -name "??-*.html" | sort); do
    echo -ne "  <li><a href=\"$FILE\">\n"
    echo -n "    $(sed -e 's|^\./||;s/-.*//' <<< "$FILE") <span class="'"chapter">'
    grep -oe "<title>.*</title>" $FILE | sed -e 's/<title> //;s| </title>|</span>|'
    echo "  </a></li>"
  done
}

sed -ne '/  <!-- chapter_list_here -->/q;p' html_resources/index_template.html > index.html
# for some fucking reason, there is no way to tell wc to only print the number so we do cat abuse to get rid of the filename
LINE_NUMBER=$(("$(cat index.html | wc -l)"+2))
genlinks >> index.html
tail -n+$LINE_NUMBER html_resources/index_template.html >> index.html
