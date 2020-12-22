
def probrability(k, m, n):
    N = k + m + n #population size
    rr = (n/N) * ((n-1)/(N-1))   #probability of aa x aa
    hh = (m/N) * ((m-1)/(N-1)) #probability of Aa x Aa
    hr = (m/N) * (n/(N-1)) + (n/N) * (m/(N-1))#probability of Aa x aa and aa x Aa

    return  ( 1 - (rr + hh/4 + hr/2))  # 1 - rececive probability = Dominant probrability




def main():
    k, m, n = input().split() #k = AA; m= Aa; n=aa
    print(probrability(int(k), int(m), int(n)))

if __name__ == '__main__':
    main()
