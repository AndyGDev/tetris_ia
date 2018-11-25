from pieza.modelo import Pieza
from pieza.acciones.desplazar import Desplazar


if __name__ == '__main__':
    pieza = Pieza("S", 2, 3, [1,1,1,1])
    accion_desplazar = Desplazar("Derecha", pieza)
    print(accion_desplazar.pieza.tipo)
    #   print("TETA")
