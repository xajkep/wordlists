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
            lists[dirname[2:]].append(" * [%s *%s*](%s/%s) (**%s** words)" % (lang, details, dirname, filename, "{0:,}".format(number_of_line).replace(',', "'")))

for k, v in lists.iteritems():
    print "## %s\n" % k.title()
    v.sort()
    print '\n'.join(v)
    print ""

print """
## Large Password Lists (Torrent)
 * [CrackStation's Password Cracking Dictionary [ONLY "real human" passwords] - 247MB compressed](https://crackstation.net/downloads/crackstation-human-only.txt.gz.torrent)
 * [CrackStation's Password Cracking Dictionary [FULL] - 4.2GB compressed](https://crackstation.net/downloads/crackstation.txt.gz.torrent)

## Large Password Lists (HTTP Direct Download)

 * [10-million-combos.zip - 85MB compressed](http://download.g0tmi1k.com/wordlists/large/10-million-combos.zip)
 * [crackstation-human-only.txt.gz - 246MB compressed](http://download.g0tmi1k.com/wordlists/large/crackstation-human-only.txt.gz)
 * [b0n3z_dictionary-SPLIT-BY-LENGTH-34.6GB.7z - 3GB compressed](http://download.g0tmi1k.com/wordlists/large/b0n3z_dictionary-SPLIT-BY-LENGTH-34.6GB.7z)
 * [crackstation.txt.gz - 4GB compressed](http://download.g0tmi1k.com/wordlists/large/crackstation.txt.gz)
 * [WPA-PSK WORDLIST 3 Final (13 GB).rar - 4GB compressed](http://download.g0tmi1k.com/wordlists/large/WPA-PSK%20WORDLIST%203%20Final%20%2813%20GB%29.rar)
 * [36.4GB-18_in_1.lst.7z - 5GB compressed](http://download.g0tmi1k.com/wordlists/large/36.4GB-18_in_1.lst.7z)
 * [b0n3z-wordlist-sorted_REPACK-69.3GB.7z - 9GB compressed](http://download.g0tmi1k.com/wordlists/large/b0n3z-wordlist-sorted_REPACK-69.3GB.7z)
 
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
 * [FIRST & LAST NAMES - philipperemy](https://github.com/philipperemy/name-dataset)

## Thanks to

 * [URLTeam](https://www.archiveteam.org/index.php/URLTeam)
"""
