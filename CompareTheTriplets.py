# link -- https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Author -- Rajneesh Sharma

def compareTriplets(a, b):
    alice = []
    bob = []
    for i in range(0, 3):
        if a[i] > b[i]:
            alice.append(1)
        elif a[i] < b[i]:
            bob.append(1)
    result = [sum(alice), sum(bob)]
    return result

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
