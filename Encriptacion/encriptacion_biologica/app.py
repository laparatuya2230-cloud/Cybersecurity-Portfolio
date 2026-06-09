#Lista para guardar los resultados en memoria 
historial = []

def solicitar_edad():
    while True:
        entrada = input('Favor de digite su edad:')
        #Permite Números positivos, cero y negativos 
        if entrada.lstrip('-').isdigit(): 
            return int(entrada)
        else: 
            print('Error al digitar a su edad, favor digitar un valor numerico.')


def clasificar_edad(edad):
    etapas = [
        (lambda e: e < 0, 'Aun no has nacido'),
        (lambda e: e == 0, 'Eres un/a neonato/a'),
        (lambda e: e >= 1    and e <=13, 'Eres un/a niño/a'),
        (lambda e: e >= 14  and e <=17,   'Eres un/a joven'),
        (lambda e: e >= 18  and e <=29,  'Eres un/a adurto/a en progreso'),
        (lambda e: e >= 30  and e <=59, 'Eres un/a adulto/a realido/a'),
        (lambda e: e >= 60  and e <=79, 'Eres un/a evejeciente'),
        (lambda e: e >= 80  and e <=99,  'Eres un/a Geriatico/a'),
        (lambda e: e >= 100 and e <=120, 'Eres un/a milagro '),
        (lambda e: e >= 121 and e <=139,    'Eres un/a leyenda (record guiness)'),
        (lambda e: e >= 140,    'jabaldor/a')
    ]

    #Uso de for para recorrer las condiciones 
    for condicion,mensaje in etapas:
        if condicion(edad):
            return mensaje
    
def guardar_resultado(edad, resultado):
    historial.append({
        'edad': edad,
        'resultado': resultado
    })

def mostrar_historial():
    if len(historial) == 0:
        print('No hay resultados guardados todaia.')
    else:
        print('\nHistorial de resultados:')

        #Uso de for para mostrar los resultados almacenados en memoria 
        for indice, registro in enumerate(historial, start=1):
            print (f'{indice},  Edad: {registro["edad"]} - Resultado: {registro["resultado"]}')



def transicion_bilogica():
    print('\nIdentificador de transicion Biologica')

    edad = solicitar_edad()
    resultado = clasificar_edad(edad)


    print(resultado)
    guardar_resultado(edad, resultado)


def menu():
    while True:
        print('\n===== Menu Principal =====')
        print ('1. Identificar transicion biologica')
        print('2. Ver hsitorial de resultados')
        print('3. Salir')


        opcion = input('Selecione una opcion:')



        if opcion == '1':
            transicion_bilogica()
        elif opcion == '2':
            mostrar_historial()
        elif opcion == '3':
            print('Muchas gracias por usar nuestra aplicacion!!')
            return
        else:
            print ('Opcion invalida. Favor selecionar una opcion correcta.')



menu()