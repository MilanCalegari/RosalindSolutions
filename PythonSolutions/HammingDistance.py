
def Hamming(s1, s2):
    HD = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            HD += 1
    return HD


def main():
    s1 = input()
    s2 = input()
    print(Hamming(s1,s2))


if __name__ == '__main__':
    main()
