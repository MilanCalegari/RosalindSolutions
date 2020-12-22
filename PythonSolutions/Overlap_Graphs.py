import sys
from Bio import SeqIO
from itertools import permutations

def overlap(a, b, min_length= 3):
    start = 0

    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

def naive_overlap_map(reads, k):
    olaps = {}
    for a,b in permutations(reads,2):
        olen = overlap(a,b, min_length=k)
        if olen > 0:
            olaps[(a,b)] = olen
    return olaps


def main():
    fasta = sys.argv[1]
    sequences = {}
    for s in SeqIO.parse(open(fasta),'fasta'):
        sequences[str(s.seq)] = s.id


