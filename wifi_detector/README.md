# Setup

## Physical

Connect the Unicorn pHAT.


## Deployment

With Python3 and Virtualenv already installed in the Pi, create an isolated Python environment, activate it and install all requirements:

```
virtualenv .direnv && . .direnv/bin/activate && pip install -r requirements.txt
```

## Notes

As Unicorn pHAT requires `root` access, it might be a good idea using:

```
sudo bash -c "cd . && . .direnv/bin/activate && python"
```

## Automation

Run the script automatically via root's `cron`. This can be configured manually via `sudo crontab -e` or via a script such as the following (which will replace previous jobs if they are already configured):

```
( sudo crontab -l | awk '!(/wifi_detector/ && /\.\/wifi.py/)' &&
echo "*/10 * * * * cd /home/pi/pypis/wifi_detector/ && . .direnv/bin/activate && ./wifi.py > /dev/null 2>&1 || true" ) | crontab
```