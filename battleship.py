class Ship:
    """
    Se crea la clase Ship (Nave/Barco)
    Parámetros: name & size del barco
    Atributos: positions & hits de los barcos
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []  # Se inicializa vacía la lista de posiciones
        self.hits = 0        # Se inicializan en 0 los impactos

    def place_ship(self, board, start_row, start_col, direction):
        directions = {'H': (0, 1), 'V': (1, 0)}  # Direcciones: Horizontal y Vertical
        
        if direction not in directions:
            print("Dirección inválida, utiliza 'H' para horizontal y 'V' para vertical")
            return False
        
        dr, dc = directions[direction]
        end_row = start_row + (self.size - 1) * dr
        end_col = start_col + (self.size - 1) * dc
        
        # Verificar si el barco cabe en el tablero
        if end_row >= len(board) or end_col >= len(board[0]):
            print(f"El barco {self.name} no cabe en esta posición.")
            return False
        
        # Verificar si las posiciones están vacías
        for i in range(self.size):
            row = start_row + i * dr
            col = start_col + i * dc
            if board[row][col] != ' ':
                print(f"Espacio ocupado. El barco {self.name} no puede colocarse aquí.")
                return False
        
        # Colocar el barco
        for i in range(self.size):
            row = start_row + i * dr
            col = start_col + i * dc
            board[row][col] = self.name[0]  # Usa la primera letra del nombre del barco
            self.positions.append((row, col))  # Registra la posición
        
        print(f"El barco {self.name} fue colocado con éxito.")
        return True

def create_ship(board, ship_number):
    print(f"\nCreando Barco {ship_number}:")
    name = input("Nombra el Barco: \n")
    size = int(input("Define el largo del barco: \n"))
    start_row = int(input("Introduce renglón: \n"))
    start_col = int(input("Introduce columna: \n"))
    direction = input("Introduce 'H' o 'V' según quieras colocar el barco: \n").upper()
    
    ship = Ship(name, size)
    if not ship.place_ship(board, start_row, start_col, direction):
        print("Error al colocar el barco. Intenta de nuevo.")
        return create_ship(board, ship_number)  # Reintentar la creación del barco
    return ship

def print_board(board):
    print("\nTablero:")
    for row in board:
        print(' | '.join(row))
    print()

# Crear el tablero
tamanio_tablero = int(input("Define el tamaño del tablero: \n"))
board = [[' ' for _ in range(tamanio_tablero)] for _ in range(tamanio_tablero)]

# Crear barcos
barco1 = create_ship(board, 1)
barco2 = create_ship(board, 2)

# Imprimir el tablero para verificar
print_board(board)