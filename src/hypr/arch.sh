#!/bin/bash

sudo pacman -S --needed --noconfirm xorg xorg-divers xorg-xwayland hyprland wayland base-devel ninja meson cmake
sudo pacman -R hyprland --noconfirm
bash hypr.sh
