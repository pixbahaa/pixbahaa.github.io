import subprocess as bash
import os
  
hos = bash.run(["cat", "/etc/hostname"], capture_output=True, text=True).stdout.strip()
wd = bash.run(["pwd"], capture_output=True, text=True).stdout.strip()

if hos == "debian":

  os.chdir(f"{wd}/src/dists/debian")
  bash.run(["bash", "debian.sh"])


elif hos == "Arch":

  os.chdir(f"{wd}/src/dists/arch")
  bash.run(["bash", "arch.sh"])

else:
    print("bahaa support only debian and Arch")
