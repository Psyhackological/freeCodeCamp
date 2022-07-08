#!/bin/bash

sudo pacman -S python-pip --needed
pip install yt-dlp --upgrade

mkdir -p Python
yt-dlp -o "Python/%(title)s.%(ext)s" --embed-subs --embed-metadata --write-description https://youtu.be/s8XjEuplx_U https://youtu.be/PXMJ6FS7llk https://youtu.be/0oSsLbh_Kv4 https://youtu.be/gbyYXgiSgdM

mkdir -p Linux
yt-dlp -o "Linux/%(title)s.%(ext)s" --embed-subs --embed-metadata --write-description https://youtu.be/RZ4p-saaQkc https://youtu.be/ROjZy1WbCIA https://youtu.be/ZtqBQ68cfJc https://youtu.be/1hvVcEhcbLM

mkdir -p Rust
yt-dlp -o "Rust/%(title)s.%(ext)s" --embed-subs --embed-metadata --write-description https://youtu.be/MsocPEZBd-M

mkdir -p Big_O_Notation
yt-dlp -o "Big_O_Notation/%(title)s.%(ext)s" --embed-subs --embed-metadata --write-description https://youtu.be/Mo4vesaut8g

mkdir -p Bootstrap
yt-dlp -o "Bootstrap/%(title)s.%(ext)s" --embed-subs --embed-metadata --write-description https://youtu.be/-qfEOE4vtxE

mkdir -p Docker
yt-dlp -o "Docker/%(title)s.%(ext)s" --embed-subs --embed-metadata --write-description https://youtu.be/fqMOX6JJhGo