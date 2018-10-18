from sympy import *
import matplotlib

f = open("entrada.txt","r")
lista = f.read().split('\n')
f.close()

f = open("saida.txt","w")
for l in lista:
    if("by" in l):
        print(l+"  by")
f.write(str(lista))
f.close()

def Euler(y0, t0, h, nPassos, funct):
    pass

def EulerInverso(y0, t0, h, nPassos, funct):
    pass

def EulerAprimorado(y0, t0, h, nPassos, funct):
    pass

def RungeKutta(y0, t0, h, nPassos, funct):
    pass

def AdamBashforthLista(y, t0, h, nPassos, funct, ordem):
    pass

def AdamBashforthAnt(metodo, t0, h, nPassos, funct):
    pass

def AdamMultonLista(y, t0, h, nPassos, funct, ordem):
    pass

def AdamMultonAnt(metodo, t0, h, nPassos, funct):
    pass
