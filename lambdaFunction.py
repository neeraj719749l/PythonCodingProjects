import numpy as np

if __name__ == '__main__':
    li = [1, 2, 3,4]
    p = list(filter(lambda x:(x%2==0), li))
    print(p)

    k = lambda x:x*x*x
    print(k(7))

    n = np.arange(0, 30)
    p1 = list(map(lambda x: x * x, n))
    p1

    