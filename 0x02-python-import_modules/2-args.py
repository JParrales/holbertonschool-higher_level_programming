#!/usr/bin/python3
import sys

if __name__ == "__main__":

    lenArg = len(sys.argv)

    if lenArg > 2:
        for i in range(lenArg):

            if i == 0:
                print("{} arguments:".format(lenArg - 1))
            else:
                print("{}: {}".format(i, sys.argv[i]))
    elif lenArg == 1:
        print("0 arguments.")
    else:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
