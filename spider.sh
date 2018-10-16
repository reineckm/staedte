#!/bin/bash

export http_proxy=""
export https_proxy=""

seiten=("www.berlin.de" "https://www.hamburg.de/buergerservice/" "www.gelsenkirchen.de/de/_meta/Buergerservice/" "www.koeln.de")

cd /home/developer/staedte/data

for element in "${seiten[@]}"
do
    wget -A.htm.html.aspx -r -p -U -N "$element" &
done 

