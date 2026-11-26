class Solution:
    def canAliceWin(self, n: int) -> bool:
        take, moves = 10, 0
        while n >= take:
            n -= take
            take -= 1
            moves += 1
        return moves % 2 == 1
