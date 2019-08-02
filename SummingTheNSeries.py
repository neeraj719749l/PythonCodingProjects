#link -- https://www.hackerrank.com/challenges/summing-the-n-series/problem

def summingSeries(n):
    return n*n


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        result = summingSeries(i)
    print(result)
