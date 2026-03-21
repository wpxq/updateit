# Package Manager Updater

---

CLI tool to update all package managers and check the latest update date 

---

## Functions

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
##### type in .bashrc => export PATH="$HOME/.local/bin:$PATH" => save & type => source .bashrc

### `--version`
Shows current version of updateit

## Setup
1. Clone this repo
2. Run the provided installation bash script:
   ```bash
   chmod +x updateit_setup.sh
   ./updateit_setup.sh
   ```
