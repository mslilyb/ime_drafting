import math
import statistics
import sys


expressionsplit(Nothing):
    return(Nothing)

cutoffsplit(filename, cutoff):
    with open(filename) as fp:
        for line in fp.readlines():
            f = line.split()
            beg = int(f[1])
            end = int(f[2])
            seq = f[-1]

            if end <= cutoff:
