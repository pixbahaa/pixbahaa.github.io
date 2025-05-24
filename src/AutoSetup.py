import os
import sys
import subprocess

hos = subprocess.run(["cat", "/etc/hostname"], capture_output=True, text=True).stdout.strip()
wd = subprocess.run(["pwd"], capture_output=True, text=True).stdout.strip()

if hos == "debian":
  os.mkdir("/home/bahaa/deb")
  os.chdir("/home/bahaa/deb")
  os.system('curl -S https://pixbahaa.github.io/src/deb/debian.sh')
  os.system('curl -S https://pixbahaa.github.io/src/deb/alacritty.yml')
  os.system('sh debian.sh')
elif hos == "Arch":
  os.mkdir("/home/bahaa/arc")
  os.chdir("/home/bahaa/arc")
  os.system('curl -S https://pixbahaa.github.io/src/arc/arch.sh')
  os.system('curl -S https://pixbahaa.github.io/src/arc/alacritty.toml')
  os.system('sh arch.sh')



else:
  #if sys.platform == freebsd15 or freebsd14:
  #  os.chdir("/home/bahaa")
  #  os.system('curl https://pixbahaa.github.io/free-bsd/ | sh')
  if wd == "/data/data/com.termux/files/home/pix/src":
    os.chdir("/data/data/com.termux/files/home")
    os.mkdir("git")
    os.chdir("/data/data/com.termux/files/home/git")
    os.system('curl -s https://pixbahaa.github.io/android-termux/hi.sh | sh')
  else:
    print("bahaa support only android, freebsd, debian and Arch")
