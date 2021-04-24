
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        fib = fibonacci(n-1)+fibonacci(n-2)
        return fib
    elif n < 0:
        fib = fibonacci(n+2)-fibonacci(n+1)
        return fib

if __name__ == '__main__':

    print('0', fibonacci(0))
    print('1', fibonacci(1))
    print('2', fibonacci(2))
    print('3', fibonacci(3))
    print('4', fibonacci(4))
    print('5', fibonacci(5))
    print('6', fibonacci(6))
    print('-7', fibonacci(-7))
    print('-8', fibonacci(-8))
