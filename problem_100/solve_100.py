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


def solve_100_brute_force(max_n):
    """
    """
    for n in range(3, max_n):
        b = blue_disks(n)
        p = prob_of_bb(n, b)
        if p == .5:
            print('n: {}, b: {}, p: {}'.format(n, b, p))
            if n >= 10**12:
                print('Project Euler Problem #100 Solution: {} blue disks'.format(b))


def time_brute_force():
    """
    """
    t0 = time.time()
    max_n_exp = 7
    max_n = 10**max_n_exp
    solve_100_brute_force(max_n)
    t1 = time.time()
    t_delta = t1 - t0
    print('brute force solution up to max_n: 10**{}, took: {} seconds'.format(max_n_exp, int(t_delta)))


def solve_100():
    """
    using the brute force generated sequence of valid `n` values:
    https://oeis.org/search?q=4%2C+21%2C+120%2C+697%2C+4060%2C+23661%2C+137904%2C+803761%2C+4684660%2C+27304197&language=english&go=Search
    """
    n_candidates = [4, 21, 120, 697, 4060, 23661, 137904, 803761, 4684660, 27304197, 159140520, 927538921, 5406093004, 31509019101, 183648021600, 1070379110497, 6238626641380, 36361380737781, 211929657785304, 1235216565974041]
    for n in n_candidates:
        b = blue_disks(n)
        if (prob_of_bb(n, b) == .5) and (n >= 10**12):
            print('Project Euler Problem #100 Solution: {} blue disks'.format(b))
            break



def main():
    """
    """
    test_blue_disks()
    test_prob_of_bb()
    time_brute_force()
    solve_100()



if __name__ == "__main__":
    main()

