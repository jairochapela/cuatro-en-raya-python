from jugadores import JugadorHumano, JugadorIA
from tablero import Tablero


class Game:

    def __init__(self, modoHumano = False):
        self.tablero = Tablero()
        self.jugadores = [
            JugadorHumano(Tablero.ROJO),  # jugador 0
            JugadorHumano(Tablero.AMARILLO) if modoHumano else JugadorIA(Tablero.AMARILLO)   # jugador 1
        ]
        self.turno = 0

    def cambiarTurno(self):
        '''
        Alterna el turno de los jugadores: 0, 1, 0, 1, ...
        '''
        self.turno = 0 if self.turno else 1


    def esFinDeJuego(self) -> bool:
        '''
        Compruebas si el juego ha llegado a su fin; bien porque uno de los
        dos jugadores pudo colocar 4 en raya, bien porque se ha llenado el 
        tablero y no hay ganador.
        '''
        return self.tablero.lleno or self.tablero.comprobarGanador()!=0
    
    def iniciar(self):
        '''
        Inicia el juego.
        Mientras no se de la condición de final del juego, se alternarán los turnos
        pidiédole a cada jugador que efectúen su jugada y se colocará la ficha en 
        la posición escogida por cada uno de ellos.
        Cuando el juego termine, se anunciará al ganador, si lo hay.
        '''
        while not self.esFinDeJuego():
            # Al comienzo de cada vuelta, dibujamos el tablero
            print(self.tablero)

            eleccion = self.jugadores[self.turno].jugar()
            try:
                self.tablero.ponerFicha(eleccion, self.jugadores[self.turno].color)
            except ValueError as err:
                # Si hay algún problema colocando la ficha, se mostrará el error
                # y se volverá a pedir al jugador que realice su jugada
                print(err)
                continue

            self.cambiarTurno()

        # Al salir del bucle, el juego ha terminado
        print(self.tablero)
        ganador = self.tablero.comprobarGanador()
        if ganador:
            print(f"El ganador es el jugador {ganador}")
        else:
            print("Empate")
