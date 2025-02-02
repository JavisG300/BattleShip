class Ship:
    """
    Se crea la clase Ship (Nave/Barco)
    Parámetros: name & size del barco
    Atibutos: positions & hits de los barcos
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = [] # Se inicializa vacía la lista de posiciones
        self.hits = 0       # Se inicializan en 0 los impactos

    # Metodo place_ship
    def place_ship(self, board, start_row, start_col, direction):
        if direction == 'H':
           if start_col + self.size - 1 >= len(board[0]):
               print("El barco no cabe horizontalmente en esta posicion")
               return False
        elif direction == 'V':
           if start_row + self.size - 1 >= len(board):
               print("El barco no cabe verticalmente en esta posicion")
               return False
        else:
           print("Direccion inválida, utiliza 'H' para horixontal y 'V' para vertical")
           return False
    
        # Paso 2: Verificar si las posiciones están vacías
        if direction == 'H':  # Horizontal
            for col in range(start_col, start_col + self.size):
                if board[start_row][col] != ' ':
                    print(f"Espacio ocupado. El barco {self.name} no puede colocarse aquí.")
                    return False
        elif direction == 'V':  # Vertical
            for row in range(start_row, start_row + self.size):
                if board[row][start_col] != ' ':
                    print(f"Espacio ocupado. El barco {self.name} no puede colocarse aquí.")
                    return False
        
        #Paso 3, colocar el barco
        if direction == 'H':  # Horizontal
            for col in range(start_col, start_col + self.size):
                board[start_row][col] = self.name[0]  # Usa la primera letra del nombre del barco
                self.positions.append((start_row, col))  # Registra la posición
        elif direction == 'V':  # Vertical
            for row in range(start_row, start_row + self.size):
                board[row][start_col] = self.name[0]  # Usa la primera letra del nombre del barco
                self.positions.append((row, start_col))  # Registra la posición

        print(f"El barco {self.name} fue colocado con éxito.")
        return True
    

# Crear el tablero
tamanioTablero = int(input("Define el tamaño del tablero: \n"))
board = [[' ' for _ in range(tamanioTablero)] for _ in range(tamanioTablero)]

#Crea barco1 y su posicion
nombreBarco1 = str(input("Nombra el Barco 1: \n"))
tamanioBarco1 = int(input("Define el largo del barco 1: \n"))
posicionRenglonBarco1 = int(input("Introduce renglon: \n"))
posicionColumnaBarco1 = int(input("Introduce columna: \n"))
horientacionBarco1 = str(input("Introduce 'H' o 'V' segun quieras colocar el Barco 1: \n"))
barco1 = Ship(nombreBarco1, tamanioBarco1)
barco1.place_ship(board,posicionRenglonBarco1,posicionColumnaBarco1,horientacionBarco1)

#Crea barco2 y su posicion
nombreBarco2 = str(input("Nombra el Barco 2: \n"))
tamanioBarco2 = int(input("Define el largo del barco 2: \n"))
posicionRenglonBarco2 = int(input("Introduce renglon: \n"))
posicionColumnaBarco2 = int(input("Introduce columna: \n"))
horientacionBarco2 = str(input("Introduce 'H' o 'V' segun quieras colocar el Barco 1: \n"))
barco1 = Ship(nombreBarco2, tamanioBarco2)
barco1.place_ship(board,posicionRenglonBarco2,posicionColumnaBarco2,horientacionBarco2)




# Imprimir el tablero para verificar
for row in board:
    print(' | '.join(row))

