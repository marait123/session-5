# Note if you're using wsl

- install postgres on wsl ubuntu [link](https://www.postgresql.org/download/linux/ubuntu/)

```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql
```

- if you have postgres on windows stop the service
  ![stop-postgres](images/stop-windows-psql.png)
- in wsl run the following command `sudo service postgresql restart`

# create a virtual env

- run `pythom3 -m ven env`
- activate env `source ./env/bin/activate`
- run `pip install -r requirements.txt`

# How to run the project (linux or wsl)

- run `sudo apt install dos2unix`
- run `sudo dos2unix ./setup.sh` this [issue](https://stackoverflow.com/questions/39527571/are-shell-scripts-sensitive-to-encoding-and-line-endings)
- run the following command `chmod +x ./setup.sh`
- run the following command `./setup.sh`
- run `flask run --reload`

# Heroku

- Assuming you have already committed all your local edits.
  `git push heroku master`
- to access the bash `heroku run bash`

# Common Issues

- if you can't connect to psql on WSL2
  `sudo /etc/init.d/postgresql start`

# Access the local postgres database

- run `sudo su postgres`
- run `psql`

# Notes

- to view a file in terminal while showing end of line characters `cat -v setup.sh`
