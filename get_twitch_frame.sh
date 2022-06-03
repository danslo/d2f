#!/bin/bash

if [[ $# -eq 0 ]] ; then
    echo "Usage: $0 <username>"
    exit 1
fi

streamlink "https://www.twitch.tv/$1" best -O | ffmpeg -y -i pipe:0 -vframes 1 -q:v 3 "frames/$1.jpg"