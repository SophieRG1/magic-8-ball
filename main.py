numero = 0

def on_gesture_shake():
    global numero
    basic.clear_screen()
    numero = randint(0, 9)
    if numero == 0:
        basic.show_string("ES CIERTO")
    elif numero == 1:
        basic.show_string("DEFINITIVAMENTE SI")
    elif numero == 2:
        basic.show_string("SI")
    elif numero == 3:
        basic.show_string("PREGUNTA MAS TARDE")
    elif numero == 4:
        basic.show_string("INTENTA DE NUEVO")
    elif numero == 5:
        basic.show_string("CONCENTRATE Y PRUEBA DE NUEVO")
    elif numero == 6:
        basic.show_string("NO CUENTES CON ELLO")
    elif numero == 7:
        basic.show_string("LA RESPUESTA ES NO")
    elif numero == 8:
        basic.show_string("LO DUDO")
    else:
        basic.show_string("UHMM...")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
