from game import Game


if __name__ == '__main__':
    while True:
        opcion = input("Quieres jugar contra la máquina o contra otro jugador? (m/j), s para salir:")
        try:
            match opcion.lower():
                case "m":
                    g = Game()
                    break
                case "j":
                    g = Game(modoHumano=True)
                    break
                case "s":
                    exit()
                case _:
                    raise ValueError("Opción no válida")
        except ValueError as err:
            print(err)
            
    g.iniciar()