Shiny Counter CLI
===

Shiny counter in command line, save your progress in sqlite and text file.

[![asciicast](https://asciinema.org/a/154377.png)](https://asciinema.org/a/154377)

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

Using with OBS
---

1. Insert a text layer
![Alt text](assset/obs-1.png?raw=true "Title")



2. Check 'Read from file'
![Alt text](assset/obs-2.png?raw=true "Title")



3. Select your shiny hunt target
![Alt text](assset/obs-3.png?raw=true "Title")



4. Position on your streaming setting
![Alt text](assset/obs-4.png?raw=true "Title")

