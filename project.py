import random


#con este metodo guardamos las palabras
def guardarPalabras():
    archivo = open("test.txt", "a")
    palabra = input("Por favor digite la palabra a guardar: ")
    archivo.write(','+palabra) 
    archivo.close()
#con este metodo creamos los jugadores
def CrearJugadores():
    print("Nombre del jugador 1: \n")
    jugador1 = input("Por favor escriba su nombre: ")
    print("\n Nombre del jugador 2: \n")
    jugador2 = input("Por favor escriba su nombre: ")

    return {'nombre1': jugador1,  'error1': 0,'nombre2': jugador2, 'error2': 0}
#con este metodo seleccionamos la palabra con la vamos a jugar
def SeleccionarPalabra():
    archivo = open("test.txt", "r")
    lines = archivo.readlines()
    arrayWords=lines[0].split(",")
    return random.choice(arrayWords)

def verifyWords():
    archivo = open("test.txt", "r")
    lines = archivo.readlines()
    if(len(lines) == 0):
        guardarPalabras()
        guardarPalabras()
##verificamos si ya se adivinaron todas las palabras
def finJuego(PalabraOculta):
    return PalabraOculta.find('*')
    
def reemplazarLetra(letraJugador,palabra,palabraOculta):
    bandera=0
    nuevaPalabra=''
    for index, letra in enumerate(palabra,start=0):
        if(palabraOculta[index] == '*'):
            if(letraJugador == letra):
                nuevaPalabra += letra
                bandera+=1
            else:
                nuevaPalabra +='*'
        else:
            nuevaPalabra += palabraOculta[index]
    if(bandera > 0):
        exito=True
    else:
        exito=False
    return {'PalabraOculta': nuevaPalabra, 'exito':exito}

def juego(jugadores,word):
    print("-------Inicia juego----------")
    print(" ")
    print("-------Adivine la palabra----")
    print(" ")
    PalabraOculta=''
    for i in word:
        PalabraOculta += '*'
    print("La palabra a adivinar es:   " + PalabraOculta)
    print(" ")
    turnoJugador=1
    t=True
        # print(word.split())
    while(t == True):
        letra = input("Jugador " + jugadores["nombre"+str(turnoJugador)]+ " ingrese una letra: ")
        result=reemplazarLetra(letra,word,PalabraOculta)
        PalabraOculta=result["PalabraOculta"]
        print(PalabraOculta)
        if(result['exito'] == False):
            jugadores["error"+str(turnoJugador)] +=1
        fin=finJuego(PalabraOculta)
        if(fin == -1):
            t=False        
        if(turnoJugador==1):
           # print("turno jugador 1")
            turnoJugador=2
        else:
           # print("turno jugador 2")
            turnoJugador=1

    print("Resultado del juego")
    if( jugadores["error1"] > jugadores["error2"] ):
        print ("Felicitaciones ganó: " + jugadores["nombre2"])
    elif( jugadores["error1"] < jugadores["error2"] ):
        print ("Felicitaciones ganó: " + jugadores["nombre1"])
    else:
        if(turnoJugador == 1):
            print ("Felicitaciones ganó: " + jugadores["nombre2"])
        else:
            print ("Felicitaciones ganó: " + jugadores["nombre1"])

        
  ##  print(jugadores)
  ##  print ("ultimo turno"+ str(turnoJugador))
##swich del juego
opcion = 0
while (opcion != 5):
    print("Menu del Juego")
    print(" ")
    print("1. Insertar Palabras     2. Iniciar juego        3. Salir \n")
    opcion = int(input("Cual es tu opcion: "))
    if(opcion == 1):
        guardarPalabras()
    elif( opcion == 2):
        verifyWords() ##verificar que existan palabras
        print("")
        jugadores=CrearJugadores() ##creamos los jugadores
        word=SeleccionarPalabra() ## seleccionar una palabra aleatoriamente
        juego(jugadores,word) ##
    else:
        break
