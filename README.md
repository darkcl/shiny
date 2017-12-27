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

# Start Hunting for Xerneas

shiny hunt "Xerneas"

# You can enter multiple names to hunt

shiny hunt "Poipole Pikachu"

# Add Counter for Xerneas and Poipole for 1, --add 1 is optional

shiny count "Xerneas Poipole" --add 1

# Your folder should contain Xerneas.txt, Poipole.txt and hunt.sqlite now

# Complete shiny hunt for Xerneas

shiny get "Xerneas"

```
