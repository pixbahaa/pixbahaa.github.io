#/bin/sh
cd
mkdir arc
cd arc

curl -O https://pixbahaa.github.io/src/arc/arch.sh
curl -O https://pixbahaa.github.io/src/arc/alacritty.toml
curl -O https://pixbahaa.github.io/src/arc/c.sh
curl -O https://pixbahaa.github.io/src/arc/i3status.conf

sh arch.sh
