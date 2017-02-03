#!/bin/bash
# Spotify Conky Now Playing
# by Paul Williams <paul@skenmy.com>

function nowplaying() {
	echo `dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata'|egrep -A 2 "artist"|egrep -v "artist"|egrep -v "array"|cut -b 27-|cut -d '"' -f 1|egrep -v ^$` "-" `dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata'|egrep -A 1 "title"|egrep -v "title"|cut -b 44-|cut -d '"' -f 1|egrep -v ^$`
}

function nowplaying_length() {
	echo `dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata'|egrep -A 2 "length"|egrep -v "length"|egrep -v "array"|cut -b 43-|cut -d '"' -f 1|egrep -v ^$`
}

#printf "Now playing: %s - Time: %s" "$(nowplaying)" "$(nowplaying_length)"
echo "$(nowplaying)"
