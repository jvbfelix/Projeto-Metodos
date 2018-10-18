from sympy import *
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def Euler(y0,t0,h,nPassos,funct):
    sfunct = sympify(funct)
    y0 = float(y0)
    t0 = float(t0)
    h = float(h)
    nPassos = int(nPassos)
    y = []
    t = []
    y.append(y0)
    t.append(t0)
    yAt = y0
    tAt = t0
    for n in range(1, nPassos+1):
        yAt += h*sfunct.subs([("y", yAt), ("t", tAt)])
        tAt += h
        y.append(yAt)
        t.append(tAt)

    return [y,t]

def EulerInverso(y0,t0,h,nPassos,funct):
    sfunct = sympify(funct)
    y0 = float(y0)
    t0 = float(t0)
    h = float(h)
    nPassos = int(nPassos)
    y = []
    t = []
    y.append(y0)
    t.append(t0)
    yAt = y0
    tAt = t0

    for n in range(0, nPassos):
        yAt = y[n] + h*sfunct.subs([("y", y[n]), ("t", t[n])])
        tAt = (t[n]+h)
        y.append(y[n] + h*sfunct.subs([("y", yAt), ("t", tAt)]))
        t.append(tAt)
    return [y,t]

def EulerAprimorado(y0,t0,h,nPassos,funct):
    sfunct = sympify(funct)
    y0 = float(y0)
    t0 = float(t0)
    h = float(h)
    nPassos = int(nPassos)
    y = []
    t = []
    y.append(y0)
    t.append(t0)
    yAt = y0
    tAt = t0

    for n in range(1, nPassos+1):
        Fn = sfunct.subs([("y", yAt), ("t", tAt)])
        proxy = yAt+(h*Fn)
        tAt += h
        diff = (Fn + sfunct.subs([("y", proxy), ("t", tAt)]))/2
        yAt += h*diff
        y.append(yAt)
        t.append(tAt)

    return [y,t]

def RungeKutta(y0,t0,h,nPassos,funct):
    sfunct = sympify(funct)
    y0 = float(y0)
    t0 = float(t0)
    h = float(h)
    nPassos = int(nPassos)
    y = []
    t = []
    y.append(y0)
    t.append(t0)
    yAt = y0
    tAt = t0

    for n in range(1, nPassos+1):
        k1 = sfunct.subs([("y", yAt), ("t", tAt)])
        k2 = sfunct.subs([("y", yAt + (0.5 * h * k1)), ("t", tAt + (0.5 * h))])
        k3 = sfunct.subs([("y", yAt + (0.5 * h * k2)), ("t", tAt + (0.5 * h))])
        k4 = sfunct.subs([("y", yAt + (h * k3)), ("t", tAt+h)])
        yAt = yAt + (h * ((k1 + (2 * k2) + (2 * k3) + k4)/6))
        tAt = tAt+h
        y.append(yAt)
        t.append(tAt)
    return [y,t]

def AdamBashforthLista(y,t0,h,nPassos,funct,ordem):
    sfunct = sympify(funct)
    t0 = float(t0)
    h = float(h)
    nPassos = int(nPassos)
    ordem = int(ordem)
    t = []
    ysub = []
    for n in y:
        ysub.append(float(n))
    y = ysub
    ysub = []
    t.append(t0)
    tAt = t0
    # for g in range(0,len(y)):
    #     ysub.append(sfunct.subs([("y", y[g]), ("t", tAt)]))
    #     tAt += tAt + h
    # tAt = t0
    # yfin = []
    # for i in range (ordem-2 , nPassos-1):
    #     #receives F calculated in created function
    #
    #     tAt = tAt + h
    #
    #
    #     #enter values in graph
    #     yfin.append(ysub[i] + calBashCof(h, i,ysub, ordem))
    #     t.append(tAt)
    #
    # print(yfin)

def calBashCof(h,i,lista,g):
    if(g==2):
        return (h/2)*(3*lista[i]-lista[i-1])
    elif(g==3):
        return ((h/12)*(23*lista[i-0]-16*lista[i-1]+5*lista[i-3]))
    elif(g==4):
        return ((h/24)*(55*lista[i-0]-59*lista[i-1]+37*lista[i-2]-9*lista[i-3]))
    elif(g==5):
        return ((h/720)*(1901*lista[i-0]-2774*lista[i-1]+2616*lista[i-2]-1274*lista[i-3]+251*lista[i-4]))
    elif(g==6):
        return (h/1440)*(4277*lista[i-0]-7923*lista[i-1]+9982*lista[i-2]-7298*lista[i-3]+2877*lista[i-4]-475*lista[i-5])

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
cc = 0
for l in lista:
    cc += 1
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
        result = RungeKutta(args[1],args[2],args[3],args[4],args[5])
        resulty = result[0]
        resultt = result[1]
        f.write("\nMetodo de Runge-Kutta\n")
        f.write(f"y({args[1]})={args[2]}\n")
        f.write(f"h={args[3]}\n")
        for x in range(0,int(args[4])+1):
            f.write(str(x)+" "+str(resulty[x])+"\n")

        plt.clf()
        plt.title(str(cc)+": Metodo de Runge-Kutta")
        plt.xlabel("t")
        plt.ylabel("y")
        plt.plot(resultt, resulty, 'go')
        plt.plot(resultt, resulty, 'k:', color='blue')
        plt.savefig(str(cc)+'.png')
    elif(args[0] == "euler_aprimorado"):
        result = EulerAprimorado(args[1],args[2],args[3],args[4],args[5])
        resulty = result[0]
        resultt = result[1]
        f.write("\nMetodo de Euler Aprimorado\n")
        f.write(f"y({args[1]})={args[2]}\n")
        f.write(f"h={args[3]}\n")
        for x in range(0,int(args[4])+1):
            f.write(str(x)+" "+str(resulty[x])+"\n")

        plt.clf()
        plt.title(str(cc)+": Metodo de Euler Aprimorado")
        plt.xlabel("t")
        plt.ylabel("y")
        plt.plot(resultt, resulty, 'go')
        plt.plot(resultt, resulty, 'k:', color='blue')
        plt.savefig(str(cc)+'.png')
    elif(args[0] == "euler_inverso"):
        result = EulerInverso(args[1],args[2],args[3],args[4],args[5])
        resulty = result[0]
        resultt = result[1]
        f.write("\nMetodo de Euler Inverso\n")
        f.write(f"y({args[1]})={args[2]}\n")
        f.write(f"h={args[3]}\n")
        for x in range(0,int(args[4])+1):
            f.write(str(x)+" "+str(resulty[x])+"\n")

        plt.clf()
        plt.title(str(cc)+": Euler")
        plt.xlabel("t")
        plt.ylabel("y")
        plt.plot(resultt, resulty, 'go')
        plt.plot(resultt, resulty, 'k:', color='blue')
        plt.savefig(str(cc)+'.png')
    elif(args[0] == "euler"):
        result = Euler(args[1],args[2],args[3],args[4],args[5])
        resulty = result[0]
        resultt = result[1]
        f.write("\nMetodo de Euler\n")
        f.write(f"y({args[1]})={args[2]}\n")
        f.write(f"h={args[3]}\n")
        for x in range(0,int(args[4])+1):
            f.write(str(x)+" "+str(resulty[x])+"\n")

        plt.clf()
        plt.title(str(cc)+": Euler")
        plt.xlabel("t")
        plt.ylabel("y")
        plt.plot(resultt, resulty, 'go')
        plt.plot(resultt, resulty, 'k:', color='blue')
        plt.savefig(str(cc)+'.png')
    else:
        continue

f.close()
