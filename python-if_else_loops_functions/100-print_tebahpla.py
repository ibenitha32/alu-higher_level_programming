#!/usr/bin/python3
for alpha in range(ord('z'), ord('a')-1, -1):
    if alpha % 2 != 0:
        print("{}".format(chr(alpha-32)), end="")
    else:
        print(f"{chr(alpha)}", end="")
