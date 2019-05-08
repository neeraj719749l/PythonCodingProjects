# link - https://www.hackerrank.com/contests/hourrank-31/challenges/hanging-posters/problem
# Author - Rajneesh Sharma

import math

def solve(h, wallPoints, lengths):
    length = [(wallPoints[i] - (lengths[i]/4) - h) for i in range(0, len(wallPoints))]
    length = [math.ceil(length[i]) for i in range(0, len(length))]
    if max(length) <= 0:
        return 0
    else:
        return max(length)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    h = int(first_multiple_input[1])
    wallpoints = list(map(int, input().rstrip().split()))
    lengths = list(map(int, input().rstrip().split()))
    print(solve(h, wallpoints, lengths))
