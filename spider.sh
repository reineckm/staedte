#!/bin/bash

export http_proxy=""
export https_proxy=""

# Alle zu synchronisierenden Seiten
seiten=("https://service.berlin.de/themen/" "https://www.gelsenkirchen.de/de/_funktionsnavigation/inhalt.aspx" "http://www.muenchen.de/dienstleistungsfinder/muenchen/")

# Ort, an welchen die Seiten geschrieben werden sollen
ziel=/media/sf_E_DRIVE/files/

# Wechsel zum Zielverzeichnis
cd $ziel

# Für jede Seite im hintergrund 4 wget crawl Prozesse starten
for element in "${seiten[@]}"
do
    wget --wait 1 -e robots=off --no-check-certificate -nc -A.htm,.html,.aspx,.php -o /dev/null -p -U -N -r "$element" &
done 

# Jede Sekunde verbrauchten Speicherplatz anzeigen
watch -n1 du -sh $ziel

# Falls abbruch durch CTRL-C oder ähnliches alle wget Prozesse stoppen
function finish {
  killall -9 wget
}
trap finish EXIT
