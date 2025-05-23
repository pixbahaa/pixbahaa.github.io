#/bin/sh
cd
mkdir deb
cd deb

curl -O https://pixbahaa.github.io/src/deb/debian.sh
curl -O https://pixbahaa.github.io/src/deb/alacritty.yml
curl -O https://pixbahaa.github.io/src/deb/c.sh
curl -O https://pixbahaa.github.io/src/deb/i3status.conf

sh debian.sh
