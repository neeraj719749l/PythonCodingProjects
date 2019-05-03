def rever(number):
    j = 0
    rev = 0
    temp = number
    while temp != 0:
        temp = int(temp/10)
        j = j + 1
    temp1 = number
    while temp1 != 0:
        x = temp1%10
        j = j - 1
        rev = rev + (x*pow(10, j))
        temp1 = int(temp1/10)
    return rev

def intake():
    n = input("please enter the number of inputs\n")
    n = int(n)
    if n <= 0:
        print("invalid input..\n")
        n = intake()
    return n

if __name__ == '__main__':
   n = intake()
   while n != 0:
       k = input("please enter the input\n")
       k = int(k)
       if k < 0:
           print("invalid input..\n")
           n = n
       else:
           print(rever(k))
           n = n - 1






