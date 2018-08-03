# -*- coding: utf-8 -*-


def solution(N):
    s = bin(N)[2:]

    gap = 0
    temp = 0

    for i in s:
        if i == '0':
            gap += 1

        if i == '1':
            if gap > temp:
                temp = gap

            gap = 0

    return temp
