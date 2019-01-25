Title: TIL- bash's `until` builtin
Date: 2019-01-25 15:12
Category: Tech
Tags: shell
Slug: bash-until
Author: Jamie Luck

I've been a heavy `bash` user for years. Writing `while` loops has been part of my bash bread & butter; on systems that don't have the Linuxy `watch` command I inevitably write some kind of `while :; do date; command; sleep 10; clear; done` during my average terminal session. Today a coworker showed me about `until`, which is like `while` but the logical opposite. To illustrate what I mean, check out this bash loop that would never run:

```shell
while false; do
  echo "You will ever see me"
done
```

The `until` builtin substituted for `while` there would make the loop run infinitely!


```shell
until false; do
  echo "You will see a whole lot of me"
done
```

To quote the `help until` output, ah... fuck it, let's just include the whole thing.

```
until: until COMMANDS; do COMMANDS; done
    Execute commands as long as a test does not succeed.
    
    Expand and execute COMMANDS as long as the final command in the
    `until' COMMANDS has an exit status which is not zero.
    
    Exit Status:
    Returns the status of the last command executed.
```

It's essentially `while ! command; do ...; done`. How neat is that!
