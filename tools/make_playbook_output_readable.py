#!/usr/bin/env python
import sys

for line in sys.stdin:
    line.replace('\n\n', '\n')
    print line
