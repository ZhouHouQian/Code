#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-09-25 01:32:07
# @Author  : houqianzhou
# @Desc    : https://leetcode.cn/problems/kth-largest-element-in-a-stream

# 最小堆/优先队列
from typing import List


class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)
        i = len(self.data) - 1
        while i > 0:
            j = (i - 1) // 2
            if self.data[i] < self.data[j]:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                i = j
                continue
            break

    def pop(self):
        result = self.data[0]
        self.data[0] = self.data.pop()
        i = 0
        while i * 2 + 1 < len(self.data):
            j = i * 2 + 1
            k = i * 2 + 2
            if k < len(self.data) and self.data[k] < self.data[j]:
                j = k
            if self.data[i] > self.data[j]:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                i = j
                continue
            break
        return result

    def top(self):
        return self.data[0]

    def size(self):
        return len(self.data)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = PriorityQueue()
        self.k = k
        for num in nums:
            self.queue.push(num)

    def add(self, val: int) -> int:
        self.queue.push(val)
        while self.queue.size() > self.k:
            self.queue.pop()
        return self.queue.top()



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)