# link -- https://www.hackerrank.com/challenges/a-very-big-sum/problem?h_r=next-challenge&h_v=zen
# Author -- Rajneesh Sharma

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(result)