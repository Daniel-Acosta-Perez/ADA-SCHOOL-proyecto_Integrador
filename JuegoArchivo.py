from Juego import Juego

class JuegoArchivo(Juego):
    def __init__(self, map_path, start_pos, end_pos):
        if not self._is_valid_position(start_pos):
            raise ValueError("Invalid start position")
        if not self._is_valid_position(end_pos):
            raise ValueError("Invalid end position")

        with open(map_path, "r") as map_file:
            map_data = map_file.read()
        map_data = map_data.strip()
        map_rows = map_data.split("\n")
        map_matrix = [list(row) for row in map_rows]
        super().__init__(map_matrix, start_pos, end_pos) # type: ignore

    def _is_valid_position(self, position):
        # Check if position is within the bounds of the map
        # Return True if valid, False otherwise
        ...