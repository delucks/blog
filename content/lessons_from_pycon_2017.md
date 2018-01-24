Title: Lessons from Pycon 2017
Date: 2017-05-22 00:00
Modified: 2017-05-22 00:00
Category: Tech
Tags: svbtle-migrated,python,pycon,notes,conference
Slug: lessons-from-pycon-2017
Author: Jamie Luck
Summary: My summary of talks I watched at Pycon 2017


This post describes some of the talks and things I learned at pycon this year. I got to see a limited subset of talks and I definitely missed a bunch of interesting ones- these are my favorites!


# Requests Under the Hood
#### [Link to Recording](https://www.youtube.com/watch?v=ptbCIvve6-k)

This talk was more focused on software maintenance patterns than the `requests` library itself, which was used as an example throughout. It presented a few scenarios from the library where critical code for an infrequently-used feature was slowly added to throughout time.

**Main takeaways**:
- The most complex, hard to modify code in a software project are the features that are used the least
- The quick hacky fix is never temporary
- Never hide from mistakes in your codebase, even if users don't complain about them


# Rants & Ruminations from 100 Job Interviews in Silicon Valley
#### [Link to Recording](https://www.youtube.com/watch?v=uzz5AaCWMps)

This was a great culture talk which dealt with a lack of respect shown in many common job application scenarios. The author relayed a number of relatable experiences over 100 interviews with various companies in the Bay Area.

**Main takeaways**:
- Take-home code assignments are not a good measure of the candidate's skill
- Most interviews don't give feedback to the candidate on what to improve, making them ultimately not valuable unless the candidate passes
- Interviewers should know exactly what they are looking for before entering the room
- Lowballing salary offers and interviews that pedantically focus on basics display a lack of respect for the candidate
- The best thing to provide a candidate pre-interview is an outline of what is expected from them, with specific-enough descriptions of the problems that entails


# Awesome Command-Line Tools
#### [Link to Recording](https://www.youtube.com/watch?v=hJhZhLg3obk)

This was a fun talk for me, being a lover of command-line interfaces. The author created tools like `pgcli` and `mycli`, which are impressively smart command-line shells for databases postgresql and mysql respectively.
They walked through a few examples of design principles to follow when creating user interfaces for tools, and gave a few libraries that are useful for implementing this in a pythonic fashion.

