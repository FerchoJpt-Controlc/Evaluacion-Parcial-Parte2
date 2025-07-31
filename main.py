def mcd(a,b):
    if b==0:
        return a
    else:
        return mcd(b,a%b)

def CadenaRepetitiva(palabra,veces):
    if veces==0:
        return palabra
    else:
        print(palabra)
        return CadenaRepetitiva(palabra,veces-1)


def ContarLetra(letra, cadena, indice=0):
    if indice >= len(cadena):
        return 0
    elif cadena[indice] == letra:
        return 1 + ContarLetra(letra, cadena, indice + 1)
    else:
        return ContarLetra(letra, cadena, indice+1)


def DecimalABinario(n):
    if n==0:
        return 0
    else:
        return DecimalABinario(bin(n)[2:])

def CantidadDeDigitos(n,aux=0):
    if aux >= len(n):
        return 0
    else:
        return 1 + CantidadDeDigitos(n, aux+1)

def Menu():
    opcion = 0

    while opcion != 6:
        print("\n-_M E N U_-")
        print("\n1. Calcular MCD")
        print("2. Cadena Repetida N Veces")
        print("3. Cantidad de Letras En una Palabra")
        print("4. Decimal A Binario")
        print("5. Diguitos En Un Numero")
        print("6. SALIR")

        opcion_input = input("\nIngrese su opción: ")
        if opcion_input.isdigit():

            opcion = int(opcion_input)
            if opcion == 1:
                print("\nM C D")

                a=int(input("Ingrese un numero: "))
                b=int(input("Ingrese un numero: "))
                resultado=mcd(a,b)
                print(f"El MCD de {a} y {b} es {resultado}")

            elif opcion == 2:

                print("\nCADENA REPETITA N VECES")

                palabra=input("Ingrese un palabra: ")
                veces=int(input("Ingrese el numero de repeticiones: "))
                CadenaRepetitiva(palabra,veces)


            elif opcion == 3:
                print("\nCANTIDAD DE LETRAS EN UNA PALABRA")

                cadena=input("Ingrese un palabra: ")
                letra=input("Ingrese un letra: ")
                cantidad=ContarLetra(letra,cadena)
                print(f"La letra -{letra}- aparece -{cantidad} veces- en la palabra -{cadena}-")

            elif opcion == 4:
                print("\nCONVERTIR NUMERO DECIMAL A BINARIO")

                n=int(input("Ingrese un numero: "))
                nbinario=DecimalABinario(n)
                print(f"El numero {n} convertido a binario es {nbinario}")

                #m=bin(n)[2:]
                #print(m)

            elif opcion == 5:
                print("\nCALCULAR CUANTOS DIGITOS TIENE UN NUMERO")

                n=input("Ingrese un numero: ")
                digitos=CantidadDeDigitos(n)
                print(f"El  numero {n} tiene {digitos} digitos")

            elif opcion == 6:
                print("ADIOS...ASTA...PRONTO...")
            else:
                print("\nOpción invalida, vuelva a intentar")
        else:
            print("\nError: ingreso de datos no numéricos")
            opcion = 0

        if opcion != 5:
            input("\nPresione ENTER para continuar...")

Menu()