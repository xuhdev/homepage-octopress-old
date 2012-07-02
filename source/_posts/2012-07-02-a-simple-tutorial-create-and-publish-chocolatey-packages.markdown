---
layout: post
title: "A Simple Tutorial: Create and Publish Chocolatey Packages"
date: 2012-07-02 11:12
comments: true
external-url: 
categories: [Chocolatey, Package Manager, Windows, Software Development]
---

[Chocolatey][] is a Machine Package Manager, somewhat like [Apt][], [RPM][] but
built with Windows. When you want to install a Windows application, with
Chocolatey, what you need to do is to simply run a one line command --
Chocolatey will automatically download and install this application for you.
While there is an [official guide][] on how to create and publish a package,
this tutorial is simpler.

<!-- more -->

## Create the Package

First, [install Chocolatey][Chocolatey] if you haven't done yet. Then, add
`%CHOCOLATEY_INSTALLATION%\bin` and
`%CHOCOLATEY_INSTALLATION%\chocolateyInstall` to the
[PATH environmental variable][], where `%CHOCOLATEY_INSTALLATION%` is the
Chocolatey installation path. The default installation directory is
`C:\Chocolatey`, so the paths you need to add to PATH variable are
`C:\Chocolatey\bin` and `C:\Chocolatey\chocolateyInstall` by default. If you
don't know how to modify environmental variables, take a look at
[this page](http://java.com/en/download/help/path.xml).

After the preparing work is done, let's create a new directory `myapp-package`
for our work. In this directory, create a file named `myapp.nuspec`, with the
following lines:

```xml
<?xml version="1.0"?>
<package xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <metadata>
    <id>myApp</id>
    <title>MyApp</title>
    <version>0.1.0.20120702</version>
    <authors>AppAuthor</authors>
    <owners>Myself</owners>
    <summary>This is an example App</summary>
    <description>Your descriptions here</description>
    <projectUrl>http://www.myapp.tld</projectUrl>
    <tags>some tags here</tags>
    <licenseUrl>http://www.myapp.tld/license.txt</licenseUrl>
    <requireLicenseAcceptance>false</requireLicenseAcceptance> <!-- or true if you require the user to accept the License before installing -->
    <iconUrl>http://www.myapp.tld/logo.png</iconUrl>
  </metadata>
</package>
```

Replace the content above with the information of your app (The `myapp.nuspec`
can be more complex than this, see [here][Nuspec Reference] for details). Save
the file.

Then create a `tools` directory, and copy [chocolateyInstall.ps1][] into the
`tools` directory. Follow the comments in [the template][chocolateyInstall.ps1]
to do some modifications to `chocolateyInstall.ps1`. For the simplist case, your
`chocolateyInstall.ps1` will contain only one line, something like:

```powershell
Install-ChocolateyPackage 'MyApp' 'msi' '/quiet' 'http://myapp.tld/myapp-0.1.0-x86.msi' 'http://myapp.tld/myapp-0.1.0-x64.msi' # The 64 bit package URL can be omitted.
```

Or for installation from a zip archive:

```powershell
Install-ChocolateyZipPackage 'MyApp' 'http://myapp.tld/myapp-0.1.0-x86.zip' "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
```

Save this file.

Switch the current working directory to the `myapp-package` directory. Run
`cpack` or `chocolatey pack` on the command line. See
[this page][Chocolatey Pack] for details about `cpack` (or `chocolatey pack`)
command. Then there should be a `myApp.0.1.0.20120702.nupkg` in the current
directory -- this is the package.

## Test the Package

Run the following command in `myapp-package` directory to test your package:

    cinst myApp -source %cd%

## Publish the Package

The easiest way (or, to be more accurate, the easiest way to learn) to publish
the package is to use the web interface. First, go to
[http://chocolatey.org/][Chocolatey] and get an account. Go to the [Upload
Package][] page, and upload your package there. Done!  There is an alternative
way to publish the package on command line, see [cpush][].

## 

You should be able to create a simple Chocolatey package now. For more details,
please take a look at the [official guide][]. Also, you can find many real
world examples [here](https://github.com/ferventcoder/nugetpackages).

* _FYI, this blog post was written after I made
[this package](http://chocolatey.org/packages/editorconfig.core). You can find
its source
[here](https://github.com/editorconfig/chocolatey-packages/tree/master/editorconfig-core)._



[Apt]: http://wiki.debian.org/Apt
[Chocolatey Pack]: https://github.com/chocolatey/chocolatey/wiki/CommandsPack
[Chocolatey]: http://chocolatey.org/
[Nuspec Reference]: http://docs.nuget.org/docs/reference/nuspec-reference
[PATH]: http://en.wikipedia.org/wiki/PATH_(variable)
[RPM]: http://rpm.org/
[Upload Package]: http://chocolatey.org/packages/upload
[chocolateyInstall.ps1]: https://github.com/chocolatey/chocolatey/wiki/ChocolateyInstallPS1
[cpush]: https://github.com/chocolatey/chocolatey/wiki/CommandsPush
[official guide]: https://github.com/chocolatey/chocolatey/wiki/CreatePackages
