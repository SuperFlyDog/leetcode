class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s

        row = [''] * numRows
        curRow = 0
        up = False

        for c in s:
            row[curRow] += c
            curRow = curRow - 1 if up else curRow + 1
            if curRow == 0 and up:
                up = False
            elif curRow == numRows-1 and not up:
                up = True

        return ''.join(row)
