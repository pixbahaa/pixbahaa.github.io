import os
import subprocess
import platform

hos = subprocess.run(["cat", "/etc/hostname"], capture_output=True, text=True).stdout.strip()
wd = subprocess.run(["pwd"], capture_output=True, text=True).stdout.strip()

if hos == "debian":
  os.mkdir("/home/bahaa/deb")
  os.chdir("/home/bahaa/deb")
  os.system('curl -O https://pixbahaa.github.io/src/deb/debian.sh')
  os.system('curl -O https://pixbahaa.github.io/src/deb/alacritty.yml')
  os.system('sh debian.sh')
elif hos == "Arch":
  os.mkdir("/home/bahaa/arc")
  os.chdir("/home/bahaa/arc")
  os.system('curl -O https://pixbahaa.github.io/src/arc/arch.sh')
  os.system('curl -O https://pixbahaa.github.io/src/arc/alacritty.toml')
  os.system('sh arch.sh')



elif:
  if platform.system() == "FreeBSD":
    os.mkdir("/home/bahaa/freebsd/")
    os.chdir("/home/bahaa/freebsd/")
    os.system('curl -O https://pixbahaa.github.io/free-bsd/user.sh')
    os.system('curl -O https://pixbahaa.github.io/free-bsd/wayfire.ini')
    os.system('chmod +x user.sh')
    os.system('sh user.sh')
if wd == "/data/data/com.termux/files/home/pix/src":
  os.chdir("/data/data/com.termux/files/home")
  os.mkdir("git")
  os.chdir("/data/data/com.termux/files/home/git")
  os.system('curl -s https://pixbahaa.github.io/android-termux/hi.sh | sh')
  else:
print("bahaa support only android, freebsd, debian and Arch")
