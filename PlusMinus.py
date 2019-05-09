# link -- https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Author -- Rajneesh Sharma

def plusMinus(arr):
    k = len(arr)
    n, p, z = 0, 0, 0
    for i in range(0, k):
        if arr[i] < 0:
            n = n + 1
        elif arr[i] > 0:
            p = p + 1
        else:
            z = z + 1
    print(p/k)
    print(n/k)
    print(z/k)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    print(a)
    plusMinus(a)
