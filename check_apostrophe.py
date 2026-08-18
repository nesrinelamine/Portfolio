#!/usr/bin/env python3
import sys

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the src line from MatchyKhedma
start = content.find('images MatchyKhedma')
if start > -1:
    # Get the src attribute
    src_start = content.rfind('src=', start - 100, start)
    src_end = content.find('\n', start)
    src_line = content[src_start:src_end]
    print('Found src:', repr(src_line))
    
    # Check the apostrophe character
    d_pos = src_line.find('d')
    if d_pos > -1:
        char_after_d = src_line[d_pos+1]
        print('Character after d:', repr(char_after_d))
        print('Unicode code point:', ord(char_after_d))
        print('Hex:', hex(ord(char_after_d)))
        
        # Check if it's a curly apostrophe
        if ord(char_after_d) == 0x2019:  # Right single quotation mark
            print('ERROR: Using curly apostrophe (U+2019) instead of straight (U+0027)')
        elif ord(char_after_d) == 0x0027:  # Straight apostrophe
            print('OK: Using straight apostrophe')
