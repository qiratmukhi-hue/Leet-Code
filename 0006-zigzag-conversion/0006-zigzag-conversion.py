class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge cases: 1 row or string shorter than row count
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        current_row = 0
        step = 1  # 1 for down, -1 for up
        
        for char in s:
            rows[current_row] += char
            
            # Bounce at top and bottom boundaries
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1
                
            current_row += step
            
        return "".join(rows)