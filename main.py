from functools import partial
import time

#fonction qui calcule le nième terme de la suite de Fibonacci
def fib(n):
    if (n == 0 or n == 1):
        return n
    return fib(n - 1) + fib(n - 2)


def partie2():
  print("fib(4)", fib(5))

  ##Code exécuté --------
partie2()