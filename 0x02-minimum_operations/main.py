#!/usr/bin/env python3
"""test the min ops func
"""
min_ops = __import__('0-minoperations').minOperations

if __name__ == "__main__":
    print(f"the min operations is {min_ops(15)}")
    assert min_ops(1) == 0
    assert min_ops(2) == 2
    assert min_ops(3) == 3
    assert min_ops(4) == 4
    assert min_ops(5) == 5
    assert min_ops(6) == 5
    assert min_ops(7) == 7
    assert min_ops(8) == 6
    assert min_ops(9) == 6
    assert min_ops(10) == 7
    assert min_ops(11) == 11
    assert min_ops(12) == 7
    assert min_ops(13) == 13
    assert min_ops(14) == 9
    # assert min_ops(15) == 5
    assert min_ops(16) == 8
    assert min_ops(17) == 17
    assert min_ops(18) == 8
    assert min_ops(19) == 19
    assert min_ops(20) == 9
