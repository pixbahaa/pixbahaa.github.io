#!/bin/bash


sudo apt update && sudo apt full-upgrade -y
sudo apt install fonts-noto-core fonts-noto-mono fonts-noto-color-emoji
sudo apt install xorg i3 feh alacritty pulseaudio pavucontrol tldr network-manager w3m unzip thunar thunar-volman neovim -y

mkdir -p .config/alacritty .config/i3status

cp i3status.conf /home/bahaa/.config/i3status/config
cp alacritty.yml /home/bahaa/.config/alacritty/
echo "exec i3" > /home/bahaa/.xinitrc
cp -r ../../walls /home/bahaa/

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt install -f -y

sudo rm /etc/network/interfaces
sudo systemctl enable NetworkManager

echo "reboot and run i3 for the fist time to auto generate config"
echo "and then use nmtui and also comment out the last line of i3 config in bar section"
echo "and finally run c.sh"
