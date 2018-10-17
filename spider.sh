#!/bin/bash

export http_proxy=""
export https_proxy=""

# Alle zu synchronisierenden Seiten
seiten=("www.berlin.de" "https://www.hamburg.de/buergerservice/" "www.gelsenkirchen.de/de/_meta/Buergerservice/" "www.koeln.de" "www.frankfurt.de/sixcms/detail.php?id=2717")

# Ort, an welchen die Seiten geschrieben werden sollen
ziel=/home/developer/staedte/data

# Wechsel zum Zielverzeichnis
cd $ziel

# Für jede Seite im hintergrund einen wget crawl Prozess starten
for element in "${seiten[@]}"
do
    wget -A.htm,.html,.aspx,.php -o /dev/null -r -p -U -N "$element" &
done 

# Jede Sekunde verbrauchten Speicherplatz anzeigen
watch -n1 du -sh $ziel

# Falls abbruch durch CTRL-C oder ähnliches alle wget Prozesse stoppen
function finish {
  killall -9 wget
}
trap finish EXIT
