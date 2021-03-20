class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day(cells):
            new_cell = []
            for pos in range(len(cells)):
                if pos == 0 or pos == len(cells) - 1 or \
                    (cells[pos - 1] ^ cells[pos + 1]):
                    new_cell.append(0)
                else:
                    new_cell.append(1)
            return new_cell
        
        prev_cells = {tuple(cells):n}
        
        while n > 0:
            cells = tuple(next_day(cells))
            if cells in prev_cells:
                n -= 1
                cycle_len = prev_cells[cells] - n
                n %= cycle_len
                break
            n -= 1
            prev_cells[cells] = n
            
        
        for ii in range(n):
            cells = next_day(cells)
        return cells

        
        