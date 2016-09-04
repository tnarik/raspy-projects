# The full setup requires Internet Sharing in an OS X machine

# Copy to the Pi
if [ "$#" -eq 0 ]; then
  scp do_usb_net.sh raspi:/tmp/.
  ssh raspi "chmod +x /tmp/do_usb_net.sh && /tmp/do_usb_net.sh -n"

fi

# Guard to execute non-interactive
while getopts "n" opt; do
  case $opt in
    n)
      echo -e "allow-hotplug usb0\niface usb0 inet manual" | sudo tee -a /etc/network/interfaces.d/usb0
      sudo reboot
      ;;
  esac
done


