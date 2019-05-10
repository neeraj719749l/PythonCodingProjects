# link -- https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Author -- Rajneesh Sharma

def birthdayCakeCandles(ar):
    maxi = max(arr)
    k = 0
    for i in range(0, len(arr)):
        if maxi == arr[i]:
            k = k + 1
    return k


if __name__ == '__main__':
    ar_count = int(input())
    arr = list(map(int , input().rstrip().split()))
    result = birthdayCakeCandles(arr)
    print(result)