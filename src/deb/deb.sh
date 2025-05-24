#/bin/sh
cd
mkdir deb
cd deb

curl -O https://pixbahaa.github.io/src/deb/debian.sh
curl -O https://pixbahaa.github.io/src/deb/alacritty.yml

sh debian.sh
