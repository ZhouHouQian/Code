#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-09-21 22:59:31
# @Author  : houqianzhou
# @Desc    : https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii
from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.height = 1
        self.left = None
        self.right = None

    def update_height(self):
        if self.left and self.right:
            self.height = max(self.left.height, self.right.height) + 1 
        elif self.left:
            self.height = self.left.height + 1
        elif self.right:
            self.height = self.right.height + 1
        else:
            self.height = 1

    def to_dict(self):
        return {
            "val": self.val,
            "count": self.count,
            "height": self.height,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None
        }

# 平衡二叉树
class BinSearchTree:
    def __init__(self):
        self.arr = []
        self.root = None

    def insert(self, val):
        self.arr.append(val)
        self.root = self.insert_node(self.root, val)
    
    def insert_node(self, current_node, val):
        if not current_node:
            return Node(val)
        
        if val < current_node.val:
            current_node.left = self.insert_node(current_node.left, val)
        elif val > current_node.val:
            current_node.right = self.insert_node(current_node.right, val)
        else:
            current_node.count += 1
            return current_node
        
        current_node.count += 1
        current_node.update_height()
        balance = self.get_balance(current_node)
        if balance > 1:
            left_balance = self.get_balance(current_node.left)
            if left_balance <= -1:
                current_node.left = self.left_rotate(current_node.left)
            current_node = self.right_rotate(current_node)
        elif balance < -1:
            right_balance = self.get_balance(current_node.right)
            if right_balance >= 1:
                current_node.right = self.right_rotate(current_node.right)
            current_node = self.left_rotate(current_node)
        return current_node

    def get_balance(self, node):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        balance = left_height - right_height
        return balance

    def right_rotate(self, node):
        x = node.left
        x_count = node.count
        node_count = node.count - x.count + (x.right.count if x.right else 0)
        node.left = x.right
        x.right = node
        node.update_height()
        x.update_height()
        node.count = node_count
        x.count = x_count
        return x        

    def left_rotate(self, node):
        x = node.right
        x_count = node.count
        node_count = node.count - x.count + (x.left.count if x.left else 0)
        node.right = x.left
        x.left = node
        node.update_height()
        x.update_height()
        node.count = node_count
        x.count = x_count
        return x

    def get_greater_count(self, val):
        if not self.root:
            return 0
        greater_count = 0
        node = self.root
        while True:
            if val == node.val:
                greater_count += node.right.count if node.right else 0
                break
            elif val < node.val:
                greater_count += node.count - (node.left.count if node.left else 0)
                node = node.left
            else:
                node = node.right
            if not node:
                break
        return greater_count


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums
        tree_a = BinSearchTree()
        tree_b = BinSearchTree()
        tree_a.insert(nums[0])
        tree_b.insert(nums[1])
        for num in nums[2:]:
            greater_count_a = tree_a.get_greater_count(num)
            greater_count_b = tree_b.get_greater_count(num)
            if greater_count_a > greater_count_b:
                tree_a.insert(num)
            elif greater_count_a < greater_count_b:
                tree_b.insert(num)
            elif tree_a.root.count > tree_b.root.count:
                tree_b.insert(num)
            else:
                tree_a.insert(num)
        return tree_a.arr + tree_b.arr


if __name__ == "__main__":
    import json
    t = BinSearchTree()
    for num in [5, 6, 5, 3, 4, 3, 2, 3, 1]:
        t.insert(num)
    print(json.dumps(t.root.to_dict()))