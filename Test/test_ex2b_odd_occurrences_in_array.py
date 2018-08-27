# -*- coding: utf-8 -*-

from Lessons.ex2b_odd_occurrences_in_array import solution
from random import randint


def test_simple_array():
    assert solution([9, 3, 9, 3, 9, 7, 9]) == 7


def test_complex_array():
    A = []
    length = int(1000000 / 2)

    for i in range(length):
        A.append(randint(0, 1000000000))

    A = list(set(A)) * 2
    A.append(A[0])

    assert solution(A) == A[0]
