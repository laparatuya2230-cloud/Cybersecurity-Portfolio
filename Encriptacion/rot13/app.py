# ============================================
# Proyecto: CryptoROT Suite
# Descripcion:
# Aplicacion de consola para transformar mensajes
# usando el algoritmo ROT13.
# ============================================

historial = []
contador_operaciones = 0


def mostrar_menu():
    print("\n===== CRYPTOROT SUITE =====")
    print("1. Transformar mensaje con ROT13")
    print("2. Ver historial")
    print("3. Ver contador de operaciones")
    print("4. Limpiar historial")
    print("5. Exportar historial a TXT")
    print("6. Salir")


def aplicar_rot13(texto):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():

            if caracter.isupper():
                codigo_base = 65
            else:
                codigo_base = 97

            posicion = ord(caracter) - codigo_base
            nueva_posicion = (posicion + 13) % 26
            nuevo_caracter = chr(nueva_posicion + codigo_base)

            resultado += nuevo_caracter

        else:
            resultado += caracter

    return resultado


def guardar_historial(mensaje_original, resultado):
    historial.append({
        "original": mensaje_original,
        "resultado": resultado
    })


def mostrar_historial():
    if len(historial) == 0:
        print("\nNo existen registros en el historial.")
    else:
        print("\n===== HISTORIAL =====")

        for indice, registro in enumerate(historial, start=1):
            print(f"\nOperacion #{indice}")
            print(f"Original : {registro['original']}")
            print(f"Resultado: {registro['resultado']}")
            print("--------------------------")


def mostrar_contador():
    print(f"\nTotal de mensajes procesados: {contador_operaciones}")


def limpiar_historial():
    historial.clear()
    print("\nHistorial limpiado correctamente.")


def exportar_historial():
    if len(historial) == 0:
        print("\nNo hay historial para exportar.")
        return

    archivo = open("historial_rot13.txt", "w", encoding="utf-8")

    archivo.write("===== HISTORIAL CRYPTOROT SUITE =====\n")

    for indice, registro in enumerate(historial, start=1):
        archivo.write(f"\nOperacion #{indice}\n")
        archivo.write(f"Original : {registro['original']}\n")
        archivo.write(f"Resultado: {registro['resultado']}\n")
        archivo.write("--------------------------\n")

    archivo.close()

    print("\nHistorial exportado correctamente.")
    print("Archivo generado: historial_rot13.txt")


def transformar_mensaje():
    global contador_operaciones

    mensaje = input("\nDigite el mensaje: ")

    resultado = aplicar_rot13(mensaje)

    print("\nResultado:")
    print(resultado)

    guardar_historial(mensaje, resultado)

    contador_operaciones += 1


def principal():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            transformar_mensaje()

        elif opcion == "2":
            mostrar_historial()

        elif opcion == "3":
            mostrar_contador()

        elif opcion == "4":
            limpiar_historial()

        elif opcion == "5":
            exportar_historial()

        elif opcion == "6":
            print("\nFinalizando programa...")
            return

        else:
            print("\nOpcion invalida. Intente nuevamente.")


principal()