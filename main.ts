let numero = 0
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    numero = randint(0, 9)
    if (numero == 0) {
        basic.showString("ES CIERTO")
    } else if (numero == 1) {
        basic.showString("DEFINITIVAMENTE SI")
    } else if (numero == 2) {
        basic.showString("SI")
    } else if (numero == 3) {
        basic.showString("PREGUNTA MAS TARDE")
    } else if (numero == 4) {
        basic.showString("INTENTA DE NUEVO")
    } else if (numero == 5) {
        basic.showString("CONCENTRATE Y PRUEBA DE NUEVO")
    } else if (numero == 6) {
        basic.showString("NO CUENTES CON ELLO")
    } else if (numero == 7) {
        basic.showString("LA RESPUESTA ES NO")
    } else if (numero == 8) {
        basic.showString("LO DUDO")
    } else {
        basic.showString("UHMM...")
    }
})
