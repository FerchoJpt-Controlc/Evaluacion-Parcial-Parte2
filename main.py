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

                a=int(input("\nIngrese un numero: "))
                b=int(input("Ingrese un numero: "))
                resultado=mcd(a,b)
                print(f"\nEl MCD de {a} y {b} es {resultado}")

            elif opcion == 2:

                print("\nCADENA REPETITA N VECES")

                palabra=input("\nIngrese un palabra: ")
                veces=int(input("Ingrese el numero de repeticiones: "))
                CadenaRepetitiva(palabra,veces)


            elif opcion == 3:
                print()
            elif opcion == 4:
                print()
            elif opcion == 5:
                print()
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