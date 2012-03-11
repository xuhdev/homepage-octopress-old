---
layout: post
title: Add an "Show Image" Switch for the Safari Browser on Your iPhone/iPad/iPod Touch
date: 2012-03-10 16:41
comments: true
imagedir: /images/posts/2012-03-10-add-an-show-image-switch-for-the-safari-browser-on-your-iphone-slash-ipad-slash-ipod-touch
categories: [iOS, iPhone, iPad, Apple]
---

When we are using the Mobile Safari Browser to surfing the Internet, sometimes
the page loading speed will be largely slowed down because of the large size of
the images on the web page. Surprisingly, as one of the world's most popular
browser, the Safari Browser on [iOS][] (the mobile operating system running on
iPhone/iPad/iPod Touch) does not provide a switch to turn on/off the image display.
However, this does not mean you can not add such a switch by yourself.

<!-- more -->

### Get Your Device Jailbroken

[Jailbreaking][jailbreaking] is the process of removing the limitations imposed
by Apple on devices running the iOS operating system, such as iPhone, iPad,
iPod Touch, Apple TV. You need to jailbreak your device before you continue to next
step. To get your device jailbroken, please take a look at
[this page](http://www.idownloadblog.com/jailbreak). If you already have your
device jailbroken, you could skip this step.


### Modify Safari.plist

After jailbreaking, the next thing you need to do is to edit a [plist][] file
located on your device. If you are a normal user, you may want to install
[iFile][]. If you are familiar with UNIX shell,
[log into your device with ssh](http://thebigboss.org/guides-iphone-ipod-ipad/install-and-use-ssh)
might be the best way for you.

You need to edit a file named `Safari.plist` located in
`/System/Library/PreferenceBundles/MobileSafariSettings.bundle/` on your device.
To edit this file with iFile, first enter
`System/Library/PreferenceBundles/MobileSafariSettings.bundle/`.

![]({{ page.imagedir }}/1.png)

Then tap `Safari.plist` and select `Text Viewer`.

![]({{ page.imagedir }}/2.png)

Tap the `Edit` button on the top left corner.

![]({{ page.imagedir }}/3.png)


Insert the following text into this file before the last `</array>`:

```xml
<dict>
  <key>cell</key>
  <string>PSGroupCell</string>
</dict>
<dict>
  <key>defaults</key>
  <string>com.apple.mobilesafari</string>
  <key>key</key>
  <string>WebKitDisplayImagesKey</string>
  <key>cell</key>
  <string>PSSwitchCell</string>
  <key>label</key>
  <string>Show Images</string>
  <key>default</key>
  <integer>1</integer>
</dict>
```

It should look something like this:

![]({{ page.imagedir }}/4.png)


Save the file. Now open `Settings->Safari`, you should see a `Show Images`
switch at the bottom. If the switch is not shown, please
[reboot your device](http://www.apple.com/support/iphone/assistant/phone/#section_1)
and open Safari Settings again.

![]({{ page.imagedir }}/5.png)

I tested this on iOS 5.0.1, but it should also work on other versions of iOS.

This post was written based on
[this post](http://bbs.weiphone.com/read-htm-tid-2871429.html) (a Chinese post).


[iFile]: http://moreinfo.thebigboss.org/moreinfo/depiction.php?file=ifileData
[iOS]: http://en.wikipedia.org/wiki/IOS
[jailbreaking]: http://en.wikipedia.org/wiki/IOS_jailbreaking
[plist]: http://en.wikipedia.org/wiki/Property_list
