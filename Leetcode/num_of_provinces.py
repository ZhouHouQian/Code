#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-09-25 20:49:53
# @Author  : houqianzhou
# @Desc    : https://leetcode.cn/problems/number-of-provinces/

from typing import List

# 并查集
class DisjointSet:
    def __init__(self, n):
        self.data = list(range(n))

    def find(self, i):
        if i != self.data[i]:
            self.data[i] = self.find(self.data[i])
        return self.data[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        self.data[i] = j

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        disjoint_set = DisjointSet(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    disjoint_set.union(i, j)
        provinces = 0
        for i, item in enumerate(disjoint_set.data):
            if item == i:
                provinces += 1
        return provinces