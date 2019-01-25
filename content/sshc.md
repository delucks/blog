Title: Introducing `sshc`
Date: 2019-01-25 15:35
Category: Software
Tags: release,oss,golang
Slug: introducing-sshc
Author: Jamie Luck
Summary: `sshc` is a tool for working with your SSH configuration file


As a developer and sysadmin who works on Unix/Linux, I use `ssh` a lot. I maintain `~/.ssh/config` files on at least six different machines, hundreds of lines of config in total. To manage all of the complexity contained within those files I have been writing a tool called [`sshc`](https://github.com/delucks/sshc). `sshc` lets you push host definitions between hosts and retrieve information from your local `~/.ssh/config` file.

For these examples, I'll be using a simple SSH config file that I've pasted below:

```text
Host *
  ControlMaster yes
  ControlPath ~/.ssh/%u_at_%h_%p.ssh.master.mux
  ControlPersist 300
  IdentityFile %d/.ssh/id_rsa.pub

Host github.com
  User git
  Port 22

Host staging
  User delucks
  Port 5522
  HostName earlyinteg.corporation.com

Host production
  User delucks
  Port 22
  HostName eng-gateway.corporation.com
```

Even for a small ssh config, there's lots of information in there- useful information! You can use that file to reference where the login point for your company's production environment is hosted, how long your controlmaster sockets will last, and what RSA key you're using to authenticate. `sshc` is very useful for getting targeted bits of that information from your config file to use elsewhere. You can retrieve single-host defininitions keyed by `Host` directive with `sshc get`, optionally returning that in JSON format:

```text
$ sshc get staging
Host staging
  User delucks
  Port 5522
  HostName earlyinteg.corporation.com

$ sshc get -j staging
{
  "HostName": "earlyinteg.corporation.com",
  "Port": "5522",
  "User": "delucks"
}
```

Let's say you have a HTTP server running on port 8080 of your company's production server. You could manually look at your ssh config and pull out the hostname, or you could just run `curl http://$(sshc get -j production | jq .HostName):8080/`. The JSON output for `sshc get` makes it easy to get specific properties from your host definitions by filtering them with the wide ecosystem of JSON-processing tools (`jq` used here).

What if you don't remember what `Host`s are in your ssh configuration?

```text
$ sshc hosts
*
github.com
staging
production
```

You see the `*` entry is listed there too- by default that won't show up in `sshc get` output but you can override that behavior with the `-w`/`--include-wildcards` flag:

```text
$ sshc get -w '*'
Host *
  ControlMaster yes
  ControlPath ~/.ssh/%u_at_%h_%p.ssh.master.mux
  ControlPersist 300
  IdentityFile %d/.ssh/id_rsa.pub

```

Note the whitespace- `sshc` uses a whitespace and comment-preserving parser library so comments and extra whitespace will appear in the Host block preceding them.

You can also search through all Host blocks using the `find` subcommand. `sshc find` will search through your configuration using a regex match, returning the full blocks that match your search. This is a substantial edge over using using `grep` to search through your configuration because it includes all necessary context from the matching Host blocks. Adding this in with `grep -C` is difficult to get right and frequently overselects.

```text
$ sshc find '\.corporation\.com'
Host staging
  User delucks
  Port 5522
  HostName earlyinteg.corporation.com

Host production
  User delucks
  Port 22
  HostName eng-gateway.corporation.com
```

If you're passing the `--color` flag to `sshc`, the matching parts of the host blocks will be highlighted. `sshc find` is aliased to `grep` and `search` as well, so this is valid:

```text
$ sshc grep git
Host github.com
  User git
  Port 22
```

The last command I'll highlight here is the reason I created `sshc`. Over time using many machines via `ssh`, I've had to maintain multiple ssh configuration files, one per workstation. I have a laptop and a desktop for development at my job, and I have a different user ssh config on each based on what hosts I've logged into frequently from each environment. When I would get access to a new host, I'd add a `~/.ssh/config` block for it on my laptop, then eventually retype the same block on my desktop's `~/.ssh/config`. Over time, maintaining these two essentially equivalent configs became frustrating as it's an unnecessary time-sink.

So, I wrote `sshc copy`. This command takes a `Host` block from your local `~/.ssh/config` and appends it to the end of another host's ssh config. This is useful for "pushing" host definitions across the wire to other workstations in your environment.

Let's say you just added this definition to the config block above.

```text
Host foobar
  HostName test.corporation.com
  Port 1025
```

To copy that definition from your local host to the `staging` host defined in your config, run `sshc copy foobar staging`. `sshc` forks off an instance of `ssh` that copies an escaped version of the block from your local configuration over the ssh pipe and appends it to the remote host's `~/.ssh/config` (path is configurable of course).

To my knowledge this is the only script that performs that specific use-case. Yay! I hope you find `sshc` as useful as I do.
