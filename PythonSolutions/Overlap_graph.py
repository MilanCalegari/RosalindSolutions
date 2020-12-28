from Bio import SeqIO
from itertools import permutations

def Overlap(sequences,k):
	overlaps = []
	for a,b in permutations(sequences,2):

		if a[-k:] == b[:k]:
			overlaps.append([a,b])

	return overlaps

def main():
	sequence = {}
	fasta = SeqIO.parse(open(input('insert fasta file: ')),'fasta')
	for i in fasta:
		sequence[str(i.seq)] = i.id

	overlaps = Overlap(list(sequence.keys()),3)


	for a,b in overlaps:
		print(sequence[a],sequence[b])
			


if __name__ == '__main__':
	main() 