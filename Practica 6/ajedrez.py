import chess
import copy
'''
tamTablero = 3
board = chess.Board()
board.clear()
rey_1 = 1
rey_2 = 3
board.set_piece_at(chess.A8, chess.Piece.from_symbol("r"))
board.set_piece_at(chess.H8, chess.Piece.from_symbol("R"))
movimiento = chess.Move.from_uci("h8g8")
movimiento = chess.Move.from_uci("a8g8")
board.push(movimiento)'''

class Pieza(object):
    def __init__ (self,posx, posy, numTablero):
        self.x = posx
        self.y = posy
        self.y = numTablero = numTablero

class Ajedrez(object):
    def __init__(self):
        self.tablero = self.generarTablero()
        self.rey_1 = Pieza(0,0,1)
        self.rey_2 = Pieza(0,7,8)
        
    def generarTablero(self):
        board = []
        temp = []
        for i in range(1,65):
            temp.append(i)
            if i % 8 == 0:
                temporal = copy.copy(temp)
                board.append(temporal)
                temp.clear()
        return board
    
    def obtenerCoordenadas(self, numero):
        y = (numero-1)%8 
        x = numero//8
        return (x,y)
    
    def obtenerAlrededor(self, x, y):
        alrededores = []
        if x == 0:
            if y == 0:
                if x != 7:
                    alrededores.append(self.tablero[x+1][y+1])
                    alrededores.append(self.tablero[x+1][y])
                if y != 7:
                    alrededores.append(self.tablero[x][y+1])
            else:
                if x!= 7:
                    alrededores.append(self.tablero[x+1][y-1])
                    if y!= 7:
                        alrededores.append(self.tablero[x+1][y+1])
                alrededores.append(self.tablero[x+1][y])
                if y!= 7:
                    alrededores.append(self.tablero[x][y+1])
                alrededores.append(self.tablero[x][y-1])
        else:
            if y == 0:
                if x != 7:
                    alrededores.append(self.tablero[x+1][y])
                    if y != 7 :
                        alrededores.append(self.tablero[x+1][y+1])
                        alrededores.append(self.tablero[x][y+1])
                        alrededores.append(self.tablero[x-1][y+1])
                alrededores.append(self.tablero[x-1][y])
            else:
                if x != 7:
                    alrededores.append(self.tablero[x+1][y-1])
                    alrededores.append(self.tablero[x+1][y])
                if y!= 7:
                    alrededores.append(self.tablero[x-1][y+1])
                    if x != 7:
                        alrededores.append(self.tablero[x+1][y+1])
                    alrededores.append(self.tablero[x][y+1])
                alrededores.append(self.tablero[x][y-1])
                alrededores.append(self.tablero[x-1][y-1])
                alrededores.append(self.tablero[x-1][y])
        print(alrededores)
        return alrededores

ajedrez = Ajedrez()
print(ajedrez.tablero)
for i in ajedrez.obtenerAlrededor(7,0):
    print(i)
    print(ajedrez.obtenerCoordenadas(i))
    