#link -- https://www.hackerrank.com/challenges/sherlock-and-moving-tiles/problem?

import math

#
# Complete the movingTiles function below.
#
def movingTiles(l, s1, s2, queries):
    result = []
    for i in queries:
        k = (l-math.sqrt(i))/(math.sqrt(abs(s2-s1)/2))
        result.append(k)
    return result

if __name__ == '__main__':

    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    print(result)
