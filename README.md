# Raspberry PI Zero as a HID Keyboard

## Requirements

1. Raspberry Pi Zero
2. Kernel 4.4+
3. Only tested with Linux PC

## Sources

[Starting a script on boot using systemd](http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)

[Setting up kernel for USB Composite Device](http://isticktoit.net/?p=1383)

## Setup

```bash
# Enable Kernel Modules
echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
echo "libcomposite" | sudo tee -a /etc/modules

# Register script to setup PI as HID device
cp isticktoit_usb /usr/bin/isticktoit_usb
chmod 755 /usr/bin/isticktoit_usb

# Run this script at startup
cp piHID.service /lib/systemd/system/piHID.service
chmod 644 /lib/systemd/system/piHID.service
sudo systemctl daemon-reload
sudo systemctl enable piHID.service

sudo reboot
```
