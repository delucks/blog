Title: Quick Script: Tape Inventory
Date: 2016-05-21 00:00
Modified: 2016-05-21 00:00
Category: Tech
Tags: svbtle-migrated,python,data,sanitization
Slug: quick-script-tape-inventory
Author: Jamie Luck
Summary: I wrote an ad-hoc python script that helped me inventory a cassette tape collection


Skills with programming can be useful in all kinds of daily life situations! I just encountered one where I was making an inventory of some cassette tapes I'm getting rid of. 

I jotted down the list of tapes in a quick, rough format of "artist - album", unless it was a compilation or collection, in which case I just wrote the name on the tape. 

I want to give this list to my relatives who will undoubtably be using spreadsheet software, so I want to munge this rough list into a nicely formatted spreadsheet for them. Let's write a quick script!!

## Input

Here's a sample of my notes file:
```
frank sinatra - academy award winners
the pachelbel canon and other baroque favorites
prince and the revolution - around the world in a day
talking heads - little creatures
crosby, stills, & nash - self-titled
```

I want to make sure that the following things are fixed:
- Artists and albums are separated by commas so it's treated as a CSV
- Self-titled albums should be replaced by the name of the band
- The First Letter Of Every Word Should Be Capitalized
- Compilations or collections should have their artist set to "Collection"

Let's get to work!

## Writing Something

I'm going to be using python, since it's my favorite language and it's easy to talk about.
Modules I'll be using:
- [`fileinput`](https://docs.python.org/3/library/fileinput.html) takes standard input and iterates over every line (I'll be putting the input file in through stdin)
- [`string.capwords`](https://docs.python.org/3/library/string.html#string-functions) capitalizes the first letter of every word in a provided string

I start this script out the way you usually start scripts that use `fileinput`:

```python
import fileinput
from string import capwords

for line in fileinput.input():
    # do stuff
```

Now that we have access to each line of the file in a variable called `line`, let's work with lines that contain an "artist - album":

```python
for line in fileinput.input():
    if '-' in line:
        # contains artist - album
        sp = line.split('-')
        artist = sp[0]
        album = '-'.join(sp[1:]).strip()
        if album == 'Self Titled':
            album = artist
```

As you can see, this handles splitting apart the album and artist portions of the line, and then sets the album name appropriately for self-titled albums. Next, we need to handle the case of a line that doesn't contain "-", a collection:

```python
    else:
        # some kind of collection, collaboration, etc
        album = line
        artist = 'Collection'
```

Easy, the whole line is the name of the album. Now to output each line:

```python
    print '{0},{1}'.format(capwords(artist), capwords(album))
```

This capitalizes the album and artist after we've decided what they're going to be. That's the end of this little script! I invoked it like:

```shell
cat tapes.txt | python parsetapes.py | tee tapes.csv
```

and there we go! A spreadsheet full of usefully parsed tape information. 

Thanks for reading! 

## The Script

```python
import fileinput
from string import capwords

for line in fileinput.input():
    if '-' in line:
        # contains artist - album
        sp = line.split('-')
        artist = sp[0]
        album = '-'.join(sp[1:]).strip()
        if album == 'Self Titled':
            album = artist
    else:
        # some kind of collection, collaboration, etc
        album = line
        artist = 'Collection'
    print '{0},{1}'.format(capwords(artist), capwords(album))
```
