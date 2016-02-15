# -*- coding: utf-8 -*-
"""
Michael Galarnyk
Assignment: Message Frequency Count
"""

d = {};

with open('Data_Files/mbox.txt', 'r') as f:

    for line in f:
        line = line.translate(None, '!\'#$%*:+')  # removing punctuation
        line = line.lower().split()
        try:
            if line[0] == 'from':
                d[line[1]] = d.get(line[1],0) + 1
        except:
            pass

message_freq = [];

for key, val in d.items():
    message_freq.append((val,key));

message_freq.sort(reverse=True)

print 'The person with the highest number of messages is:', message_freq[0][1], ' with ', message_freq[0][0], 'messages'
