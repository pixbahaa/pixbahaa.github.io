import os
import sys
import subprocess

hos = subprocess.run(["cat", "/etc/hostname"], capture_output=True, text=True).stdout.strip()
wd = subprocess.run(["pwd"], capture_output=True, text=True).stdout.strip()

if hos == "debian":
  os.system('curl -s https://pixbahaa.github.io/src/deb/deb.sh | sh')
elif hos == "Arch":
  os.system('curl -s https://pixbahaa.github.io/src/arc/arc.sh | sh')




else:
  #if sys.platform == freebsd15 or freebsd14:
  #  os.chdir("/home/bahaa")
  #  os.system('curl https://pixbahaa.github.io/free-bsd/ | sh')
  if wd == "/data/data/com.termux/files/home/pix/src":
    os.chdir("/data/data/com.termux/files/home")
    os.mkdir("git")
    os.chdir("/data/data/com.termux/files/home/git")
    os.system('curl https://pixbahaa.github.io/android-termux/ | sh')
  else:
    print("bahaa support only android, freebsd, debian and Arch")
