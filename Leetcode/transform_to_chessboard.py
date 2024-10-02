#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-09-24 00:23:13
# @Author  : houqianzhou
# @Desc    : https://leetcode.cn/problems/transform-to-chessboard/

from typing import List


class Solution:
    def count_bit(self, num):
        result = 0
        while num:
            result += 1
            num -= num & (-num)
        return result

    def one_start(self, n):
        num = 0
        for i in range(0, n, 2):
            num += 2 ** i
        return num

    def zero_start(self, n):
        num = 0
        for i in range(1, n, 2):
            num += 2 ** i
        return num

    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        rows, cols = dict(), dict()
        for i in range(n):
            num = 0
            for j in range(n):
                num += (2 ** j) * board[i][j]
            rows[num] = rows.get(num, 0) + 1
        for i in range(n):
            num = 0
            for j in range(n):
                num += (2 ** j) * board[j][i]
            cols[num] = cols.get(num, 0) + 1
        if len(rows) != 2 or len(cols) != 2:
            return -1
        row1, row2 = rows.keys()
        if abs(rows[row1] - rows[row2]) > 1 or (row1 & row2) > 0 or (self.count_bit(row1) != n // 2 and self.count_bit(row1) != (n + 1)// 2):
            return -1
        col1, col2 = cols.keys()
        if abs(cols[col1] - cols[col2]) > 1 or (col1 & col2) > 0 or (self.count_bit(col1) != n // 2 and self.count_bit(col1) != (n + 1) // 2):
            return -1
        row_move, col_move = n, n
        one_start_num = self.one_start(n)
        zero_start_num = self.zero_start(n)
        row_one_move = self.count_bit(one_start_num ^ row1)
        row_zero_move = self.count_bit(zero_start_num ^ row1)
        col_one_move = self.count_bit(one_start_num ^ col1)
        col_zero_move = self.count_bit(zero_start_num ^ col1)
        if not row_one_move % 2:
            row_move = min(row_move, row_one_move // 2)
        if not row_zero_move % 2:
            row_move = min(row_move, row_zero_move // 2)
        if not col_one_move % 2:
            col_move = min(col_move, col_one_move // 2)
        if not col_zero_move % 2:
            col_move = min(col_move, col_zero_move // 2)
        return row_move + col_move
        

if __name__ == "__main__":
    print(Solution().movesToChessboard([[1,0],[1,0]]))    

        