#!/usr/bin/env python
__version__ = "2.0"
from pathlib import Path
import datetime, os
import shutil, sys
import stat, requests as r

log_path = Path.home() / ".local/share/updateit/latest.log"
log_path.parent.mkdir(parents=True, exist_ok=True)

def read_last():
    if log_path.exists():
        return log_path.read_text().strip()
    return None

def write_log():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path.write_text(now + "\n")
    return now

def has_cmd(cmd):
    return shutil.which(cmd) is not None

pkg_managers = [
    ("Pacman", "sudo pacman -Syu"),
    ("Flatpak", "flatpak update"),
    ("DNF", "sudo dnf upgrade"),
    ("Snap", "sudo snap refresh"),
    ("Yay", "yay -Syu"),
    ("Pip", "pip install --upgrade pip && pip list --outdated --format=freeze | cut -d = -f 1 | xargs -n1 pip install -U"),
    ("Npm", "npm update -g"),
    ("Portage", "sudo emerge --sync && sudo emerge -uDN @world"),
    ("Zypper", "sudo zypper refresh && sudo zypper update"),
    ("Brew", "brew update && brew upgrade"),
    ("PKG", "sudo pkg update && sudo pkg upgrade"),
    ("APT", "sudo apt update && sudo apt upgrade -y")
]

def clear():
    os.system("clear")

def show_log():
    last = read_last()
    if last:
        print(f"Last update: {last}")
    else:
        print("No update logged")

def updateit():
    start = write_log()
    print(f"[{start}] Starting update...")

    for name, cmd in pkg_managers:
        if has_cmd(cmd.split()[0]):
            print(f"[{start}] Updating {name}...")
            os.system(cmd)
            clear()
        else:
            print(f"[{start}] Skipping {name}: package manager is not installed")

def refresh():
    url = "https://raw.githubusercontent.com/wpxq/updateit/refs/heads/main/updateit.py"
    resp = r.get(url)
    if resp.status_code == 200:
        with open("updateit.py", "wb") as f:
            f.write(r.content)
        print("Succesfully fetch update")
    else:
        print("Failed to fetch update")
        return
    updateit_f = "updateit.py"
    updateit_alias = "updateit"
    st = os.stat(updateit_f)
    os.chmod(updateit_f, st.st_mode | stat.S_EXEC)
    shutil.copy(updateit_f, f"/usr/local/bin/{updateit_alias}")
    print(f"{updateit_f} refreshed")

if len(sys.argv) !=2:
    commands = """
updateit [--update] Updates package managers
updateit [--latest] Shows latest update log 
"""
    print(commands)
    sys.exit(1)
arg = sys.argv[1]

if arg == "--help":
    commands = """
updateit [--update] Updates package managers
updateit [--latest] Shows latest update log 
"""
    print(commands)
    sys.exit(1)

elif arg == "--latest":
    show_log()
elif arg == "--update":
    updateit()
elif arg == "--refresh":
    refresh()
else:
    print("Unknown arg, try --help")
    sys.exit(1)
