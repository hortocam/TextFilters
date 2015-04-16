#!/usr/bin/python
import fileinput
print ''.join([line.strip() for line in fileinput.input()], ',')
