import numpy as np

class grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.state = np.zeros((rows, cols), dtype=np.uint8)

    def randomize(self, prob: float = 0.2):
        self.state = (np.random.rand(self.rows, self.cols) < probability).astype(np.uint8)

    def clear(self) -> None:
        self.state.fill(0)

    def toggle_cell(self, row: int, col: int) -> None:
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.state[row, col] ^= 1
    def get_state(self) -> np.ndarray:
        return self.state.copy()
