#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-09-22 16:16:53
# @Author  : houqianzhou
# @Desc    : https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i

from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums) + 1):
                # 移除nums[i:j]
                
                flag = True
                last_num = None
                for k in range(0, i):
                    if last_num and nums[k] <= last_num:
                        flag = False
                        break
                    last_num = nums[k]
                for k in range(j, len(nums)):
                    if last_num and nums[k] <= last_num:
                        flag = False
                        break
                    last_num = nums[k]
                if flag:
                    count += 1
        return count
    

if __name__ == "__main__":
    print(Solution().incremovableSubarrayCount([1, 2, 3, 4]))
