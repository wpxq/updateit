# Package Manager Updater

![ppush](https://github.com/wpxq/updateit/blob/main/updateit.png)

---

CLI tool to update all package managers and check the latest update date 

---

## Functions

### `--update`  
Updates all packages from All Package Managers

| Package Managers |
| ---------------- |
| Pacman           |
| Xbps             |
| Dnf              |
| Yay              |
| Pkg              |
| Apt              |
| Portage          |
| Zypper           |
| Flatpak          |
| Snap             |
| Pip              |
| Npm              |
| Brew             |
| Pnpm             |
| Cargo            |

### `Cargo` (IMPORTANT!)
- For Cargo updates, you must have `cargo-update` installed:
##### cargo install cargo-update

### `--latest`
Shows the latest update

### `--refresh`
Fetch new version from this github repo
if there are any problems with the path:
##### type in .bashrc => export PATH="$HOME/.local/bin:$PATH" => save & type => source .bashrc

### `--version`
Shows current version of updateit

## Requirements:
* Python 3.11 or higher
* `requests` library

## Setup
1. Clone this repo
2. Run the provided installation bash script:
   ```bash
   chmod +x updateit_setup.sh
   ./updateit_setup.sh
   ```