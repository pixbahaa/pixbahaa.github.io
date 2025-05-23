#!/bin/bash

sudo pacman -Syu --noconfirm
sudo pacman -S --noconfirm noto-fonts noto-fonts-emoji noto-fonts-extra ttf-noto-nerd
sudo pacman -S --noconfirm xorg xorg-drivers xorg-xinit i3 alacritty dmenu base-devel grml-zsh-config powerline python-click-completion zsh zsh-autosuggestions zsh-completions zsh-history-substring-search zsh-syntax-highlighting intel-ucode pulseaudio pavucontrol
sudo usermod -s /bin/zsh bahaa
echo "source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> /home/bahaa/.zshrc
echo "source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh" >> /home/bahaa/.zshrc
echo "source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh" >> /home/bahaa/.zshrc


git clone https://aur.archlinux.org/paru-bin
cd paru-bin
makepkg -si --noconfirm
cd ..

mkdir -p /home/bahaa/.config/alacritty
cp alacritty.toml /home/bahaa/.config/alacritty/
cp -r ../../walls /home/bahaa/
echo "exec i3" > /home/bahaa/.xinitrc
mkdir /home/bahaa/.config/i3status
cp i3status.config /home/bahaa/.config/i3status/config

echo "reboot and run i3 for the fist time to auto generate config and then run c.sh"
