# automcserver
auto-generate a minecraft server

Auto generate a vanilla minecraft, PaperMC (bukkit) server, fabric server, or a bukkit server with my own list of plugins installed.
Option to auto start the server after it generates as well.

Add to /bin directory on linux, or add script to directory you want server to generate. (only run command from within the desired directory! Server will begin generating in that location)

# Usage
`mcserver --help`
```
usage: mcserver [-h] [-a] [-g] [-v] [-p] [-f] [-c]

optional arguments:
  -h, --help        show this help message and exit
  -a, --auto-start  auto-start minecraft server after generated
  -g, --gui         enable gui for auto-start (BY DEFAULT OFF, ONLY USE FLAG IF WANTED)
  -v, --vanilla     create vanilla mc server
  -p, --paper       create papermc server
  -f, --fabric      create fabric mc server
  -c, --custom      create premade custom server

```

# Example:
```
mcserver -f -a
```

# Prerequisites:
Requires gdown, but can work easily with git, wget, ftp, http, etc. by replacing the commands and hosting the files yourselves.    

Minecraft 1.18.1 requires at least Java 17. 

My mcMMO jarfile was pirated. cry about it if you're going to feel bad.
