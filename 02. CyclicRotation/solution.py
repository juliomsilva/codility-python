# -*- coding: utf-8 -*-


def solution(A, K):
    length = len(A)

    for i in range(K):
        last = A[-1]

        for j in range(length-1, -1, -1):
            if j == 0:
                A[0] = last
            else:
                A[j] = A[j-1]

    return A
