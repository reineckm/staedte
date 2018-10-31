#!/bin/sh
staedte=$1
suchworte=$2
ziel=$3
while read stadt; do 
  echo $stadt
  mkdir $ziel/$stadt
  while read suchwort; do
    echo $suchwort
    # Ergebnis von Auf gut Glück, also dem Redirect in URL speichern
    URL=$(curl -sA "Chrome" "https://www.google.de/search?hl=de&q="$stadt"+"$suchwort"&oq=&btnI=1" | grep -oha 'HREF=".*"' | sed 's/HREF="//g' | sed 's/"//g')
    echo $URL
    wget $URL -P "$ziel/$stadt/$suchwort"
  done < $suchworte
done < $staedte
