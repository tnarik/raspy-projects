# Automation

Currently, the script is running on a Pi in its previous incarnation, via crontab:

```
*/5 * * * * cd /home/pi/pipy/two_duckies/ && . ./env/bin/activate && ./test.py > /dev/null 2>&1 || true
```

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
virtualenv .direnv && source .direnv/bin/activate && pip install -r requirements.txt
```