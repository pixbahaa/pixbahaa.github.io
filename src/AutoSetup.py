import os
import sys

hos = os.system('cat /etc/hostname', capture_output=True, text=True).stdout.strip()
wd = os.system('pwd', capture_output=True, text=True).stdout.strip()


if hos == "debian":
  os.system('curl -s https://pixbahaa.github.io/src/deb/deb.sh | sh')
elif hos == "Arch":
  os.system('curl -s https://pixbahaa.github.io/src/arc/arc.sh | sh')




else:
  if sys.platform == freebsd15 or freebsd14:
    os.chdir("/home/bahaa")
    os.system('curl https://pixbahaa.github.io/free-bsd/ | sh')
  if wd == "/data/data/com.termux/files/home/13v":
    os.chdir(wd)
    os.mkdir("git")
    os.chdir(f"{wd}/git")
    os.system('curl https://pixbahaa.github.io/android-termux/ | sh')
  else:
    print("bahaa support only android, freebsd, debian and Arch")
