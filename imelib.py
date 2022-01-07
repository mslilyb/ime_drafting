import math
import statistics
import sys
import itertools as iter

def generatefilters(): #generates a list of legal kmers. in the future, user specified exceptions could be handled
    filter = {}
    perms = list(iter.product('ACTG', repeat=5))
    for i in range(0, len(perms)):
        perms[i] = ''.join(perms[i])
        filter[perms[i]] = 1
    return(filter)
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
    fp.close()
    return(prox, dist)

def kmercount(seqs, k): #determines the total count of kmers in the sequences
    don = 5 #donor seqeuence
    acc = 10 #acceptor sequence. we're...hardcoding these, I guess. Not a fan.
    total = 0
    decay = 1
    count = {}
    filter = generatefilters() #a dictionary of all the possible legal kmers. reformatting to dictionary drastically cuts down processing time

    for s in seqs:
        for i in range(don, len(s)-k+1-acc):
            kmer = s[i:i+k]
            if kmer in filter: #this is a CPU sink, really big O
                if kmer not in count:
                    count[kmer] = 0
                count[kmer] += decay #to factor in geom decay, to account for intron significance dropping off as it lengthens
                total += decay #pretty sure we want to make the total with the decay as well
                #some sort of decay function goes here...

    return(count, total) #returns a tuple, a dictionary keyed with unique kmers and their counts, and the total number)

def kmerfreqs(counts): #determines frequencies of kmers across an introns
    #print(counts)
    freqs= {}
    for kmer in counts[0]:
        freqs[kmer] = counts[0][kmer] / counts[1]
    return(freqs)

def training(proxfreqs, distalfreqs, xfold): #calculates the log odd probability for our kmerfreqs
    trained = {}
    for kmer in sorted(proxfreqs):
        trained[kmer] = math.log2(proxfreqs[kmer] / distalfreqs[kmer])
    return(trained)

def scoring(prox, distal, trained, k):
    proxscores = []
    distalscores = []
    don = 5
    acc = 10

    for seq in prox:
        score = 0
        for i in range(don, len(seq) -k +1 -acc):
            kmer = seq[i:i+k]
            if kmer in trained:
                score += trained[kmer]
        proxscores.append(score)

    for seq in distal:
        score = 0
        for i in range(don, len(seq) -k +1 -acc):
            kmer = seq[i:i+k]
            if kmer in trained:
                score += trained[kmer]
        distalscores.append(score)

    print(statistics.mean(proxscores))
    print(statistics.mean(distalscores))
    #print(proxscores)
