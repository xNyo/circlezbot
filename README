## circlezbot

### Requirements
- Python 3.6
- A MySQL Server

### Setting up
```
$ git clone ...
$ cd circlezbot
$ virtualenv -p $(which python3.6) .pyenv
$ source .pyenv/bin/activate
(.pyenv) $ pip install -r requirements.txt
(.pyenv) $ deactivate
$ cp settings.sample.ini settings.ini
$ nano settings.ini
...
$ mysql -u circle -p circle < sql/base.sql
$ tmux
$ source .pyenv/bin/activate
(.pyenv) $ python3 circlebot.py
```

### License
This project is licensed under the GNU AGPL 3 License.
See the "LICENSE" file for more information.
