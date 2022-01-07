import math
import statistics
import sys
import itertools


#expressionsplit():
    #return(Nothing)

def cutoffsplit(filename, cutoff):
    prox = []
    dist = []
    with open(filename) as fp:
        for line in fp.readlines():
            f = line.split()
            beg = int(f[1])
            end = int(f[2])
            seq = f[-1]

            if end <= cutoff:
                prox.append(seq)
            else:
                dist.append(seq)
    return(prox, dist)
