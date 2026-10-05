class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        row = 0
        direction = 1

        for i in range(len(s)):
            rows[row] += s[i]

            if row == numRows - 1:
                direction = -1
            elif row == 0:
                direction = 1

            row = row + direction

        return "".join(rows)