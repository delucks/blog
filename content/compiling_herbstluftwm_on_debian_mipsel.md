Title: Compiling Herbstluftwm on Debian MIPSel
Date: 2014-12-17 00:00
Modified-Date: 2014-12-17 00:00
Category: Tech
Tags: short,linux
Slug: compiling-herbstluftwm-on-debian-mipsel
Author: Jamie Luck
Summary: Building the herbstluftwm window manager on a Debian MIPS32 dev board

This'll be a short post about how I've gotten my favorite window manager, [herbstluftwm](http://herbstluftwm.org/) to work properly on a 32-bit little-endian mips board under Debian GNU/Linux. The specific board I'm targeting is a [Creator CI20](http://elinux.org/MIPS_Creator_CI20), which I'm trying to use as a workstation at the moment. 

There's [a package](https://packages.debian.org/wheezy/herbstluftwm) for herbstluftwm available in the official repositories, but it's version 0.3, which lags behind the development version by quite a bit. I use a bleeding-edge git version on my laptop, and I'm a fan of the features they've introduced recently, like a reorganized theming configuration syntax. So, I'm going to be downloading/compiling/installing from git so I can get these features.

First, ```git clone git://git.cs.fau.de/hlwm```. You'll need GCC and G++ version 4.7 to install, as they support the '-std=c++11' compiler option, which herbstluftwm requires. The Creator CI20's Debian distribution does not come with this compiler by default, so you'll have to install it. ```sudo apt-get install gcc-4.7 g++-4.7```

Next, library dependencies. You'll need all these to compile.

* asciidoc (if you build the documentation)
* libxext-dev
* libx11-dev

Then, a `make CC=/usr/bin/gcc-4.7 CXX=/usr/bin/g++-4.7` should sort you out.

If you're reading this on a CI20, herbstluftwm is a great choice for a minimal window manager that won't slow down X the same way xfce and other desktop environments do. 
