from sympy import *
import matplotlib


def Euler(y0,t0,h,nPassos,funct):
    sfunct = sympify(funct)

def EulerInverso(y0,t0,h,nPassos,funct):
    sfunct = sympify(funct)

def EulerAprimorado(y0,t0,h,nPassos,funct):
    sfunct = sympify(funct)

def RungeKutta(y0,t0,h,nPassos,funct):
    sfunct = sympify(funct)

def AdamBashforthLista(y,t0,h,nPassos,funct,ordem):
    sfunct = sympify(funct)

def AdamBashforthAnt(metodo,y0,t0,h,nPassos,funct,ordem):
    sfunct = sympify(funct)

def AdamMultonLista(y,t0,h,nPassos,funct,ordem):
    sfunct = sympify(funct)

def AdamMultonAnt(metodo,y0,t0,h,nPassos,funct,ordem):
    sfunct = sympify(funct)

def FormulaInversaLista(y,t0,h,nPassos,funct,ordem):
    sfunct = sympify(funct)

def FormulaInversaAnt(metodo,y0,t0,h,nPassos,funct,ordem):
    sfunct = sympify(funct)


f = open("entrada.txt","r")
lista = f.read().split('\n')
f.close()

f = open("saida.txt","w")
for l in lista:
    args = l.split(" ")
    if("by" in args[0]):
        args[0] = args[0].split("_by_")
        if(args[0][0] == "formula_inversa" ):
            FormulaInversaAnt(args[0][1],args[1],args[2],args[3],args[4],args[5],args[6])
        elif(args[0][0] == "adam_multon" ):
            AdamMultonAnt(args[0][1],args[1],args[2],args[3],args[4],args[5],args[6])
        elif(args[0][0] == "adam_bashforth" ):
            AdamBashforthAnt(args[0][1],args[1],args[2],args[3],args[4],args[5],args[6])
    elif(args[0] == "formula_inversa" ):
        FormulaInversaLista(args[1:(len(args)-5)],args[len(args)-5],args[len(args)-4],args[len(args)-3],args[len(args)-2],args[len(args)-1])
    elif(args[0] == "adam_multon" ):
        AdamMultonLista(args[1:(len(args)-5)],args[len(args)-5],args[len(args)-4],args[len(args)-3],args[len(args)-2],args[len(args)-1])
    elif(args[0] == "adam_bashforth" ):
        AdamBashforthLista(args[1:(len(args)-5)],args[len(args)-5],args[len(args)-4],args[len(args)-3],args[len(args)-2],args[len(args)-1])
    elif(args[0] == "runge_kutta"):
        RungeKutta(args[1],args[2],args[3],args[4],args[5])
    elif(args[0] == "euler_aprimorado"):
        EulerAprimorado(args[1],args[2],args[3],args[4],args[5])
    elif(args[0] == "euler_inverso"):
        EulerInverso(args[1],args[2],args[3],args[4],args[5])
    elif(args[0] == "euler"):
        Euler(args[1],args[2],args[3],args[4],args[5])
    else:
        continue
f.close()
