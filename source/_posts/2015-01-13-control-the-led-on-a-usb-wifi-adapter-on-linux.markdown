---
layout: post
title: "Control the LED on a USB WiFi Adapter on Linux"
date: 2015-01-13 07:46:07 +0000
comments: true
categories: [Linux]
---

First, find the corresponding directory of this LED device in `/sys/class/leds`, such as `/sys/class/leds/device_name`,
and switch your working directory to this directory. The `device_name` may be similar to the device driver of your wifi
adapter. You should have a file named `trigger` and a file named `brightness` in this directory. `cat trigger` shows you
available triggers to trigger the LED light, with the current trigger surrounded by brackets. Different triggers will
turn on and off the LED in different cases. Use `echo new-trigger > trigger` to change trigger. `cat brightness` shows
the current brightness of the LED. Use `echo N > brightness` to change brightness, where N is an integer.

For example, I have a USB wifi adapter with an Atheros AR9271 chip, which is powered by the driver `ath9k_htc` on Linux.
When I plug in the device, I have a new directory `/sys/class/leds/ath9k_htc-phy0` created on my system. `cat trigger`
outputs

    none cpu0 cpu1 cpu2 cpu3 usb-gadget usb-host rfkill0 phy0rx phy0tx phy0assoc phy0radio [phy0tpt]

<!-- more -->

The default, `phy0tpt`, causes the LED to blink when there are activities. `echo phy0radio > trigger` causes the LED
light to be on when this wifi interface is on. `echo phy0assoc > trigger` causes the LED to be on when connected to an
access point. You can check the relevant [document](https://www.kernel.org/doc/htmldocs/80211/led-support.html) for
explanation of phy0rx, phy0tx, phy0assoc, phy0radio, phy0tpt (Click into the corresponding link to see what the trigger
means). `echo none > trigger` means no trigger. That is, LED will be controlled manually. In this case, `echo 255 >
brightness` can be used to turn on the LED, and `echo 0 >brightness` to turn it off.

If you want to automatically use a different trigger other than the default trigger when the adapter is plugged in,
[you can make a udev rule to do this](http://askubuntu.com/questions/25071/how-to-run-a-script-when-a-specific-flash-drive-is-mounted).
Note that this link is about flash drive, but the rule is the same for any USB devices. In my example I above, I created
a script `wifi-led.sh` to update the trigger:

```sh wifi-led.sh
#!/bin/bash

for trigger in ls /sys/class/leds/ath9k_htc-phy*/trigger; do
    id=$(echo $trigger | sed -e 's/.*ath9k_htc-phy\([0-9]\).*/\1/g')
    echo "phy${id}radio" > $trigger
done
```

And add a new udev rule `100-usbwifi.rules` to `/etc/udev/rules.d` to run this script when the adapter is plugged:

    ACTION=="add", ATTRS{idVendor}=="venid", ATTRS{idProduct}=="prodid", RUN+="/path/to/wifi-led.sh"

Replace `venid` and `prodid` with your actually usb device ID. You can see the ID by running `lsusb`. For example, I
have this following line output by `lsusb` corresponding to my USB wifi adapter.

    Bus 001 Device 004: ID 0cf3:9271 Atheros Communications, Inc. AR9271 802.11n

where `0cf3` is the vendor ID, `9271` is the product ID.
