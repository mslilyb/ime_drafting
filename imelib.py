import math
import statistics
import sys
import itertools as iter


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

def kmercount(seqs, k): #determines the total count of kmers in the sequences
    don = 5 #donor seqeuence
    acc = 10 #acceptor sequence. we're...hardcoding these, I guess. Not a fan.
    total = 0
    decay = 1
    count = {}
    filter = list(iter.product('ACTG', repeat=5))
    for i in range(0, len(filter)):
            filter[i] = ''.join(filter[i])
    #print(filter)
    for s in seqs:
        for i in range(don, len(s)-k+1-acc):
            kmer = s[i:i+k]
            if kmer in filter:
                if kmer not in count:
                    count[kmer] = 0
                count[kmer] += decay #to factor in geom decay, to account for intron significance dropping off as it lengthens
                total += decay #pretty sure we want to make the total with the decay as well
            #some sort of decay function...
            if (decay):
                """
                can't be flat...can it? every 50 bases you turn it down by like 0.1? because
                depending on how long or short the intron is you won't account for the start vs. end consistently
                so maybe we take the whole length and every increment we decrement the decay. This makes it
                consistent across introns regardless of length.

                In order to do this, I think I need a cutoff, like where in the intron the significance drops
                off. May have to be experimentally determined...but if it's a cutoff, a flat value may make more
                sense. Does a 1000bp intron have a larger "range of significance" than a 100bp one? Good to ask!

                decay function draft, flat decrement value
                #lets assume without cause that anything after 100 bp is less important...by some...proportion...
                sig_assumed = 100
                rate_assumed = 0.5
                if i+k <= sig_assumed -1:
                    decay *= rate_assumed
                    sig_assumed += sig_assumed
                #okay...now lets say instead the decay is more based on how far on any given intron you've gone down.
                #The assumptions here are again a suitable rate of decay and how often you want to decrement.
                rate_assumed = 0.5
                proportion_assumed = 0.1
                sig_interval = len(s) * proportion_assumed
                #then again, the same idea
                if i+k <= sig_interval -1:
                    decay *= rate_assumed
                    sig_interval += sig_interval
                """
    return(count, total) #returns a tuple, a dictionary keyed with unique kmers and their counts, and the total number)

def kmerfreqs(counts): #determines frequencies of kmers across an introns
    #print(counts)
