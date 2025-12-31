def game_of_life(cell_state: int, alive_neighbors: int) -> int:
    """ Conway's Game of Life rules."""
    if cell_state == 1:
        if alive_neighbors < 2 or alive_neighbors > 3:
            return 0  # Cell dies
        else:
            return 1  # Cell lives
    else:
        if alive_neighbors == 3:
            return 1  # Cell becomes alive
        else:
            return 0  # Cell remains dead
