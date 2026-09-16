# betaOS — Hybrid Terminal Operating System (Beta)

**Windows + Linux in one beautiful terminal OS**, written in pure Python.  
Now with cinematic boot sequence, groovy animations, and a full **100-room adventure game**.

## Features

- **Cinematic Boot** – Head setup, multi-stage loading bars, matrix rain, glitch text
- **Hybrid Shell** – Linux (`ls`, `cat`, `rm`) + Windows (`dir`, `type`, `del`, `cls`) commands
- **Virtual Filesystem** – Persistent, with `/home`, `/mnt/c` (Windows C:), `/etc`, etc.
- **Live Metrics** – CPU sparkline, memory, disk, process monitor
- **Built-in Apps**
  - `neofetch` – System info with logo
  - `top` / `htop` – Process monitor
  - `edit` / `nano` – Text editor
  - `pkg` / `apt` / `winget` – Hybrid package manager
  - `calc` – Calculator
  - `python` / `dotnet` – Developer tools
- **HybridQuest** – Full 100-room text RPG
  - 100 procedurally connected rooms
  - Items, weapons, armor, consumables
  - Enemies, combat, leveling
  - Inventory, locked doors, quest items
  - Win by collecting source fragments and returning to the entrance

## Quick Start

```bash
cd hybridos
python3 main.py
```

You will see the full boot animation, then land in the shell.

### Start the game
```
quest
```
or
```
game
```

## Requirements

- Python 3.8+
- No external packages (stdlib only)

---

**betaOS** – Hybrid power. Terminal soul. 100 rooms of adventure.
