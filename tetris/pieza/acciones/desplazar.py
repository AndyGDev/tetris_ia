from libs.problema_espacio_estados import Acción
import copy
from pieza.modelo import Pieza
class Desplazar(Acción):

    def __init__(self, direccion, pieza):
        #super().__init__()
        self.direccion = direccion
        self.pieza = pieza
        self.estado = self.pieza.tablero




    def es_aplicable(self, estado):
        if self.direccion == "Derecha":
             return not  self.pieza.is_colision_derecha(self)

        elif self.direccion == "Izquierda":
             return not self.pieza.is_colision_izquierda(self)

        elif self.direccion == "Abajo":
             return not self.pieza.is_colision_debajo(self)

        return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        tp = self.pieza.tracking_point
        nuevo_estado[tp.fila - 1][tp.columna] = 0
        nuevo_estado[tp.fila - 1][tp.columna + 2] = 1
        nuevo_estado[tp.fila - 2][tp.columna + 1] = 0
        nuevo_estado[tp.fila - 2][tp.columna + 3] = 1
        return nuevo_estado
