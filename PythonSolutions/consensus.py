from Bio import SeqIO

def consensus_matrix(seq):
    matrix = [ ]

    for i in range(len(seq[0])):
        correlance = {'A':0, 'C':0, 'G':0, 'T':0}
        for j in range(len(seq)):
            correlance[seq[j][i]] += 1
        matrix.append(list(correlance.values()))

    return matrix
def consensus_sequence(matrix):
    correlance = {0:'A', 1:'C', 2:'G', 3:'T'}
    
    sequence = []
    for row in matrix:
        for i in range(len(row)):
            if row[i] == max(row):
                sequence.append(correlance[i])
                break
    return ''.join(sequence)

def matrix_l2r(matrix):
    line_A = ['A:']
    line_C = ['C:']
    line_G = ['G:']
    line_T = ['T:']

    for i in range(len(matrix)):
        line_A.append(str(matrix[i][0]))
        line_C.append(str(matrix[i][1]))
        line_G.append(str(matrix[i][2]))
        line_T.append(str(matrix[i][3]))

    line_A.append('\n')
    line_C.append('\n')
    line_G.append('\n')

    final = ' '.join(line_A) + ' '.join(line_C) + ' '.join(line_G) + ' '.join(line_T)

    return final
	


f = input()
fasta = SeqIO.parse(open(f),"fasta")
sequences = [str(i.seq) for i in fasta]

matrix = consensus_matrix(sequences)

print(consensus_sequence(matrix))
print(matrix_l2r(matrix))


