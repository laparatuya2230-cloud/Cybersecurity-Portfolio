# ==========================================
# Proyecto: CryptoCesar Pro
# Autor: Luis Mario
#Descripcion: este es un programa de encriptacion
#Aplicacion de consola para cifrar y decifrar
#mensaje usando el algoritmo Cifrado de cesar.
# ===========================================

historial = []
contador_operaciones = 0 



def mostrar_menu():
    print("\n===== CRYPTOCESAR PRO =====")
    print("1. CIFRAR MENSAJE")
    print("2. DECIFRAR MENSAJE")
    print("3. VER HISTORIAL")
    print("4. VER CONTADOR DE OPERACIONES")
    print("5. EXPORTAR HISTORIAL A TXT")
    print("6. SALIR")


def solicitar_clave():
    while True:
        clave = input("Digite la clave numerica: ").strip()

        if clave.isdigit():
            return int(clave)
        else:
            print("Error: debe digitar una clave numerica.")


def cifrar_cesar(texto, clave):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():

            if caracter.isupper():
                codigo_base = 65
            else:
                codigo_base = 97

            
            nuevo_codigo  = ord(caracter) - codigo_base
            nuevo_codigo = (nuevo_codigo + clave) % 26
            resultado += chr(nuevo_codigo + codigo_base)

        else:
            resultado += caracter

    return resultado

def decifrar_cesar(texto, clave):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():

            if caracter.isupper():
                codigo_base = 65
            else:
                codigo_base = 97


            nuevo_codigo = ord(caracter) - codigo_base
            nuevo_codigo = (nuevo_codigo - clave) % 26
            resultado += chr(nuevo_codigo + codigo_base)

        else:
            resultado += caracter

    return resultado

def guardar_historial(operacion, mensaje_original, clave, resultado):
    historial.append({
        "operacion": operacion,
        "mensaje_original": mensaje_original,
        "clave": clave,
        "resultado": resultado
    })



def mostrar_historial():
    if len(historial) == 0:
        print("\nNo hay operaciones guardadas en el historial.")
    else:
        print("\n ===== HISTORIAL DE OPERACIONES =====")

        for indice, registro in enumerate(historial, start=1):
            print(f"\nOperacion #{indice}")
            print (f"Tipo: {registro['operacio']}")
            print(f"Mensaje original: {registro['mensaje_origina']}")
            print(f"clave: {registro['clave ']}")
            print(f"Resultado: {registro ['resultado']}")


def exportar_historial():
    if len(historial) == 0:
        print("\n No hay historial para exportar.")
        return
    

    archivo = open("historial_crypto_cesar.txt", "w", encoding="utf-8")


    archivo.write("===== HISTORIAL CRYPTOCESAR PRO =====\n")


    for indice, registro in enumerate(historial, start=1):
        archivo.write(f"\nOperacion #{indice}\n")
        archivo.write(f"Tipo: {registro ['operacion']}\n")
        archivo.write(f"Mensaje original: {registro['mensaje_original']}\n")
        archivo.write(f"clave: {registro ['clave']}\n")
        archivo.write(f"Resultado: {registro['resultado']}\n")

    archivo.close()

    print("\n HIstorial exportado correctamente en el archivo:")
    print("historial_crypto_cesar.txt")



def ejecutar_cifrado():
    global contador_operaciones

    mensaje = input("Digite el mensaje que desea cifrar:")
    clave = solicitar_clave()


    resultado = cifrar_cesar(mensaje, clave)


    print("\nMnesaje cifrado:")
    print(resultado)


    guardar_historial("cifrado", mensaje,clave,resultado)
    contador_operaciones += 1 

def mostrar_contador():
    print(f"\nCantidad de operaciones realizadas: {contador_operaciones}")


def principal():
    while True:
        mostrar_menu()


        opcion = input("selecione una opcion:").strip()

        if opcion == "1":
            ejecutar_cifrado()

        elif opcion =="2":
            ejecutar_cifrado()

        elif opcion =="3":
            mostrar_historial()

        elif opcion =="4":
            mostrar_contador()

        elif opcion == "5":
            exportar_historial()

        elif opcion == "6":
            print("\n Gracias por usar cryptocesar pro.")
            return
        
        else:
            print("\nOpcion invalida, Intente nuevamente.")


principal()