#!/usr/bin/env python
# coding: utf-8
"""
"""


import time


def blue_disks(n):
    """
    """
    return int(n*2** - .5) + 1


def test_blue_disks():
    """
    """
    assert 15 == blue_disks(21)
    assert 85 == blue_disks(120)


def prob_of_bb(n, b):
    """
    """
    return (b**2 - b) / (n**2 - n)


def test_prob_of_bb():
    """
    """
    assert .5 == prob_of_bb(21, 15)
    assert .5 == prob_of_bb(120, 85)


def solve_100(max_n):
    """
    """
    for n in range(3, max_n):
        b = blue_disks(n)
        p = prob_of_bb(n, b)
        if p == .5:
            #print('n: {}, b: {}, p: {}'.format(n, b, p))
            #print(n)
            print(b)
            if n >= 10**12:
                print('Project Euler Problem #100 Solution: {} blue disks'.format(b))


def brute_force():
    """
    """
    t0 = time.time()
    max_n_exp = 7
    max_n = 10**max_n_exp
    solve_100(max_n)
    t1 = time.time()
    t_delta = t1 - t0
    print('brute force solution up to max_n: 10**{}, took: {} seconds'.format(max_n_exp, int(t_delta)))


def main():
    """
    """
    test_blue_disks()
    test_prob_of_bb()
    brute_force()



if __name__ == "__main__":
    main()

