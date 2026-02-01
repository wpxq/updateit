# Package Manager Updater

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Bash Script](https://img.shields.io/badge/bash_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)

---

CLI tool to update all package managers and check the latest update date 

---

## Funcs

### `--update`  
Updates all packages from All Package Managers

| Package Managers |
| ---------------- |
| Pacman           |
| Flatpak          |
| DNF              |
| Snap             |
| Yay              |
| PIP              |
| NPM              |
| Portage          |
| Zypper           |
| Brew             |
| PKG              |
| APT              |

### `--latest`
Shows the latest update

### `--refresh`
Fetch new version from this github repo
if there are any problems with the path:
type in .bashrc => export PATH="$HOME/.local/bin:$PATH" => save & type => source .bashrc

### `--version`
Shows current version of updateit
