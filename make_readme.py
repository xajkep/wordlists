import os

print "# Wordlists\n\n"
out = list()

for dirname, dirnames, filenames in os.walk('.'):
    if '.git' in dirnames:
        dirnames.remove('.git')
    
    for subdirname in dirnames:
        print "## %s\n" % subdirname.title()
    
    for filename in filenames:
        if dirname != '.':
            lang = filename.split('_')[0].upper()
            details = ' '.join(filename.split('.')[0].split('_')[1:])
            out.append(" * [%s *%s*](%s/%s)" % (lang, details, dirname, filename))

out.sort()
print '\n'.join(out)