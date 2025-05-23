import os
  
hos = os.system('cat /etc/hostname', capture_output=True, text=True).stdout.strip()
wd = os.system('pwd', capture_output=True, text=True).stdout.strip()
os.mkdir(f"{wd}/src/hypr")
os.chdir(f"{wd}/src/hypr")

if hos == "debian":
  
  os.system('bash debian.sh')
elif hos == "Arch":
  
  os.system('bash arch.sh')
