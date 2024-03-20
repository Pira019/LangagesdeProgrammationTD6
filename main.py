from functools import partial
import time

#fonction qui calcule le nième terme de la suite de Fibonacci
def fib(n):
    if (n == 0 or n == 1):
        return n
    return fib(n - 1) + fib(n - 2)


#générateur infini 1.4
def fibGen(): #génère la suite de fibonacci au complet (générateur infini...)
    i=0
    while(True):             
        yield fib(i)
        i +=1
"""
gen = fibGen()
 
print(next(gen))   
print(next(gen))   
print(next(gen))   
"""