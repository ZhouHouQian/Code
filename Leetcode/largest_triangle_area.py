#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-09-23 21:14:49
# @Author  : houqianzhou
# @Desc    : https://leetcode.cn/problems/largest-triangle-area/

from typing import List


class Solution:
    def getConvexHull(self, points: List[List[int]]) -> List[List[int]]:
        points.sort()
        stack1 = list(points[:2])
        for point in points[2:]:
            while len(stack1) >= 2:
                a = (stack1[-1][0] - stack1[-2][0], stack1[-1][1] - stack1[-2][1])
                b = (point[0] - stack1[-1][0], point[1] - stack1[-1][1])
                if a[0] * b[1] - a[1] * b[0] <= 0:
                    stack1.pop()
                else:
                    break
            stack1.append(point)
        stack2 = list(points[-1:-3:-1])
        for point in points[-3::-1]:
            while len(stack2) >= 2:
                a = (stack2[-1][0] - stack2[-2][0], stack2[-1][1] - stack2[-2][1])
                b = (point[0] - stack2[-1][0], point[1] - stack2[-1][1])
                if a[0] * b[1] - a[1] * b[0] <= 0:
                    stack2.pop()
                else:
                    break
            stack2.append(point)
        return stack1[:-1] + stack2[:-1]

    def triangleArea(self, p1, p2, p3):
        return abs(p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p1[1] * p2[0] - p2[1] * p3[0] - p3[1] * p1[0]) / 2

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        convex_hull = self.getConvexHull(points)
        result = 0
        for i in range(len(convex_hull) - 2):
            k = i + 2
            for j in range(i + 1, len(convex_hull) - 1):
                current_area = self.triangleArea(convex_hull[i], convex_hull[j], convex_hull[k])
                while k + 1 < len(convex_hull):
                    next_area = self.triangleArea(convex_hull[i], convex_hull[j], convex_hull[k + 1])
                    if current_area > next_area:
                        break
                    k += 1
                    current_area = next_area
                result = max(result, current_area)
        return result


if __name__ == "__main__":
    print(Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
    print(Solution().largestTriangleArea([[37,48],[44,48],[-35,36],[-48,-31],[4,-49],[25,11],[31,-13],[-4,32],[2,-3],[-10,2],[33,-22],[-42,8],[-28,-19],[-28,19],[-8,-10],[-13,37],[-16,-49],[25,38],[42,-9],[35,48],[49,47],[-5,-39],[-5,-28],[-30,32],[47,24]]))