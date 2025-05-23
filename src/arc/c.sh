#!/bin/bash
i3bcd=/home/bahaa/.config/i3/config
sed -i '$s/^/#/' $i3bcd
echo "new_window pixel 0" >> $i3bcd
echo "new_float pixel 0" >> $i3bcd

echo "gaps inner 2" >> $i3bcd

echo "exec --no-startup-id setxkbmap -layout \"us,ara\" -option \"grp:alt_shift_toggle" >> $i3bcd

sed -i 's/font pango:monospace 8/font pango:Noto Sans 12/' $i3bcd
sed -i 's/bindsym $mod+Return exec i3-sensible-terminal/bindsym $mod+Return exec alacritty/' $i3bcd
echo "bindsym \"$mod+z\" exec google-chrome-stable" >> $i3bcd
sed -i 's/bindsym $mod+d exec --no-startup-id dmenu_run/bindsym $mod+d exec --no-startup-id dmenu_run -fn "Noto Sans"/' $i3bcd
sed -i 's/exec --no-startup-id xss-lock --transfer-sleep-lock -- i3lock --nofork/#exec --no-startup-id xss-lock --transfer-sleep-lock -- i3lock --nofork/' $i3bcd
sed -i 's/bar {/#bar {/' $i3bcd
sed -i 's/status_command i3status/#status_command i3status/' $i3bcd

echo "bar {" >> $i3bcd
echo "   position top" >> $i3bcd
echo "   status_command i3status" >> $i3bcd
echo "   font pango:Noto Sans 10" >> $i3bcd
echo "   colors {" >> $i3bcd
echo "       background #1d1f21" >> $i3bcd
echo "       statusline #c5c8c6" >> $i3bcd
echo "       separator  #666666" >> $i3bcd
echo " " >> $i3bcd
echo "       # Workspace colors" >> $i3bcd
echo "       focused_workspace  #282a2e #81a2be #ffffff" >> $i3bcd
echo "       active_workspace   #1d1f21 #373b41 #c5c8c6" >> $i3bcd
echo "       inactive_workspace #1d1f21 #282a2e #c5c8c6" >> $i3bcd
echo "       urgent_workspace   #1d1f21 #cc6666 #ffffff" >> $i3bcd
echo "    }" >> $i3bcd
echo "}" >> $i3bcd



paru -S --noconfirm google-chrome
sudo pacman -S --noconfirm zip unzip wget fastfetch htop linux-headers linux-docs meson ninja
