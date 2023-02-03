sudo apt-get install python-pip
sudo pip install getrpimodel pyserial requests
sudo sed -i "s/^enable_uart=.*/enable_uart=1/" /boot/config.txt
read -p "Would you like to reboot now?  (y/n) :" YN
if [ "${YN}" = "y" ]; then
  sudo reboot
else
  exit 1;
fi
