class Pieza:

    def __init__(self, tipo, tracking_point_fila, tracking_point_columna, tablero):
        if tipo not in ["I", "J", "L", "O", "S", "T", "Z"]:
            raise ValueError("Ese tipo de pieza no es valido")
        self.area = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.tipo = tipo
        self.forma = self.get_forma_from_tipo()
        self.tracking_point = TrackingPoint(tracking_point_fila, tracking_point_columna)
        self.tablero = tablero

    def get_forma_from_tipo(self):
        if self.tipo == "S":
            return [[0, 1, 1],
                    [1, 1, 0],
                    [0, 0, 0]]
        # TODO: Completar resto de casos (tipos)

    # En el momento que algun 1 del array 3(filas) del area de la pieza, sea colindante a un 1 del
    # tablero actual, o al borde del tablero se considera una colision
    def is_colision_debajo(self):
        for i in range(0, 3):
            if self.forma[2][i] == 1:
                if self.tracking_point.fila == 0 or self.tablero[self.tracking_point.fila+1][self.tracking_point.columna+i] == 1:
                    return True
        return False

    def is_colision_izquierda(self):
        for i in range(0, 3):
            if self.forma[i][0] == 1:
                if self.tracking_point.columna == 0 or self.tablero[self.tracking_point.fila-i][self.tracking_point.columna-1] == 1:
                    return True
        return False

    def is_colision_derecha(self):
        for i in range(0, 3):
            if self.forma[i][2] == 1:
                if self.tracking_point.columna + 3 == 9 or self.tablero[self.tracking_point.fila-i][self.tracking_point.columna+3] == 1:
                    return True
        return False


class TrackingPoint:

    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna



