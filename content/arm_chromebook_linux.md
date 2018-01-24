Title: Installing "Real" Linux on an ARM Chromebook
Date: 2014-09-30 00:00
Modified: 2014-09-30 00:00
Category: Tech
Tags: svbtle-migrated,chromebook,linux,arm
Slug: installing-real-linux-on-arm-chromebook
Author: Jamie Luck
Summary: How to install Archlinux ARM on a Samsung ARM Chromebook

I'm the proud owner of a Samsung Chromebook, first model, the lightest and longest-lasting laptop I've ever had the pleasure of owning. It's got a dual-core ARMv7 processor at 1.7GHz, a quad-core GPU, and 2GB RAM. I've had it for a bit over a year now, during which I used the included Chrome OS to death.

I figured when I was purchasing it that the Linux base of Chrome OS meant I'd be able to hack it to my heart's content. That's… less than accurate. Chrome OS has many nice features, most notably a (post developer-mode switch) root shell to the underlying operating system. This allowed me to bootstrap dnschneid/crouton and run a variety of Linux chroots. I briefly had some fun with a Kali chroot, and installed Arch in a chroot to fulfill all my Linux needs. However, the chroot opens a new X display to display any X windows, and this is a pretty severe hit on performance. After getting by with this situation for a year, I started looking into a more permanent and hackable solution for my most portable laptop.

I settled on Archlinux ARM because, well, Archlinux is my favorite workstation OS right now. Also, it helps that my model of Chromebook was specifically listed on their site as a target model. I decided I'd install on the internal eMMC, as it would be significantly faster than all my USB2.0 drives, as well as much more portable. Their installation guide was okay, but I had to do a few things differently to make it work.
 
## Installing to eMMC

I installed my system via a SD card which had the Archlinux ARM filesystem tarball unpacked on it, as described in their guide. The Archlinux ARM guide assumes that you're creating this removable drive from Chrome OS, which I did for the first step.

One important part they leave out is copying over any tools you'll need to repeat the instructions from the removable drive. This includes cgpt, the ChromeOS partitioning tool. It's a statically linked executable, so you can just

```shell
sudo cp $(which cgpt) /path/to/my/rootfs/bin/
```

to get the file onto your install drive (mounted rootfs at `/path/to/my/rootfs/`). I'd also recommend keeping around copies of the Archlinux tarball, kernel, u-boot script, and nv-U-Boot generated in the guide in case anything goes wrong.

After rebooting into the removable drive, I first ran into my first problem with the installation. I idiotically forgot to edit /etc/fstab and set my boot partition correctly, so the second time I booted it failed. Thankfully that was pretty easy to change from another computer, so I rebooted and installed Arch in a similar way from the removable media onto the eMMC. After finishing the install, I found the eMMC wouldn't boot whatsoever. I then realized I forgot to edit /etc/fstab/ again, not allowing the system to boot correctly.

Great, so I figured I'd just boot into the Archlinux removable media and fix it. Not so easy. I started getting TONS of kernel logging messages echoed to my ttys, making typing any commands impossible. Thanks to this forum thread , I was able to silence the messages temporarily using

```shell
dmesg -n1
```

and permanently using the ‘quiet' kernel option on the next boot.

With my logging spam taken care of, I was able to edit /etc/fstab and get the system to boot fine. I copied the cgpt binary and my other resources onto the hard drive, and kept a copy on an external drive in case I ever need to rescue the machine.
 
## Usability

Linux on the Chromebook feels just as usable as Chrome OS. In some ways it's very difficult, yet in others I find it much more efficient.
 
### Thorns

- HDMI doesn't work, at least not from the ~30 minutes I spent hacking around with xrandr
- Audio output via alsa is clunky, but easily scriptable
- Battery life seems slightly less, I'd assume due to CPU tuning of Chrome OS
- I have no warranty anymore
 
### Roses

- Using multiple terminals at once is really easy
- Video framerate using the Google-developed video driver is comparable to ChromeOS performance on HTML5
- More software, consistent selection of good general and specific tools
- Have access to entire internal drive space
- You keep the 100GB free Google Drive space
 
## Going Forward

I've been using Linux on the Chromebook for about 3 weeks now, and I've been updating this article as I work on more things with it. I really enjoy it a lot, especially since using the same window manager (herbstluftwm) between my main laptop and my Chromebook makes life slightly more efficient. I've created a new branch of my github dotfiles repo specifically for the Chromebook, and I've been customizing my configurations there to make things feel like home.

Would I recommend making the switch for any \*nix power user? Definitely.
For someone who wants a smooth experience? No.

But I had fun with it!

Feel free to shoot me any questions you have about anything I wrote here. Contact info is on my [homepage](https://jamieluck.com).
