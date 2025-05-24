import os
import subprocess

hos = subprocess.run(["cat", "/etc/hostname"], capture_output=True, text=True).stdout.strip()
wd = subprocess.run(["pwd"], capture_output=True, text=True).stdout.strip()
os.mkdir(f"{wd}/src/hypr")
os.chdir(f"{wd}/src/hypr")
os.system('curl -O https://pixbahaa.github.io/src/hypr/hypr.sh')

if hos == "debian":
  os.system('curl -O https://pixbahaa.github.io/src/hypr/debian.sh')
  os.system('bash debian.sh')
elif hos == "Arch":
  os.system('curl -O https://pixbahaa.github.io/src/hypr/debian.sh')
  os.system('bash arch.sh')
