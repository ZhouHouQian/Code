#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-09-22 14:26:18
# @Author  : houqianzhou
# @Desc    : https://leetcode.cn/problems/maximum-profit-in-job-scheduling
from typing import List
from bisect import bisect_right

class Solution:
    # 二分查找
    def search(self, job_list, value, start_idx, end_idx):
        while start_idx < end_idx:
            mid = (start_idx + end_idx) // 2
            if job_list[mid][1] <= value:
                start_idx = mid + 1
            else:
                end_idx = mid
        return start_idx

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        job_list = list(zip(startTime, endTime, profit))
        job_list.sort(key=lambda x: x[1])
        dp = [0] * (len(job_list) + 1)
        for i, job in enumerate(job_list, start=1):
            k = self.search(job_list, job[0], 0, i - 1)
            dp[i] = max(dp[i - 1], dp[k] + job[2])
        return dp[len(job_list)]
