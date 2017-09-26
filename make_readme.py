import os

def line_count(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

print "# Wordlists\n\n"
lists = {}

for dirname, dirnames, filenames in os.walk('.'):
    if '.git' in dirnames:
        dirnames.remove('.git')
    
    

    for subdirname in dirnames:
        lists[subdirname] = []
        
    
    for filename in filenames:
        if dirname != '.':
            lang = filename.split('_')[0].upper()
            details = ' '.join(filename.split('.')[0].split('_')[1:])
            number_of_line = line_count(os.path.join(dirname, filename))
            lists[dirname[2:]].append(" * [%s *%s*](%s/%s) (**%i** words)" % (lang, details, dirname, filename, number_of_line))

for k, v in lists.iteritems():
    print "## %s\n" % k.title()
    v.sort()
    print '\n'.join(v)
    print ""

print """
## Others Repositories

 * [FUZZING - SecLists](https://github.com/danielmiessler/SecLists)
 * [FUZZING - FuzzDB](https://github.com/fuzzdb-project/fuzzdb/)
 * [DOMAIN - Easylist](https://github.com/easylist/easylist)
 * [DOMAIN - Fanboy/Adblock](https://github.com/ryanbr/fanboy-adblock)
 * [DICTIONNARY - English Words](https://github.com/dwyl/english-words)
 * [DICTIONNARY - Probable Wordlists](https://github.com/berzerk0/Probable-Wordlists)

## External Ressources

 * [DNS - Cisco Umbrella Top 1 million](http://s3-us-west-1.amazonaws.com/umbrella-static/top-1m.csv.zip)
 * [DNS - Cisco Umbrella Top TLDs](http://s3-us-west-1.amazonaws.com/umbrella-static/top-1m-TLD.csv.zip)
 * [DNS - Alexa Top 1 million](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip)
 * [DOMAIN - FilterLists](https://filterlists.com/)
 * [PASSWORD - OpenWall](http://www.openwall.com/wordlists/)
 * [PASSWORD - CrackStation](https://crackstation.net/buy-crackstation-wordlist-password-cracking-dictionary.htm)
 * [PASSWORD - g0tmi1k's blog](http://blog.g0tmi1k.com/2011/06/dictionaries-wordlists/)
 * [PASSOWRD - Skull Security](https://wiki.skullsecurity.org/Passwords)
 * [WORDLIST - Hashcrack](http://hashcrack.blogspot.ch/p/wordlist-downloads_29.html)
 * [WORDLIST - md5this](http://www.md5this.com/tools/wordlists.html)
 * [WORDLIST - Packet Storm](https://packetstormsecurity.com/Crackers/wordlists/)
"""