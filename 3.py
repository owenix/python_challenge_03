#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  3.py
#  
import re

in_file = open('junk.txt')

in_string = in_file.read()

print(in_string)

matches = str(re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', in_string))

print(re.sub('[A-Z]', '', matches))

