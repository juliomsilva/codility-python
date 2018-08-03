# -*- coding: utf-8 -*-

from solution import solution


def test_solution_1_rotation():
    assert solution([0, 0, 0], 1) == [0, 0, 0]
    assert solution([3, 8, 9, 7, 6], 1) == [6, 3, 8, 9, 7]
    assert solution([6, 3, 8, 9, 7], 1) == [7, 6, 3, 8, 9]
    assert solution([7, 6, 3, 8, 9], 1) == [9, 7, 6, 3, 8]


def test_solution_4_rotations():
    assert solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]


def test_solution_empty_array():
    assert solution([], 1) == []
