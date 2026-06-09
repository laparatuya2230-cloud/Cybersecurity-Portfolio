# GUÍA #3 - Cifrado y Descifrado Vigenère
# CryptoVigenere Suite

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def limpiar_clave(clave):
    """
    Deja la clave solamente con letras A-Z.
    Ejemplo: 'K F H 123' -> 'KFH'
    """
    clave_limpia = ""

    for letra in clave:
        letra = letra.upper()

        if letra in ALFABETO:
            clave_limpia += letra

    return clave_limpia


def cifrar_vigenere(texto, clave):
    resultado = ""
    clave = limpiar_clave(clave)

    if clave == "":
        return None

    indice_clave = 0

    for caracter in texto:
        letra_mayuscula = caracter.upper()

        if letra_mayuscula in ALFABETO:
            valor_texto = ord(letra_mayuscula) - 65
            valor_clave = ord(clave[indice_clave % len(clave)]) - 65

            cifrado = (valor_texto + valor_clave) % 26

            if caracter.isupper():
                resultado += chr(cifrado + 65)
            else:
                resultado += chr(cifrado + 97)

            indice_clave += 1

        else:
            resultado += caracter

    return resultado


def descifrar_vigenere(texto, clave):
    resultado = ""
    clave = limpiar_clave(clave)

    if clave == "":
        return None

    indice_clave = 0

    for caracter in texto:
        letra_mayuscula = caracter.upper()

        if letra_mayuscula in ALFABETO:
            valor_texto = ord(letra_mayuscula) - 65
            valor_clave = ord(clave[indice_clave % len(clave)]) - 65

            descifrado = (valor_texto - valor_clave) % 26

            if caracter.isupper():
                resultado += chr(descifrado + 65)
            else:
                resultado += chr(descifrado + 97)

            indice_clave += 1

        else:
            resultado += caracter

    return resultado


def mostrar_menu():
    print("\n===== CRYPTOVIGENERE SUITE =====")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Ver historial")
    print("4. Cambiar clave")
    print("5. Exportar historial")
    print("6. Ver estadísticas")
    print("7. Salir")


def mostrar_historial(historial):
    print("\n===== HISTORIAL =====")

    if len(historial) == 0:
        print("No existen registros.")
    else:
        for registro in historial:
            print(f"Operación : {registro['operacion']}")
            print(f"Texto     : {registro['texto']}")
            print(f"Clave     : {registro['clave']}")
            print(f"Resultado : {registro['resultado']}")
            print("---------------------")


def exportar_historial(historial):
    if len(historial) == 0:
        print("\nNo hay historial para exportar.")
        return

    archivo = open("historial_vigenere.txt", "w", encoding="utf-8")

    archivo.write("===== HISTORIAL VIGENERE =====\n\n")

    for registro in historial:
        archivo.write(f"Operación : {registro['operacion']}\n")
        archivo.write(f"Texto     : {registro['texto']}\n")
        archivo.write(f"Clave     : {registro['clave']}\n")
        archivo.write(f"Resultado : {registro['resultado']}\n")
        archivo.write("---------------------\n")

    archivo.close()

    print("\nHistorial exportado correctamente en historial_vigenere.txt")


def mostrar_estadisticas(contador_cifrados, contador_descifrados):
    total = contador_cifrados + contador_descifrados

    print("\n===== ESTADÍSTICAS =====")
    print(f"Cifrados realizados     : {contador_cifrados}")
    print(f"Descifrados realizados  : {contador_descifrados}")
    print(f"Total de operaciones    : {total}")


def pedir_clave():
    while True:
        clave = input("Digite la clave: ")
        clave_limpia = limpiar_clave(clave)

        if clave_limpia != "":
            return clave

        print("La clave debe contener al menos una letra.")


def principal():
    historial = []

    contador_cifrados = 0
    contador_descifrados = 0

    clave_actual = pedir_clave()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mensaje = input("\nDigite el mensaje: ")

            resultado = cifrar_vigenere(mensaje, clave_actual)

            print("\nMensaje cifrado:")
            print(resultado)

            historial.append({
                "operacion": "Cifrado",
                "texto": mensaje,
                "clave": clave_actual,
                "resultado": resultado
            })

            contador_cifrados += 1

        elif opcion == "2":
            mensaje = input("\nDigite el mensaje cifrado: ")

            resultado = descifrar_vigenere(mensaje, clave_actual)

            print("\nMensaje descifrado:")
            print(resultado)

            historial.append({
                "operacion": "Descifrado",
                "texto": mensaje,
                "clave": clave_actual,
                "resultado": resultado
            })

            contador_descifrados += 1

        elif opcion == "3":
            mostrar_historial(historial)

        elif opcion == "4":
            clave_actual = pedir_clave()
            print("\nClave cambiada correctamente.")

        elif opcion == "5":
            exportar_historial(historial)

        elif opcion == "6":
            mostrar_estadisticas(contador_cifrados, contador_descifrados)

        elif opcion == "7":
            print("\nFinalizando programa...")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


principal()