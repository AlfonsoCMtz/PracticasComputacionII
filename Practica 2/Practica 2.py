import numpy as np
from sympy.abc import x, y
from sympy import *
import time
import math
import matplotlib.pyplot as plt

class NumericalMethods:

    def bisectionMethod(self, a, b, tol, maxIter, func):       

        if (func.subs(x,a) * func.subs(x,b)) < 0:
            print("Existe un cambio de signo")
        else: 
            print("No existen raices reales en el intervalo")
            exit(0) 

        if  a > b:
         print("intervalo mal definido")
         exit(0)

        error = np.inf

        while error > tol:
          c = (a + b) / 2

          Fa = func.subs(x, a)
          Fc = func.subs(x, c)     
          
          
          if (Fc * Fa) < 0:
                b = c
          if (Fc * Fa) > 0:
                a = c
          if Fc == 0:
                break

        return c
class NaiveMethods:

    def NaiveSearch(self, a, b, func):
        
        X = np.linspace(a, b, 5000)
        Y = np.zeros_like(X)
        raizx = []
        raizy = []
        cero = 0
        for i in range(len(X)):
            Y[i] = abs(func.subs(x, X[i]))
            if abs(Y[i]) < 0.5:
                raizx.append(X[i])
                raizy.append(Y[i])
        v = raizy.index(min(raizy))
        raiz = raizx[v]
        return raiz

def main():
    x0 = 0
    maxIter = 90000
    tol = 0.0000000000000000001
    func =(x*3) -(x**2)- 1
    a = -10
    b= 10
    
    ##a=int(input('donde empieza el intervalo'))
    ##b=int(input("donde termina el intervalo"))



    objNM = NumericalMethods()

    print("Metodo de biseccion")
    startbisection = time.time()
    rootbisection = objNM.bisectionMethod(a, b, tol, maxIter, func)
    endbisection = time.time()
    tiempobiseccion = endbisection - startbisection
    print("Raíz:", rootbisection)
    print("Tiempo de biseccion:", tiempobiseccion)

    print("Metodo Busqueda Ingenua")

    
    objN = NaiveMethods()
   
    startnaive = time.time()
    rootnaive = objN.NaiveSearch(a, b, func)
    endnaive = time.time()
    tiemponaive = endnaive - startnaive
    print('raiz', rootnaive)
    print("Tiempo de busqueda ingenua", tiemponaive)


if __name__ == "__main__":
    main()
    main()