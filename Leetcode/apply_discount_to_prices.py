#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-09-22 15:33:37
# @Author  : houqianzhou
# @Desc    : 

class Solution:
    def replace(self, word: str, discount: int) -> str:
        if word[0] != "$" or len(word) == 1:
            return word
        for char in word[1:]:
            if char not in "0123456789":
                return word
        return "${:.2f}".format(int(word[1:]) * (100 - discount) / 100)

    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(" ")
        for i, word in enumerate(words):
            words[i] = self.replace(word, discount)
        return " ".join(words)