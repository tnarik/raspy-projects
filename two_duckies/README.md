# Setup

## Physical

Connect the Camera Module V2 to the Raspberry Pi you intend to use.
Connect the Sense HAT as well.

## Deployment

Create a [Twitter Application](https://apps.twitter.com/), with read-write permissions.

Deploy all code to the Pi (either via `scp` or importing via `git`):

```
git clone https://github.com/tnarik/raspy-projects.git two_duckies
cd two_duckies
git remote set-url --push origin no_push
git subtree split --prefix=two_duckies -b split
git checkout split
```

In the same folder, copy `config.example.yaml` to `config.yaml` and configure with the key and secret for your application.

With Python3 and Virtualenv already installed in the Pi, create an isolated Python environment, activate it and isntall all requirements:

```
virtualenv .direnv && . .direnv/bin/activate && pip install -r requirements.txt
```


### Update from GIT

```
git checkout master
git pull
git subtree split --prefix=two_duckies -b split
git checkout split
```

## Automation

Run the scrdipt automatically via `cron`. This can be configured manually via `crontab -e` or via a script such as the following (which will replace previous jobs if they are already configured):

```
( crontab -l | awk '!(/two_duckies/ && /\.\/eyes.py/)' &&
echo "*/10 * * * * cd /home/pi/pypis/two_duckies/ && . .direnv/bin/activate && ./eyes.py > /dev/null 2>&1 || true" ) | crontab
```
