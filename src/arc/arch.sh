#/bin/sh

cd
sudo pacman -Syu --noconfirm
sudo pacman -S --noconfirm noto-fonts noto-fonts-emoji noto-fonts-extra ttf-noto-nerd
sudo pacman -S --noconfirm xorg xorg-drivers xorg-xinit dwm dmenu alacritty dmenu base-devel zsh zsh-autosuggestions zsh-history-substring-search zsh-syntax-highlighting intel-ucode pulseaudio pavucontrol
sudo usermod -s /bin/zsh bahaa
echo "source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> /home/bahaa/.zshrc
echo "source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh" >> /home/bahaa/.zshrc
echo "source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh" >> /home/bahaa/.zshrc

git clone https://aur.archlinux.org/paru-bin
cd paru-bin
makepkg -si --noconfirm
cd ..
rm -rf paru-bin

mkdir -p .config/alacritty
cp alacritty.toml .config/alacritty/
echo "exec dwm" > .xinitrc
