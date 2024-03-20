from functools import partial
import time

#fonction qui calcule le nième terme de la suite de Fibonacci
def fib(n):
    if (n == 0 or n == 1):
        return n
    return fib(n - 1) + fib(n - 2)



# Affiche les termes de la suite, et indique le temps écoulé
def enumerer(suite):
  t = time.time()
  count = 0
  for term in suite:
    dt = (time.time() - t)*1000
    print (count,":", term, "({temps:.2f} ms)".format(temps=dt))	
    count +=1 

#fonction partie 1
def partie1():
  #calculer les 20 premiers termes de la suite de Fibonacci
  #1.1
  suite = [fib(i) for i in range(20)] # liste en compréhension
  #enumerer(suite)
  #1.2
  suiteG = (fib(i) for i in range(20))
  #afficher les valeurs calculées
  enumerer(suiteG)

 ##Code exécuté --------
partie1()

