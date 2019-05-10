#link -- https://www.hackerrank.com/challenges/mini-max-sum/problem
#Author -- Rajneesh Sharma

def miniMaxSum(arr):
    maxi = max(arr)
    mini = min(arr)
    print(sum(arr) - maxi, sum(arr) - mini)



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)