**Libraries used**:
- [python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit)
- [pygments](http://pygments.org/)
- [click](https://github.com/pallets/click)

**Main takeaways**:
- A user focus in program design will make your program more intuitive
- Make features of the program discoverable; don't hide them behind arcane keyboard combinations unless they make sense that way
- Make documentation readily available from within the program
- Configuration should be for subjective options only; unnecessary config options mean that sane defaults haven't been chosen
- `python-prompt-toolkit` is really awesome if you are making a REPL


# Satellite Imagery using Python
#### [Link to Recording](https://www.youtube.com/watch?v=rUUgLsspTZA)
#### [Code](https://github.com/kscottz/PythonFromSpace)

This was really interesting, and I would highly recommend watching the recorded talk. The presenter is good at illustrating what happens as they step through a jupyter notebook that illustrates doing cool things with satellite images, esp. animating them.

**Main takeaways**:
- Space is a public/private shared area, most free images come from NASA/ESA/other public space agencies although commercial ones also typically have a free tier
- Using satellite imagery requires a non-trivial amount of libraries and computing power
- BUT, using satellite imagery is straightforward conceptually
- The talk links to all libraries required to do this yourself


# Algorithmic Music Generation
#### [Link to Recording](https://www.youtube.com/watch?v=Kk33YgJuDfk)
[Code](https://github.com/unnati-xyz/music-generation)

This talk walks through how "easy" it is to generate entirely unique music using a large training set and a recurrent neural network implemented using the `keras` library.

**Main takeaways**:
- LSTM RNNs are the most appropriate type for this use case
- Normalization of the input data requires translation from lossy to lossless formats
- Many, many iterations of the training set will be required to produce anything that sounds remotely like music


# Creating a Good Library API
#### [Link to Recording](https://www.youtube.com/watch?v=4mkFfce46zE)

I have a few python libraries and polishing their APIs is a priority at all times, I paid close attention throughout this talk. The author stated four values for writing libraries:
- Simplicity
- Flexibility
- Consistency
- Safety
They talked about the first two and trade-offs to be made between them and ended with this quote:

```
An API should make the simple easy, the complex possible, and the wrong impossible
```

**Main takeaways**:
- Write your README first, describing the user experience from the beginning
- Reduce clutter through progressive disclosure
- Avoid cumbersome inputs (like things wrapped in lists) and required object creation just to call basic methods
- Create abstraction to focus on the "what" over the "how"
- Making your API granular & composable helps with incorporating flexibility: can users subclass something to provide extra functionality?


# Running python in the Linux Kernel with bpf
#### [Link to Recording](https://www.youtube.com/watch?v=CpqMroMBGP4)

This guy was a good presenter with a great sense of humor about the ridiculousness of what he managed to fit into bpf's stack-based machine. It was pretty impressive though,
and included a strace-esque syscall notifier that was implemented in like ~50 lines.

**Main takeaways**:
- If you reduce the amount of language features you have, you can fit a lot of python bytecode operations into a very limited transpiling target architecture
- I can't wait for this code to be open source


# Immutable programming: Writing Functional Python
#### [Link to Recording](https://www.youtube.com/watch?v=_OLEVvjrIj8)

This talk was an overview of different strategies one can take to program (mostly) functionally using python.
It spent a good amount of time talking about datastructures that are useful for this purpose, and how to write Command pattern code which can take inherently mutable parts of your codebase and glue them to the immutable core of the codebase.

**Main takeaways**:
- Immutability enables local thinking in a codebase
- Main libraries to use when writing immutable datastructures: `namedtuple`, `frozenset`, `str` and other primitives
- User input and other inherently mutable parts can be adapted using the Command design pattern


# Grok the GIL
#### [Link to Recording](https://www.youtube.com/watch?v=7SSYhuk5hmc)

I liked this talk a lot. The presenter dove into the cpython codebase, pointed out situations where the GIL can be acquired and released, then walked through examples showing good places to use `multiprocessing` versus `threading`.

**Main takeaways**:
- Python supports both preemtive and cooperative multitasking, but it's ultimately single-threaded in the reference implementation.
- Locks are required when mutable state is used in a multithreaded environment
- Use threads for concurrency, processes for parallelism


# No Hands! Bikes with Python
#### [Link to Recording](https://www.youtube.com/watch?v=D-5V7s0GflU)
#### [Code](https://github.com/betatim/pycon17-no-hands)

This talk used the really cool [micropython project](https://micropython.org/) to build a practical speedometer for a bike! They walked (and biked) through the whole process. I would recommend watching this if you're interested in microcontrollers.

**Main takeaways**:
- Micropython is powerful enough to run a significant application on an Arduino-sized board
- ESP8266 is a good board for hobbyist purposes and has onboard wifi


# Hacking Cars with Python
#### [Link to Recording](https://www.youtube.com/watch?v=3bZNhMcv4Y8)
#### [Code](https://github.com/linklayer/pyvit)

This talk covered the connection between different computer components in a typical car and how to interface with its CAN network to perform different operations within the car.

**Main takeaways**:
- Standards for cars are created to run over cheap components that are easy to mass-produce, so the protocols are fairly simple.
- The author's library encodes these protocols so you don't have to do it


# Hacking Nintendo Games in Python
#### [Link to Recording](https://www.youtube.com/watch?v=v75rNdPukuI)

This one was really fun. The presenter made a SMS gateway API to write memory addresses in an emulator, which led to the audience doing hilarious things with their game of Zelda.


# Debugging in 3.6: Harder, Better, Faster, Stronger
#### [Link to Recording](https://www.youtube.com/watch?v=NdObDUbLjdg)
[Code](https://github.com/Elizaveta239/frame-eval)

This was another impressive talk, where the presenter made their own frame evaluation debugger for 3.6 with a new field in PyCodeObject.


# Keynote on Instagram's python3 migration
#### [Link to Recording](https://www.youtube.com/watch?v=66XoCk79kjM)

I missed the first part of this talk, so my notes are a bit incomplete.

**Main takeaways**:
- Unit tests for python3 compatibility are straightforward to write and act as a good measuring stick for your migration progress
- Roll out slowly, through employee whitelists and A/B segments
- Unicode/binary bugs can be hard to track down, and some modules have specific needs


# Facts and Miscellany

This is stuff I gleaned from presentations that wasn't explicitly pointed out above.

How to define default args for a namedtuple:
```python
from collections import namedtuple
Rectangle = namedtuple('Rectangle', ['height', 'weight'])
Rectangle.__new__.__defaults__ = (10, 20)
```

How to allow GIL re-acquisition every tick in cpython, which makes multithreaded contention bugs easier to reproduce:
```python
import sys
sys.setcheckinterval(1)
```

How to disassemble python into bytecode:
```python
import dis
dis.dis(name)
```
