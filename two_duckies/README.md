# Automation

Currently, the script is running on a Pi in its previous incarnation, via crontab:

```
*/5 * * * * cd /home/pi/pipy/two_duckies/ && . ./env/bin/activate && ./test.py > /dev/null 2>&1 || true
```