# -*- coding: utf-8 -*-
"""
Michael Galarnyk
Assignment: Files, Lists, and Split
"""

def freq_count(user_string, unique_words):
    for word in unique_words:
        print word, ":", user_string.count(word);
        
text_file_name = raw_input('Enter a text file please \n');
user_string = raw_input('What substring do you want ? \n')
with open('romeo.txt', 'r') as f:
    script_list = [];
    line_list = [];
    for line in f:
        line_list.extend(line.split());

for word in line_list:
    if word not in script_list:
        script_list.append(word);
         
script_list.sort();

freq_count(user_string, script_list);
