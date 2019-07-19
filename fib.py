___author___ = 'Kash Farhadi"

''' fib.py
    Provides n-th number in the Fibonacci sequence.
'''

def fib(n) :

    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1);
            a, b = b, a+b
        return b
