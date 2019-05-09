#link -- https://www.hackerrank.com/challenges/staircase/problem
#Author -- Rajneesh Sharma

def staircase(n):
    for i in range(0, n-1):
        print(' ' * (n-i-2), "#" * (i+1))
    print("#"*n)


if __name__ == '__main__':
    n = int(input())
    staircase(n)