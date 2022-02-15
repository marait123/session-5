# How to run the project (linux or wsl)

- run `sudo apt install dos2unix`
- run `sudo dos2unix ./setup.sh` this [issue](https://stackoverflow.com/questions/39527571/are-shell-scripts-sensitive-to-encoding-and-line-endings)
- run the following command `chmod +x ./setup.sh`
- run the following command `./setup.sh`
- run `flask run --reload`

# Common Issues

- if you can't connect to psql on WSL2
  `sudo /etc/init.d/postgresql start`

# Notes

- to view a file in terminal while showing end of line characters `cat -v setup.sh`
