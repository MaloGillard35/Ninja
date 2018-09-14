# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def f(n):
    s = 0
    for k in range(1,n+1):
        s = s + k
    return s

def g(n):
    s = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            s = s + 1/(i+j)
            print(f"i = {i} , j = {j}")
    return s

def h(x):
    return x

def eval2(f):
    return f(2)



def rectangle(f,a,b,n):
    s = 0
    t = (b-a)/n
    for k in range(0,n):
        s = s + f(a+k*t)
    return t*s

def carree(x):
    return x**2

# lambda x: x**3
    
def euler(eps):
    s = 0
    k = 1
    while 1/k**2 > eps:
        s = s + 1/k**2
        k = k + 1
    print(f"{k} iterations")
    return s

def pair(n):
    if n%2 == 0:
        return True
    else:
        return False
    
#Pour importer des objets mathématiques : import math
#Pour importer une fonction : from math import sqrt (par exemple pour la 
#fonction racine)
#autre module : sympy (pour avoir exactement les racines, sinus, etc)
    
f = lambda x: (3*x+1)/(2*x+1)
    
def liste1(a,f,n):
    liste = [a]
    for i in range(n):
        liste.append(f(liste[-1])) #le -1 est le dernier élément de la liste (à droite)
    return liste                   #donc en itérant a est pris en premier, puis f(a), puisf(f(a))
    
from math import sqrt  

def estpremier(n):
    if n <= 1:
        print("Pas un entier supérieur ou égal à 2, recommencez.")
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def estpremieralt(n):          #Programme alternatif
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def listepremier(n):
    l = []
    for i in range(2,n):
        if estpremier(i):
            l.append(i)
    return l

def eratosthene(n):           #Version 2, avec moins de tests
    l = [2]                     #Crible d'Eratosthène
    for i in range(3,n,2):
        for k in l:
            if i%k == 0:
                break
            if k**2 > i:
                l.append(i)
                break
    return l


#Pour l'analyse numérique, on utilise le module numpy
# import numpy as np (plus commun dans la communauté scientifique)


def racine(liste):
    newlist = []
    for a in liste:
        newlist.append(math.sqrt(a))
    return newlist

def hilb(n):      #Version (moi) qui ne marche pas
    M= []
    for i in range(1,n+1):
        L = [1/j for j in range(1,n+1)]
        M.append(L)
    return M
    

def hilb2(n):
    L = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(1/(i+j+1))
        L.append(l)
    return np.array(L)

def hilb3(n):
    M = [[1/(i+j+1) for j in range(n)] for i in range(n)]
    return np.array(M)


# x = np.arange(0,9,2) même chose que x = np.array(range(0,9,2))
# x = np.linspace(0,1,5)
    
# import matplotlib.pyplot as plt ===> importe un package pour les graphiques

# x = np.linspace(0,1,100)
# x**2
# plt.plot(x,x**2)
# plt.plot(x,x**2,x,x**3)
# %matplotlib permet d'ouvrir une fenêtre pour le dessin et d'y mettre plusieurs courbes

# xx = np.linspace(0,1,5)
# plt.plot(x,x**2,xx,xx**3)


def dessin():
    for i in range(1,10):
        plt.plot(x,x**i,label = f'y = x**(i)')
    plt.title("Un beau dessin") # Pour mettre un titre au dessin/graphique
    plt.xlabel("abscisse") # Pour donner un nom à l'axe des x
    plt.ylabel("ordonnée") # Pour donner un nom à l'axe des y
    plt.legend() # Met une légende pour chaque courbe

def dessin2():
    plt.plot(x,x**2,label='x**2')
    plt.plot(x,x**3,label='x**3')
    plt.legend() 


# x = np.random.rand(2,3) 
# x = np.random.normal(200,25, size=100) 
# plt.hist(x,25) ===> trace un histogramme

# x = np.random.rand(100)
# y = np.random.rand(100)
# plt.scatter(x,y) ===> trace un nuage de point
    

