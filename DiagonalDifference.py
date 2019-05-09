#link -- https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Author -- Rajneesh Sharma

import math

def diagonalDifference(arr):
    k = len(arr)
    print(k)
    d1 = 0
    d2 = 0
    for i in range(0, k):
        d1 = d1 + arr[i].__getitem__(i)
        d2 = d2 + arr[i].__getitem__(k-i-1)
    return int(math.fabs(d1 - d2))

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(0, n):
        arr.append(list(map(int, input().rstrip().split())))
    print(arr)
    result = diagonalDifference(arr)
    print(result)
