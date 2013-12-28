---
layout: post
title: "Manage Multiple SSH Private Keys"
date: 2013-05-05T11:59:07
comments: true
categories: [ssh]
---

If you have multiple ssh keys, it is sometimes hard to manage. This was
[written before][post],
but mostly they are handling using different keys with different host. What if
you have two or more [GitHub][] or [BitBucket][] accounts requiring different
keys? As a result, I created [skm][] to provide a more general solution. Here
I'll give a brief introduction of how to manage multiple SSH private keys with
skm.

<!-- more -->

## Installation

Since skm is written in [Ruby][], you need to install ruby first. Ruby is
shipped with Mac OS X, and for most Linux distributions, you can install them
quite easily:

```sh
# Debian/ubuntu
sudo apt-get install ruby

# Fedora
sudo yum install ruby
```

Then install [RubyGems][] if `gems` command does not exist.

Alternatively, you could use [rvm][] to install Ruby and RubyGems.

Finally install skm:

    gem install skm     # You may need root privilege by prepending `sudo`


## Use skm

### Create Keys

If you want to create new keys with skm, simply use the following command:

    skm create key_name

Or use the following command to add a comment to the key (you may prefer it
your email address):

    skm create key_name -C "my@email.com"

Then you should find your new keys stored in a directory named `key_name`
located at `~/.skm/keys`:

    $ ls ~/.skm/keys/key_name
    id_rsa  id_rsa.pub

### Import Keys

To import keys to skm, simply create a new directory in `~/.skm/keys` and copy
`id_rsa` and `id_rsa.pub` (or `id_dsa` and `id_dsa.pub`) into that directory:

    mkdir -p ~/.skm/keys/key_name
    cp /path/to/id_rsa /path/to/id_rsa.pub ~/.skm/keys/key_name

### Switch Keys

Suppose you already have several keys either created or imported. `list`
command will list them all:

    $ skm list
    key1
    key2

Say now we want to use key1. Simply run `skm use key1`, then the keys in
`~/.skm/keys/key1` will be copied to `~/.ssh` to make the keys valid. After
doing some works, if you run `skm use key2`, the keys in `~/.skm/keys/key2`
will be copied to `~/.ssh`, which makes `key2` valid.

### Example

OK, suppose you have two accounts _hare_ and _tortoise_ on some website, which
requires different keys for each account. Then you need two keys:

    skm create hare
    skm create tortoise

Let's list them:

    $ skm list
    hare
    tortoise

Then you could switch them by `skm use hare` or `skm use tortoise`.


## Different Hosts with Different Keys

Besides all I've written above, if you still need to connect to some hosts with
some specific keys, you can still take advantage of `~/.ssh/config`. For
example, you could have something like this in `~/.ssh/config` (the example is
taken from [this post][post] with slight modifications):

    Host github.com
        User git
        Hostname github.com
        PreferredAuthentications publickey
        IdentityFile ~/.skm/keys/git/id_rsa
    Host fedoraproject.org
        Hostname fedoraproject.org
        PreferredAuthentications publickey
        IdentityFile ~/.skm/keys/fedoraproject/id_rsa
    Host fedorapeople.org
        Hostname fedorapeople.org
        PreferredAuthentications publickey
        IdentityFile ~/.skm/keys/fedoraproject/id_rsa




[BitBucket]: http://bitbucket.org
[GitHub]: http://github.com
[RubyGems]: http://rubygems.org/pages/download
[Ruby]: http://www.ruby-lang.org
[post]: http://www.robotgoblin.co.uk/blog/2012/07/24/managing-multiple-ssh-keys/
[rvm]: http://rvm.io
[skm]: http://github.com/xuhdev/skm#readme
