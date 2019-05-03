# to reverse a string.
# to make the code unbreakable.

def rever(str):
    s1 = ''
    for c in str:
        s1 = c + s1
    return s1


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
        string = input("Enter the string\n")
        n = n - 1
        print(rever(string))


