---
layout: post
title: "Install PHP Extensions on Shared Hosts"
date: 2014-10-13 05:49:00 +0000
comments: true
categories: [php, hosting]
---

In this post, I will show you a workaround to install additional PHP extensions which are not available on your
Linux/BSD shared host. Before you proceed, you should ask whether your shared hosting company has an official way to
install or whether they can include the extension you need on their system, as this method is really only a
workaround: it probably works, but there is no guarantee of stability, especially your shared hosting company upgrades
PHP version.

I'll assume you have the basic knowledge of how to use a UNIX shell.

<!-- more -->

# Prerequisition

- SSH Access
- Custom `php.ini`
- All dependencies of your additional extensions are met 

File a ticket, send an email, or whatever way to contact your shared hosting customer service to ask for SSH access.
Also make sure you can add your own `php.ini` for your sites, and log in your SSH account to check whether they have all
the required libraries installed.

# Build the Extension

## Download the Source

Download the source from the extension website. If the extension is included in PHP source, download the version of PHP
source code from [PHP website](PHP) which is corresponding to the version on your shared host.

## Does Your Shared Host Provide Compiler and Meet Other Requirements to Build the extension?

Log into your SSH account. Type `which gcc` to see whether the command exists. If yes, very likely you can build the
extension right on the shared host, but note that there may be some missing header files or libraries. If you cannot
build your extension on the shared host, see the next section for what to do.

## Figure out What OS Your Shared Hosting Company Uses

You only need this part if you are not able to build the extension on the shared host, which means you have to build the
extension on a different machine. Figuring out what platform your shared host is on, log in your SSH account and
inspecting files there, such as `/etc/debian_version`, `/etc/redhat-release` to determine which Linux distribution or
BSD variants you are using. You can try to get some information by executing `uname -a`. However, there is no definite
way to tell which platform you are on, you need to be familiar with different distributions or BSD variants if the
shared hosting company has blocked some easy ways to tell which OS it is on. The most common ones may be CentOS, Debian,
Ubuntu and FreeBSD.

## Build the Extension on the Same Platform with Your Shared Host

For those people who cannot build extensions on the shared host directly, after figuring out what platform your website
is on, you need to have an exactly same BSD variant or Linux distribution and version to build the extension. If you
happen to be on the same platform, congrats you can go straight ahead and build it. If you are using a different Linux
distribution or BSD variants, just install it on a virtual machine, such as [VirtualBox][].

Follow the extension build instructions and build the extension on the target platform. If your extension is only
available with the PHP source code, configure PHP with a command similar to the command below when building PHP (check
`./configure --help` for the switch to enable the extension you need):

    ./configure --diable-all --enable-what-I-need=shared

For example for fileinfo extension, you should build php with `./configure --diable-all --enable-fileinfo=shared`.  Note
that in this case you need to make sure the extension is enabled to be built as a shared library, not built into the PHP
executable.

# Install the Extension

Create a phpinfo page, and find the directive `extension_dir`, the value of which is where the extensions are installed
on the shared host. Make a new directory under your home directory, say `~/php_extensions`, and copy all the
extensions in `extension_dir` to your newly created directory. Then, also copy the extension you built to this
directory.

Alright, we are almost there. Add an `extension_dir` directive to your own `php.ini` file to make PHP able to find your
extension. If you don't know the path of your extension directory, you can run the following command to find out the
path to the extension directory (I assume you put all your extensions in `~/php_extensions`):

    cd ~/php_extensions
    pwd

Finally, don't forget to add a new line `extension = your_extension.so` to your `php.ini` to enable the new extension.
Take a test and hopefully it should work.

# It doesn't work!

If it turns out that your site still does not use the new extension, first make sure you have enabled this extension in
your `php.ini`. If you are sure you have enabled the extension, run `ldd /path/to/your/extension.so` on the host to see
whether some dependencies are missing. If there is, either you didn't build the extension on the same OS with the same
version with the shared host, or the shared host does not have a required library installed. If it's the latter case,
do the same thing above for all the missing libraries, and install them in your home directory on the shared host.

# Conclusion

You are now able to install additional extensions on your shared host. However, this workaround is not for serious
business, as a single PHP update on the host can break your site! If you are on serious business, consider finding
another host which has all the extensions you need installed, or buying a [VPS][].

If you used this way to install additional extensions, you may also want to ask your shared hosting company to notify
you the date they are going to update PHP, so you can get ready for a possible break.

[PHP]: http://www.php.net
[VirtualBox]: http://www.virtualbox.org
[VPS]: http://en.wikipedia.org/wiki/Virtual_private_server
