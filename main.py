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

#2.3
def memo(f):
	cache = {}
	def fcache(*t):
		if(t in cache):
			#print ("valeur cachee:", str(t))
			return cache[t]
		
		cache[t]=f(*t)
		#print ("insert in cache:", str(t))
		return cache[t]
	return fcache

# Affiche les termes de la suite, et indique le temps écoulé
def enumerer(suite):
  t = time.time()
  count = 0
  for term in suite:
    dt = (time.time() - t)*1000
    print (count,":", term, "({temps:.2f} ms)".format(temps=dt))	
    count +=1

#fonction qui calcule le nième terme de la suite de Fibonacci
#@trace 
@memo
def fib(n):
    if (n == 0 or n == 1):
        return n
    return fib(n - 1) + fib(n - 2)

#fib(8)
#memo(trace(fib(2)))

#fonction partie 1
def partie1():
  #calculer les 20 premiers termes de la suite de Fibonacci
  #1.1
  suite = [fib(i) for i in range(20)]
  #afficher les valeurs calculées
  enumerer(suite)
##Code exécuté --------
partie1()