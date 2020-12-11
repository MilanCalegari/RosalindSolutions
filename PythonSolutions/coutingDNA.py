from collections import Counter

sequence = input()
counter = Counter(sequence)


print('%s %s %s %s'%(counter['A'],counter['C'],counter['G'],counter['T']))
