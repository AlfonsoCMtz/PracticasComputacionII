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
    
    
    def newtonMethod(self, tol, maxIter, x0, func):
        root = np.inf
        # Calcular derivada de la función original
        firstDer = diff(func, x)

        # Inicializar error e iteraciones
        error = np.inf
        iter =0


        while(error >tol and iter < maxIter):

            # TODO: Validación de división entre 0

            X1 = x0 - (func.subs(x, x0)/ firstDer.subs(x,x0))

            # TODO: calcular error

            x0 = X1 

            iter += 1
        
        # TODO: Evaluar cual de las dos condiciones se dejó de cumplir
        # Si se dejó de cumplir la primer condición enotnces root = X1
        return root


    def secantMethod(self, tol, maxIter,  x0, func):
            
            root = np.inf
            x_1=0
            # Inicializar error e iteraciones
            error = np.inf
            iter =0

            while(error > tol and iter < maxIter):
                fx0 = func.subs(x, x0)
                x_1 = x0 - ( (fx0  * (x0 - x_1)) / (fx0 - func.subs(x, x_1)))

                x_1 = x0
                x0 = x_1
                iter += 1
            
            root = x0
            return root


    def brentDekkerMethod(self, a, b, tol, maxIter, func):
        root = np.inf
        error = np.inf
        iter = 0

        if func.subs(x, a) * func.subs(x, b) >= 0:
            print("No existe una raíz en el intervalo proporcionado...")
            exit(0)
        # Validar valores
        if abs(func.subs(x, a)) < (func.subs(x, b)):
            # Cambiar los valores de a por b y viceversa
            a,b = b,a
            
        
        c = a
        while( error > tol and iter < maxIter):
            if (func.subs(x, a) != func.subs(x, c)) and (func.subs(x, b) != func.subs(x, c)):
                s = ((a*func.subs(x, b) * func.subs(x, c)) / (((func.subs(x, a) - func.subs(x, b))) *(func.subs(x, a) - func.subs(x, c))) + 
                ( ((b*func.subs(x, a) * func.subs(x, c)) / (((func.subs(x, b) - func.subs(x, a))) * (func.subs(x, b)) - func.subs(x, c)))) + 
                (((c*func.subs(x, a) * func.subs(x, b)) / (((func.subs(x, c) - func.subs(x, a))) * (func.subs(x, c)) - func.subs(x, b)))))
            else: 

                # Método de la secante
                s = b - (func.subs(x, b)) * ((b-a) / (func.subs(x, b) - func.subs(x, a))) 
            
        root=s    
        return root            



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
    func = x**3-1*x-1
    a = -10
    b= 10
    
    ##a=int(input('donde empieza el intervalo'))
    ##b=int(input("donde termina el intervalo"))



    objNM = NumericalMethods()


    startbisection = time.time()
    rootbisection = objNM.bisectionMethod(a, b, tol, maxIter, func)
    endbisection = time.time()
    tiempobiseccion = endbisection - startbisection
    print("Raíz:\n", rootbisection) 
    print("Tiempo de biseccion:\n", tiempobiseccion)


    startnewton = time.time()
    rootNewton = objNM.newtonMethod(tol, maxIter, x0, func)
    endnewton = time.time()
    tiemponewton = endnewton - startnewton
    print("Tiempo de newton:\n", tiemponewton)

    startsec = time.time()
    rootsec = objNM.secantMethod(tol, maxIter,   x0, func)
    endsec = time.time()
    tiemposec = endsec - startsec
    print("Tiempo de secante :\n", tiemposec)



    startbrent = time.time()
    endbrent= time.time()
    tiempobrent = endbrent - startbrent   
    print("Tiempo de brent :\n", tiempobrent)


    
    objN = NaiveMethods()
   
    startnaive = time.time()
    rootnaive = objN.NaiveSearch(a, b, func)
    endnaive = time.time()
    tiemponaive = endnaive - startnaive
    print("Tiempo de busqueda ingenua\n", tiemponaive)


if __name__ == "__main__":
    main()