#!/bin/bash

export http_proxy=""
export https_proxy=""

# Alle zu synchronisierenden Seiten
seiten=("https://www.hamburg.de/buergerservice/" "www.gelsenkirchen.de/de/_meta/Buergerservice/")

# Ort, an welchen die Seiten geschrieben werden sollen
ziel=/media/sf_E_DRIVE/files/

# Wechsel zum Zielverzeichnis
cd $ziel

# Für jede Seite im hintergrund einen wget crawl Prozess starten
for element in "${seiten[@]}"
do
    wget -r --no-check-certificate --no-parent -A.htm,.html,.aspx,.php -o /dev/null -p -U -N "$element" &
done 

# Jede Sekunde verbrauchten Speicherplatz anzeigen
watch -n1 du -sh $ziel

# Falls abbruch durch CTRL-C oder ähnliches alle wget Prozesse stoppen
function finish {
  killall -9 wget
}
trap finish EXIT
