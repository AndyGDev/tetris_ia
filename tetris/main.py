from pieza.modelo import Pieza, TrackingPoint
from libs.problema_espacio_estados import Acción
from pieza.acciones.desplazar import Desplazar

array10_vacio = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
estado = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 0, 0, 1, 1, 1]]

pieza = Pieza("S", 17, 1, estado)
accion_desplazar = Desplazar("Derecha", pieza)
def printear_tablero(estado):
    for level in estado:
        print(level)

def main():
    print(pieza.tracking_point.fila)
    print(pieza.tracking_point.columna)

    printear_tablero(estado)
    print("HACE MOVIMIENTO")
    nuevo_estado = accion_desplazar.aplicar(estado)
    nuevo_estado2 = accion_desplazar.aplicar(nuevo_estado)
    printear_tablero(nuevo_estado2)


if __name__ == '__main__':
    main()
