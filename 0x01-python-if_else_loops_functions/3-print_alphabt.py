#!/usr/bin/python3
for i in range(122, 96, -1):
    if i == ord("q") or i == ord("e"):
        continue
    print("{:s}".format(chr(i)), end='')
