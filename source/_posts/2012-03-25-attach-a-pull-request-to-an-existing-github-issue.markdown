---
layout: post
title: Attach a Pull Request to an Existing GitHub Issue
date: 2012-03-25 21:17
comments: true
file_title: 2012-03-25-attach-a-pull-request-to-an-existing-github-issue
categories: [Software Development, GitHub, git]
---

{% include custom/post_initialization.html %}

[GitHub][] users may have this experience: after reporting an issue for a
project on GitHub, you suddenly found a solution to fix it. Then you want to
attach a [pull request][] to this issue, but by the time this article is
written, GitHub does not provide a web interface to attach a pull request to an
issue. However, no such web interface does not mean it's impossible -- a
command line tool called [**hub**][hub] could help you out.

<!-- more -->

Let's suppose that the project to which you submit the issue is called
"test-repo". The issue is `Issue #1`. The issue may look something like this:

![The Issue]({{ post_file_url }}/1.png)

You have forked this repo, and you have committed some modification in a branch
"my-changes" and pushed them to your repo. 

![The Fork]({{ post_file_url }}/2.png)

Now let's convert this issue to a pull request.

First follow the installation instructions on [hub project page][hub readme] to
install hub.

Then clone your fork to your local directory if you have not done so. Say your
local copy of the repo is at `/home/user/test-repo`. Switch your working
directory to the git repo directory:

    cd /home/user/test-repo

Then setup your [GitHub token][] for this repo. After the setup, use hub command
to attach a pull-request to the issue you have submitted:

    hub pull-request -i 1 -b ORIGINAL_AUTHOR:master -h YOUR_USER_NAME:my-changes

The number **1** in the above command means the number of the issue you created.
In this example, it's `Issue #1`, thus **1** is passed to the `-i` option.

Now this issue should look like this:

![The Issue]({{ post_file_url }}/3.png)

The pull request is now successfully attached to the issue.

[GitHub]: http://www.github.com
[pull request]: http://help.github.com/send-pull-requests
[hub]: https://github.com/defunkt/hub
[hub readme]: https://github.com/defunkt/hub#readme
[GitHub token]: http://help.github.com/set-your-user-name-email-and-github-token
