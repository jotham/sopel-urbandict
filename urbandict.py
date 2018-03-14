from __future__ import print_function
import requests

BASE_URL = "http://api.urbandictionary.com/v0/define?term={}"
MAX_LINES = 2 # Maximum return lines for top definition

def urban_search(term):
    query = requests.get(BASE_URL.format(term)).json()
    if query:
        try:
            definition = query['list'][0]['definition'].strip()
            return [term, definition]
        except (IndexError, KeyError) as error:
            return None

try:
    import sopel.module
except ImportError:
    pass
else:
    from sopel.formatting import underline, bold
    @sopel.module.commands('urb', 'urban')
    @sopel.module.example('.urb cunt')
    def f_urban(bot, trigger):
        """Search Urban Dictionary for a dank definition"""
        if trigger.group(2):
           query = trigger.group(2).strip().lower()
           results = urban_search(query)
           if results:
               bot.say('{} — {}'.format(underline(results[0]), results[1]), trigger.sender, MAX_LINES)
        else:
            bot.say('Couldn\'t find anything for {}'.format(bold(query)))

if __name__ == '__main__':
    import sys
    query = 'cunt'
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
    print('Looking up "{}"'.format(query))
    results = urban_search(query)
    if results:
        print('{} — {}'.format(results[0], results[1]))
    else:
        print('Couldn\'t find anything for "{}"'.format(query))
