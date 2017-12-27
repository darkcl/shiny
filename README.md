Shiny Counter CLI
===

Shiny counter in command line, save your progress in sqlite and text file.

Installation
---

```sh
git clone git@github.com:darkcl/shiny.git
sudo pip install .
```

Usage
---

```sh
# Go to a empty folder to save your progress

cd ~/Document/my-progress

shiny hunt "Xerneas"

# Start Hunting for Xerneas

shiny hunt "Poipole Pikachu"

# You can enter multiple names to hunt

shiny count "Xerneas Poipole" --add 1

# Add Counter for Xerneas and Poipole for 1, --add 1 is optional

shiny get "Xerneas"

# Complete shiny hunt for Xerneas
```
