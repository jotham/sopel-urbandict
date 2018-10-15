# sopel-urbandict

Urban Dictionary phrase lookup script for Sopel IRC bot.

## Installation

Tested on Ubuntu 16.04 LTS.

Aside from Sopel itself, sopel-urbandict requires `requests`. Sopel itself has since version 6.3.0, so you probably already have it, but if you don't:

```
sudo pip3 install requests
```

## Testing

```
$ python3 sopel-urbandict/urbandict.py jack of all traits
Looking up "jack of all traits"
jack of all traits: A politically correct way of describing someone with multiple personality disorder
```
