#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-09-21 22:59:31
# @Author  : houqianzhou
# @Desc    : https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii
from typing import List

# 树状数组
class BinaryIndexTree:
    def __init__(self, n) -> None:
        self.n = n
        self.data = [0] * (n + 1)
    
    def add(self, i):
        while i <= self.n:
            self.data[i] += 1
            i += i & -i

    def query(self, i):
        result = 0
        while i > 0:
            result += self.data[i]
            i -= i & -i
        return result


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums
        sort_nums = sorted(nums)
        index = {}
        for num in sort_nums:
            if num not in index:
                index[num] = len(index) + 1
        arr_a = [nums[0]]
        arr_b = [nums[1]]
        tree_a = BinaryIndexTree(len(index) + 1)
        tree_b = BinaryIndexTree(len(index) + 1)
        tree_a.add(index[nums[0]])
        tree_b.add(index[nums[1]])
        for num in nums[2:]:
            greater_count_a = len(arr_a) - tree_a.query(index[num])
            greater_count_b = len(arr_b) - tree_b.query(index[num])
            if greater_count_a > greater_count_b:
                tree_a.add(index[num])
                arr_a.append(num)
            elif greater_count_a < greater_count_b:
                tree_b.add(index[num])
                arr_b.append(num)
            elif len(arr_a) > len(arr_b):
                tree_b.add(index[num])
                arr_b.append(num)
            else:
                tree_a.add(index[num])
                arr_a.append(num)
        return arr_a + arr_b


if __name__ == "__main__":
    import json
    t = BinaryIndexTree()
    for num in [5, 6, 5, 3, 4, 3, 2, 3, 1]:
        t.insert(num)
    print(json.dumps(t.root.to_dict()))