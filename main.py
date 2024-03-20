from functools import partial
import time

#décorateur pour tracer les appels de fonction (utilisé dans la deuxième partie du TD)
def trace(f):
  def ftracee(*args): # la syntaxe * permet de représenter plusieurs arguments par un tuple
    print("appel de "+f.__name__+" avec arguments:"+str(args))
    t1 = time.time()
    v = f(*args)
    t2 = time.time()
    dt = (t2-t1)*1000
    print("fin appel {ff:s}({aa:s}) t= {tt:.2f} ms".format(ff=f.__name__, aa=str(args), tt=dt))
    return v
  return ftracee

#fonction qui calcule le nième terme de la suite de Fibonacci
@trace 
def fib(n):
    if (n == 0 or n == 1):
        return n
    return fib(n - 1) + fib(n - 2)

fib(2)