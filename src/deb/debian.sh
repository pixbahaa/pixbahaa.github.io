#!/bin/bash

cd

sudo apt update && sudo apt full-upgrade -y
sudo apt install fonts-noto-core fonts-noto-mono fonts-noto-color-emoji
sudo apt install xorg dwm suckless-tools feh alacritty pulseaudio pavucontrol tldr w3m unzip thunar thunar-volman vim -y

mkdir -p .config/alacritty

cp alacritty.yml .config/alacritty/
echo "exec dwm" > .xinitrc

cd /tmp

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i /tmp/google-chrome-stable_current_amd64.deb
sudo apt install -f -y
