

class Tablero:

    ROJO = 1
    AMARILLO = 2
    
    def __init__(self):
        self.casillas = [[0 for _ in range(6)] for _ in range(7)]

    def __str__(self) -> str:
        s = "+---"*7 + "+\n"
        for fila in range(6):
            for columna in range(7):
                match self.casillas[columna][fila]:
                    case 1:
                        s += "| O "
                    case 2:
                        s += "| X "
                    case _:
                        s += "|   "
            s += "|\n"
            s += "+---"*7 + "+\n"
        return s


    def ponerFicha(self, columna, color):
        libres = sum(c==0 for c in self.casillas[columna])
        if libres > 0:
            self.casillas[columna][libres - 1] = color
        else:
            raise ValueError(f"Columna {columna} llena")


    def comprobarGanador(self):
        # Comprobar si hay 4 en raya en sentido vertical
        for fila in range(3):
            for columna in range(7):
                if self.casillas[columna][fila] != 0 \
                    and self.casillas[columna][fila] == self.casillas[columna][fila+1] \
                    and self.casillas[columna][fila] == self.casillas[columna][fila+2] \
                    and self.casillas[columna][fila] == self.casillas[columna][fila+3]:
                        return self.casillas[columna][fila] # Tenemos ganador
        # Comprobar si hay 4 en raya en sentido horizontal
        for fila in range(6):
            for columna in range(4):
                if self.casillas[columna][fila] != 0 \
                    and self.casillas[columna][fila] == self.casillas[columna+1][fila] \
                    and self.casillas[columna][fila] == self.casillas[columna+2][fila] \
                    and self.casillas[columna][fila] == self.casillas[columna+3][fila]:
                        return self.casillas[columna][fila] # Tenemos ganador        
        # Comprobar si hay 4 en raya en sentido diagonal / o \
        for fila in range(3):
            for columna in range(4):
                if self.casillas[columna][fila] != 0 \
                    and self.casillas[columna][fila] == self.casillas[columna+1][fila+1] \
                    and self.casillas[columna][fila] == self.casillas[columna+2][fila+2] \
                    and self.casillas[columna][fila] == self.casillas[columna+3][fila+3]:
                        return self.casillas[columna][fila] # Tenemos ganador 
            for columna in range(3, 7):
                if self.casillas[columna][fila] != 0 \
                    and self.casillas[columna][fila] == self.casillas[columna-1][fila+1] \
                    and self.casillas[columna][fila] == self.casillas[columna-2][fila+2] \
                    and self.casillas[columna][fila] == self.casillas[columna-3][fila+3]:
                        return self.casillas[columna][fila] # Tenemos ganador              
        # Si no se da alguna de las anteriores, devolver 0
        return 0


if __name__ == '__main__':
    tablero = Tablero()
    tablero.ponerFicha(0, Tablero.ROJO)
    tablero.ponerFicha(0, Tablero.AMARILLO)
    tablero.ponerFicha(6, Tablero.ROJO)
    print(tablero)
    tablero.ponerFicha(0, Tablero.ROJO)
    tablero.ponerFicha(0, Tablero.AMARILLO)
    tablero.ponerFicha(0, Tablero.ROJO)
    tablero.ponerFicha(0, Tablero.AMARILLO)
    try:
        tablero.ponerFicha(0, Tablero.ROJO) # Esta no se llega a colocar
    except ValueError as err:
        print("No puedes colocar ahí:", err)
    print("Ganador:", tablero.comprobarGanador())
    tablero.ponerFicha(1, Tablero.ROJO)
    tablero.ponerFicha(1, Tablero.AMARILLO)
    tablero.ponerFicha(2, Tablero.ROJO)
    tablero.ponerFicha(2, Tablero.AMARILLO)
    tablero.ponerFicha(6, Tablero.ROJO)
    tablero.ponerFicha(3, Tablero.AMARILLO)
    tablero.ponerFicha(6, Tablero.ROJO)
    tablero.ponerFicha(1, Tablero.AMARILLO)
    print(tablero)
    print("Ganador:", tablero.comprobarGanador())
