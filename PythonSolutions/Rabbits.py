#!/usr/bin/python3
from fuctions import lru_cache
## optimization time

#The calculation of number of rabbits is equals Fn = Fn-1 + (Fn-2 * k)

# def recursion_naive(n, k):
#     if n <= 1:
#         return n
#     else:
#         return recursion_naive(n-1,k) + (int(recursion_naive(n-2,k))*k)

# def recursion_fast(n, k, computed={1:1, 2:1}):
#         if n not in computed:
#             computed[n] = recursion_fast(n-1, k) + (int(recursion_fast(n-2, k))*k)
#             return computed[n]
#         else:
#             return computed[n]


def fib(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1, m) + fib(n-2, m)*m


def main():
    n,k = input().split()
    #print(recursion_naive(int(n),int(k)))
    print(recursion_fast(int(n), int(k)))

if __name__ == '__main__':
    main()
