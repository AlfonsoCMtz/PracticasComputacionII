

import numpy as np
import sympy

class GaussJordan:
    
    # Constructor
    #def init(self, filas, cols, M):
        #self.f = filas
        #self.c = cols
        #self.M = M


    def intercambiarFilas(self, index1, index2, M):
        #print("A intercambiar", index1, " por ", index2)
        #print("Antes \n", M)
        for i in range(len(M[0])): # itera sobre el número de columnas
            tmp = M[index2][i]
            M[index2][i] = M[index1][i]
            M[index1][i] = tmp
        #print("Después:\n", M)
        return M

    
    def multiplicarFila(self, k, fila, colInicial, M):
        for i in range (colInicial, len(M[0])):
            M[fila][i] = k * M[fila][i]
        return M

    def restarFilas(self, f1, f2, colInicial, M):
        for i in range(colInicial, len(M[0])):
            M[f1][i] =  M[f2][i] - M[f1][i]
        return M 

    def buscarPivote(self, filas, col, M):
        indiceFila = -1
        maxNum = np.inf *-1
        for i in range(col+1, filas):
            if(M[i][col] > maxNum and M[i][col] != 0):
                indiceFila = i
                maxNum = M[i][col]
        return indiceFila

    def eliminicacionGaussiana(self, f, c, M):
        # Definición de variables
        indicePiv = -1
        
        for i in range(f):
            pivote = M[i][i]
            if pivote == 0:
                indicePiv = self.buscarPivote(f, i, M) # Se implementa pivoteo parcial
                #TODO: Implementar pivoteo completo
                if indicePiv == -1:
                    print("El sistema no tiene solución")
                    exit(0)
                else:
                    M = self.intercambiarFilas(indicePiv, i, M)
                    pivote = M[i][i]
            
            for j in range(i+1, f): # Realizar la eliminación de los elementos debajo del pivote
                if M[j][i] != 0:
                    k = pivote / M[j][i]    # Multiplicador para la eliminación
                    M = self.multiplicarFila(k, j, i, M)
                    M = self.restarFilas(j, i, i, M)
        print("Matriz resultante: \n", M)




def main():

    # Definición de número de filas y columnas
    f = 3
    c = f+1 # +1 se debe a la columna de resultados
    
    # Inicializar una matriz de 
    M = np.random.randint(10, size = (f,c))

    print("matrix aleatoria:\n", M)
    
    # Creación de un objeto
    objG = GaussJordan()
    print("Realizando eliminación Gaussiana...")
    objG.eliminicacionGaussiana(f, c, M) 


if __name__ == "__main__":
    main()
