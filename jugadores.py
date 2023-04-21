import random
from tablero import Tablero


class Jugador:
    
    def __init__(self, color):
        self.color = color

    def jugar(self):
        pass


class JugadorHumano(Jugador):
    
    def jugar(self):
        while True:
            try:
                columna = int(input("Introduce columna (entre 0 y 6): "))
                if columna < 0 or columna > 6:
                    raise ValueError("La columna debe estar entre 0 y 6")
                # Si no hay errores antes, llegamos al return que devuelve la columna elegida
                return columna
            except ValueError as err:
                print(f"Columna incorrecta: {err}")



class JugadorIA(Jugador):
    
    def jugar(self):
        return random.randint(0, 6)




if __name__ == '__main__':
    jh = JugadorHumano(Tablero.ROJO)
    eleccion = jh.jugar()
    print(f"Has elegido la columna {eleccion}")
    tab = Tablero()
    tab.ponerFicha(eleccion, jh.color)
    print(tab)