#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-10-02 15:44:47
# @Author  : houqianzhou
# @Desc    : https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/description/


from typing import List


# 二分法
class Solution:
    def get(self, dist, m):
        s = sum([(d + m - 1) // m for d in dist[:-1]])
        s += dist[-1] / m
        return s

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        max_dist = max(dist) * 101
        s, e = 1, max_dist
        while s < e:
            m = (s + e) // 2
            if self.get(dist, m) > hour:
                s = m + 1
            else:
                e = m
        return s
