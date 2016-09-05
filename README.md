# Raspberry pi projects

## Foundations

These projects will run on a [Raspbian](https://www.raspbian.org/) based [Raspberry Pi](https://www.raspberrypi.org/).

The intention of this folder is bundling all the simplest projects together.

The current image used is Raspbian Jessie :

```
Version:May 2016
Release date:2016-05-27
Kernel version:4.4
SHA-1: 64c7ed611929ea5178fbb69b5a5f29cc9cc7c157 (full)
SHA-1: 03b6ea33efc3bb4d475f528421d554fc1ef91944 (lite)
```

For the installation on a SD card you can use [ApplePi-Baker](http://www.tweaking4all.com/software/macosx-software/macosx-apple-pi-baker/), which can be currently installed via Homebrew Cask. Alternatively (but testing shows it is slower), follow these steps:

1. Format the SD card to FAT32.
2. Identify the SD card via `diskutil list`, which shows the partition identifier (such as `disk3s1`) and the disk identifier (such as `disk3`)
3. `diskutil unmountDisk /dev/disk<disk# from diskutil>` (or just unmount)
4. `sudo dd bs=1m if=path_of_your_image.img of=/dev/<disk# from diskutil>` or (if you installed `pv`) : `sudo dd bs=1m if= path_of_your_image.img | pv | sudo dd  of=/dev/<disk# from diskutil>`


### PiZero as a USB gadget

It is possible using the PiZero via USB directly [as an Ethernet device](https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a).

Using the following process, with the PiZero, it is possible programming without additional peripherals, connecting instead via virtual Ethernet.

A couple of files in the boot partition need to be modified:

- Add to `cmdline.txt` the text `modules-load=dwc2,g_ether` (after `rootwait`)
- Add to `config.txt` a line with `dtoverlay=dwc2` to load the DWC2 USB OTG driver

As commands that you can paste and execute with the SD card mounted:

```
sed -ie 's/rootwait\ /rootwait modules-load=dwc2,g_ether /g' /Volumes/boot/cmdline.txt
echo "\n#DWC2 USB OTG driver\ndtoverlay=dwc2" >> /Volumes/boot/config.txt
```

Connect via the USB data port (it will provide power as well) and you will be able to ssh into the Pi Zero (use `-o"UserKnownHostsFile /dev/null"` if you are using several Pi Zero):

```
ssh pi@raspberrypi.local
```

Ideally you want to expand the filesystem so that it has access to the whole SD card.

```
sudo raspi-config --expand-rootfs
sudo raspi-config nonint do_hostname <new name>
```

### Credentials

By default, the user is `pi` and password is `raspberry`. It has `sudo` capabilities.

### Set WiFi

Look for available networks:

```
sudo iwlist wlan0 scan
# or
wpa_cli scan && sleep 5 && wpa_cli scan_results
```

Then add the network configuration:

```
echo -e '\nnetwork={\n    ssid="<ESSID>"\n    psk="<password>"\n}' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
```

## Python projects

A good strategy for Python is using [virtualenv](https://virtualenv.pypa.io/en/stable/) and [pip](https://pypi.python.org/pypi/pip), for isolation of requirements/modules. Except for the libraries which are specific to the Rapsberry Pi, development can take place in OS X (for instance), and we can take advantage of the integration with [direnv](https://github.com/direnv/direnv). Just create a `.envrc` file under every project folder, containing:

```
layout python python3
```

Then add the `.direnv` folder to your `.gitignore` file (if you are using `git`).

Describing dependencies in a `requirements.txt` file is a good practice. It can be done explicitely or executing `pip freeze > requirements.txt` after installation of the required packages via `pip install`. Later on this can be used via `pip install -r requirements.txt` (and integrates directly with Heroku systems, for instance).

Use of Python3 is recommended, so use of Python3 tools should be assumed in this repo.


Although the projects can be located anywhere (and some previous practice suggested running code as `root`), I prefer keeping code for all projects (specially when each is compact) under a single folder: `$HOME/pypis`

### Python modules on the Pi

As we will install support for components and the like via `pip`, within a contained `virtualenv` environment, that means we need the following:
 
```
sudo apt-get install -y python3-pip python3-dev
sudo pip3 install virtualenv
```

To run manually on a virtual environment (`.direnv` as convention):

```
mkdir <folder>
cd <folder>
virtualenv .direnv
. .direnv/bin/activate
```
