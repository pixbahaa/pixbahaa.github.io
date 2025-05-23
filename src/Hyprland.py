import subprocess as bash
import os
  
hos = bash.run(["cat", "/etc/hostname"], capture_output=True, text=True).stdout.strip()
wd = bash.run(["pwd"], capture_output=True, text=True).stdout.strip()
os.chdir(f"{wd}/src/hypr")

if hos == "debian":
  bash.run(["bash", "debian.sh"])
elif hos == "Arch":
  bash.run(["bash", "arch.sh"])
