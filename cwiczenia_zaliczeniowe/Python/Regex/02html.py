'''
>>> get_emails()
['monika.krol@uj.edu.pl','dorota.gumula@uj.edu.pl','sekr@oa.uj.edu.pl','a.czelusniak@uj.edu.pl','ewa.lanoszka@uj.edu.pl','smp@uj.edu.pl']
'''

import re
import urllib2


def get_emails():
    handler = urllib2.urlopen("http://www.fais.uj.edu.pl/dla-kandydatow/sekretariaty-dydaktyczne")
    html = handler.read()
    pattern = r"[a-zA-Z0-9][a-zA-Z0-9.\-_]*[a-zA-Z0-9\-_]@[a-zA-Z\.]+"
    regexp = re.compile(pattern, re.MULTILINE)
    return list(set(regexp.findall(html)))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
