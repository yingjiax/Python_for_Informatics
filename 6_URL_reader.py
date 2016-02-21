# Wasnt sure what exactly the assignment wanted, but this seems to work.

import urllib
import re

# https://www.gutenberg.org/files/1342/1342-h/1342-h.htm#link2HCH0034

try: 
    url = raw_input('Enter - ');
    fhand = urllib.urlopen(url);
    count = 0; # only characters upper and lowercase a-z.
    adjusted_3000 = [];
    while count < 3000:
        new_char = fhand.read(1);
        adjusted_3000 = adjusted_3000 + re.findall('[A-Za-z]', new_char)
        count += 1; 
    print 'first 3000 thousand characters are: ', adjusted_3000;
    
    new_chars = fhand.read()
    entire_doc = adjusted_3000 + re.findall('[A-Za-z]', new_chars)
    print 'The length of the entire document is: ', len(entire_doc)    
except: 
    print "Bad link"


