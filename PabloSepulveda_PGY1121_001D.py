from os import system
system ("cls")
nom=100
listaasientosplati=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
listaasientosgold=[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
listaasientossilver=[51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
listacomprados=[]

contadorplat=0
contadorgold=0
contadorsilver=0

platinum=120000
gold=80000
silver=50000

def menu():
    print(""" Que desea realizar
    1.-Comprar entradas
    2.-Mostrar ubicaciones disponibles
    3.-Ver listado de asistentes
    4.-Mostrar ganancias totales
    5.-Salir
    """)   

def calculos():
    print(f"""Los calculos totales son:
    Platinum : Entradas {contadorplat}, por un valor total de : {totalp}
    Gold : Entradas {contadorgold}, por un valor total de : {totalg}
    Silver : Entradas {contadorsilver}, por un valor total de {totals}
    Total recaudado de entradas {totalp+totalg+totals}""")

def asientos():
    print("Estos son los asientos disponibles")
    print(listaasientosplati)
    print("Estos asientos son de la categoria Platinum, y tienen un valor de $120.000 cada uno")
    print(listaasientosgold)
    print("Estos asientos son de la categoria gold, y tienen un valor de $80.000 cada uno")
    print(listaasientossilver)
    print("Estos asientos son de la categoria silver, y tienen un valor de $50.000 cada uno")


while True:
    menu()
    op=input("Ingrese la opción")
    match op:
        case "1":
            while True:
                entradas=int((input("Cuantas entradas desea comprar entre 1 y 3")))
                if entradas > 3:
                    print("El maximo es de 3 entradas y el minimo de 1")
                if entradas < 1:
                    print("Ingrese un numero valido")
                else:
                    print(f"Usted selecciono, {entradas} entradas")
                    break
            asientos()
            for cantidad in entradas:
                numentra=int(input("seleccione el numero de la entrada que desea comprar"))
                if numentra in listaasientosplati:
                    indice=listaasientosplati.index
                    contadorplat+=1
                    while True:
                        rut=int(input("Ingrese su rut, sin digito verificador ni puntos ni guion"))
                        if rut > 99999999:
                            print("Ingrese correctamente el rut nuevamente")
                        else:
                            break
                    listanew=[numentra,rut]
                    listacomprados.append(listanew)
                    if numentra in listaasientosgold:
                        indice=listaasientosgold.index
                        contadorgold+=1
                    if numentra in listaasientossilver:
                        indice=listaasientossilver.index
                        contadorsilver+=1
        case "2":
            pass
        case "3":
            pass
        case "4":
            totalp=contadorplat*platinum
            totalg=contadorgold*gold
            totals=contadorsilver*silver
            calculos()
            pass
        case "5":
            break