#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-09-22 20:56:56
# @Author  : houqianzhou
# @Desc    : https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices


from typing import List


class Solution:
    # def search(self, nums: List[int], value, start_idx, end_idx):
    #     while start_idx < end_idx:
    #         mid = (start_idx + end_idx) // 2
    #         if nums[mid] >= value:
    #             end_idx = mid
    #         else:
    #             start_idx = mid + 1
    #     print(nums, value, start_idx)
    #     return start_idx

    def has_match(self, nums, m):
        for i in range(m):
            if nums[i] * 2 > nums[len(nums) - m + i]:
                return False
        return True

    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) // 2
        result = 0
        while i < j:
            m = (i + j + 1) // 2
            if self.has_match(nums, m):
                i = m
            else:
                j = m - 1 
        return i * 2


if __name__ == "__main__":
    print(Solution().maxNumOfMarkedIndices([3,5,2,4]))
    print(Solution().maxNumOfMarkedIndices([9,2,5,4]))
    print(Solution().maxNumOfMarkedIndices([2,4,8,16]))
    print(Solution().maxNumOfMarkedIndices([7,6,8]))
