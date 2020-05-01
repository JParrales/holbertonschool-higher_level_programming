#!/usr/bin/python3
import sys

if __name__ == "__main__":

    lenArg = len(sys.argv)
    numbrs = []

    for i in range(1, lenArg):
        numbrs.append(int(sys.argv[i]))

    print("{}".format(sum(numbrs)))
