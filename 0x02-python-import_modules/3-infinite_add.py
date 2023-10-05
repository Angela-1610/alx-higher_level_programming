#!/usr/bin/python3
if __name__ == "__main__":
    """task 3."""
import sys
args = len(sys.argv) - 1
sum = 0
for i in range(args):
    sum = sum + int(sys.argv[i + 1])
print("{}".format(sum))
