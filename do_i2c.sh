# Copy to the Pi
if [ "$#" -eq 0 ]; then
  scp do_i2c.sh raspi:/tmp/.
  ssh raspi "chmod +x /tmp/do_i2c.sh && /tmp/do_i2c.sh -n"

fi

# Guard to execute non-interactive
while getopts "n" opt; do
  case $opt in
    n)
      sudo raspi-config --expand-rootfs
      echo -e "\ni2c-dev" | sudo tee -a /etc/modules
      sudo reboot
      ;;
  esac
done


