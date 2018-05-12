Title: Website Brutalism, or, making this site better for everyone
Date: 2018-05-12 22:15
Category: Tech
Tags: newblog
Slug: brutalism
Author: Jamie Luck
Summary: All it needs is some <blink\>

My website design has felt stale to me for quite some time. I love getting comments from engineers about my command-line interface, but the full-screen design of the page hid a lot of the content I've been creating. Did you know I have a blog? Neither did anyone else! I recently moved all my content to a static site generator so I could start combining all my blog posts with the main landing page, and today that effort has come to fruition.

The new interface is designed to focus on the content first and the styling afterward. As you can tell from the old site, I don't care about having a flashy UI or following the latest web design trend. I've been trying to stick to a few basic principles this time:

- Responsive design for a multitude of screen sizes
- Accessibility
- Small pagesize to reduce network bandwidth and decrease load times
- Removing requirement on Javascript

I made a bunch of important changes to the site to achieve these goals. I learned how to use flexboxes and some slightly more advanced CSS tricks like targeting elements within other selectors. I don't have a sophisticated set of tools in my web design toolbox, but it's fun to learn some more basics each time I redo this site. I've tested the site on a bunch of different screen sizes & text-mode web browsers, it seems to work well.

Accessibility was a priority in this redesign, but I didn't know a lot going in so I read guidelines and took some lessons from the internet. I preferred the use of high contrast colors, standard fonts, and a semantic layout that should be easily understood by screen readers. If you're reading this site on an assistive device that doesn't support the content well, please let me know!

The average page on this site weighs in under 20kb on the wire, plus image size. The one you're reading right now was 11kb compressed. This is a substantial improvement from my last design, about 30x on the homepage. That involved the transfer of about 300kb of Javascript, and an ungodly amount on [svbtle](https://svbtle.com) where my blog was previously hosted.

I moved the command-line interface out to a separate page, [which you can find here](https://cli.jamieluck.com). The refactor of that interface also moved it to a separate [repository on my github](https://github.com/delucks/cli.jamieluck.com) so I can deploy it separately from the main site. This is the only part of my site that has a hard requirement on Javascript to function properly, so I wanted to make sure that people could use the main site without needing to have Javascript enabled. Why the hate for Javascript? Well, I think the requirement to have Javascript installed is overly normalized in today's web design culture. Javascript opens up new avenues of risk for the users of a website- do you trust the page author to not include malicious payloads? Are identifying characteristics about your browser being transmitted to third parties via analytics scripts? I don't want to expose the users of my website to these kinds of questions, so I avoid it as much as possible. I also want to respect the choice of those that disable Javascript by default in their web browsers. You can achieve a lot of functionality without Javascript while retaining concern for users' choice and privacy.

Anyway this will be much nicer for me to write content on since I can write it in vim and publish it with git, rather than logging into a damn website. I hope you enjoy it.
