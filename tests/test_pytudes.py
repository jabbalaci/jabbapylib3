"""
From Peter Norvig's pytudes repository.
Original location: https://github.com/norvig/pytudes/blob/master/ipynb/Advent%202017.ipynb
"""

import math

from jplib import pytudes


def test_pytudes():
    "Tests for the utility functions."
    assert(len(pytudes.letters) == 26)

    # Functions for Input, Parsing
    assert pytudes.Array('''1 2 3
                            4 5 6''') == ((1, 2, 3),
                                          (4, 5, 6))
    assert pytudes.Vector('testing 1 2 3.') == ('testing', 1, 2, 3.0)
    assert pytudes.Integers('test1 (2, -3), #4') == (2, -3, 4)
    assert pytudes.Atom('123.4') == 123.4 and pytudes.Atom('x') == 'x'

    # Functions on Iterables
    assert pytudes.cat(pytudes.upto('abcdef', 'd')) == 'abcd'
    assert pytudes.cat(['do', 'g']) == 'dog'
    assert pytudes.groupby([-3, -2, -1, 1, 2], abs) == {1: [-1, 1], 2: [-2, 2], 3: [-3]}
    assert list(pytudes.grouper(range(8), 3)) == [(0, 1, 2), (3, 4, 5), (6, 7, None)]
    assert list(pytudes.overlapping((0, 1, 2, 3, 4), 3)) == [(0, 1, 2), (1, 2, 3), (2, 3, 4)]
    assert list(pytudes.overlapping('abcdefg', 4)) == ['abcd', 'bcde', 'cdef', 'defg']
    assert list(pytudes.pairwise((0, 1, 2, 3, 4))) == [(0, 1), (1, 2), (2, 3), (3, 4)]
    assert pytudes.join(range(5)) == '01234'
    assert pytudes.join(range(5), ', ') == '0, 1, 2, 3, 4'
    assert pytudes.transpose(((1, 2, 3), (4, 5, 6))) == ((1, 4), (2, 5), (3, 6))
    assert pytudes.ints(1, 100) == range(1, 101)
    assert pytudes.identity('anything') == 'anything'
    assert set(pytudes.powerset({1, 2, 3})) == { (), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3) }
    assert pytudes.quantify(['testing', 1, 2, 3, int, len], callable) == 2  # int and len are callable
    assert pytudes.quantify([0, False, None, '', [], (), {}, 42]) == 1  # Only 42 is truish
    assert set(pytudes.shuffled('abc')) == set('abc')

    # Functional programming
    assert pytudes.mapt(math.sqrt, [1, 9, 4]) == (1, 3, 2)
    assert pytudes.map2d(abs, ((1, -2, -3), (-4, -5, 6))) == ((1, 2, 3), (4, 5, 6))

    # Making immutable objects
    assert pytudes.Set([1, 2, 3, 3]) == {1, 2, 3}
    assert pytudes.canon('abecedarian') == 'aaabcdeeinr'
    assert pytudes.canon([9, 1, 4]) == pytudes.canon({1, 4, 9}) == (1, 4, 9)

    # Math
    assert pytudes.transpose([(1, 2, 3), (4, 5, 6)]) == ((1, 4), (2, 5), (3, 6))
    assert pytudes.ints(1, 5) == range(1, 6)
    assert list(pytudes.floats(1, 5)) == [1., 2., 3., 4., 5.]
    assert pytudes.multiply(pytudes.ints(1, 10)) == math.factorial(10) == 3628800
