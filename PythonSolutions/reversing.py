#!/usr/bin/python3

def reverse(sequence):
    rev = {'A':'T','T':'A','C':'G','G':'C'}
    rev_seq = []
    for i in sequence:
        rev_seq.append(rev[i])
    rev_seq = ''.join(rev_seq)[::-1]

    return rev_seq
    

def main():
    sequence = input()
    print(reverse(sequence))

if __name__ == '__main__':
    main()
