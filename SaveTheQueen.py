#link - https://www.hackerrank.com/contests/hourrank-31/challenges/save-the-queen
#Author - Rajneesh Sharma

def avg(a, b):
   return (sum(a)+b)/len(a)

def solve(n, a):
    a = sorted(a, reverse = True)
    on, off = a[0:n], sum(a[n:])
    while on and avg(on, off) < max(on) : on.pop(0)
    print(avg(on, off))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    a = list(map(int, input().rstrip().split()))
    solve(n, a)