from functools import partial
import time

def traceur(f):
	def ftracee(*args):
		print("appel de "+f.__name__+" avec arguments:"+str(args))
		return f(*args)
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
@trace # on peut garder les 2 annotations, ou en enlever
@memo
def fib(n):
	if (n==0 or n==1):
		return n	 
	return fib(n-1)+fib(n-2)


# Affiche les termes de la suite, et indique le temps écoulé
def enumerer(suite):
  t = time.time()
  count = 0
  for term in suite:
    dt = (time.time() - t)*1000
    print (count,":", term, "({temps:.2f} ms)".format(temps=dt))	
    count +=1


#générateur infini 1.4
def fibGen(): #génère la suite de fibonacci au complet (générateur infini...)
	i=0
	while(True):
		yield fib(i)
		i +=1

#enumération limitée à 10 ms (Q1.5)
def enumerer2(suite):
	count = 0
	for term in suite:
		count +=1
		dt = (time.time() - t)*1000
		print (count, term, "({temps:.2f} ms)".format(temps=dt))	
		if (dt>10):
			break


#fonction partie 1
def partie1():
  #calculer les 20 premiers termes de la suite de Fibonacci
  #1.1
  suite = [fib(i) for i in range(20)]
  #1.2
  suiteG = (fib(i) for i in range(20))

  #1.3 
  suiteMap = map(fib, range(20))
  #=>map est un générateur


  #afficher les valeurs calculées
  enumerer(suite)

#fonction pour partie 2
def partie2():
  print("fib(4)", fib(4))
  # pour évaluer le nombre de termes, utiliser le générateur infini et énumérer2 (enlever le traçage)

##Code exécuté --------
partie2()


