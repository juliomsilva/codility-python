# -*- coding: utf-8 -*-


from Lessons.ex1_binary_gap import solution


def test_solution():
    assert solution(2147483647) == 0
    assert solution(214748364) == 2
    assert solution(21474836) == 4
    assert solution(2147483) == 5
    assert solution(214748) == 3
    assert solution(21474) == 3
    assert solution(2147) == 4
    assert solution(214) == 1
    assert solution(21) == 1
    assert solution(2) == 0
