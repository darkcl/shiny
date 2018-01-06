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

Server
===

shiny include web server function

start shiny web server with ```shiny serve``` in your progress directory

Restful API
===

GET /pokemon
---
List all shiny progress

POST /pokemon Create a tracker 
---

Payload:

```json
{"name": "Pikachu"}
```

Return:

```json
{"id": "1"}
```

GET /pokemon/{id} Get Current Progress from id
---

Return:

```json
{
    "id": "1",
    "name": "Pikachu",
    "count": "100",
    "is_finish": true,
    "finish_date": "2018-01-01"
}
```

GET /pokemon/{id}/add Add one to counter
---

Return:

```json
{
    "id": "1",
    "name": "Pikachu",
    "count": "101",
    "is_finish": true,
    "finish_date": "2018-01-01"
}
```

GET /pokemon/{id}/completed Add one to counter
---

Return:

```json
{
    "id": "1",
    "name": "Pikachu",
    "count": "101",
    "is_finish": true,
    "finish_date": "2018-01-01"
}
```