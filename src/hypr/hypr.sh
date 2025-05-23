#!/bin/bash

git clone --recursive https://github.com/hyprwm/Hyprland

cd Hyprland
make -j2 legacyrenderer && sudo cp ./build/Hyprland /usr/bin && sudo cp ./example/hyprland.desktop /usr/share/wayland-sessions
