#/bin/sh

cd /usr/ports/x11-wm/hyprland
clear
echo "check legacy renderer"
sleep 5
doas make config
doas make config-recursive
doas make -DBATCH install clean
