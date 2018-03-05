#!/usr/bin/env python3

"""
The following codes are from Peter Norvig's pytudes repository.
Original location: https://github.com/norvig/pytudes/blob/master/ipynb/Advent%202017.ipynb
"""

import random
import re
from collections import abc, defaultdict, deque
from itertools import chain, combinations, takewhile, zip_longest

letters  = 'abcdefghijklmnopqrstuvwxyz'
cat = ''.join

################ Functions for Input, Parsing

def Array(lines):
    "Parse an iterable of str lines into a 2-D array. If `lines` is a str, splitlines."
    if isinstance(lines, str): lines = lines.splitlines()
    return mapt(Vector, lines)

def Vector(line):
    "Parse a str into a tuple of atoms (numbers or str tokens)."
    return mapt(Atom, line.replace(',', ' ').split())

def Integers(text):
    "Return a tuple of all integers in a string."
    return mapt(int, re.findall(r'-?\b\d+\b', text))

def Atom(token):
    "Parse a str token into a number, or leave it as a str."
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token

################ Functions on Iterables

def upto(iterable, maxval):
    "From a monotonically increasing iterable, generate all the values <= maxval."
    # Why <= maxval rather than < maxval? In part because that's how Ruby's upto does it.
    return takewhile(lambda x: x <= maxval, iterable)

identity = lambda x: x

def groupby(iterable, key=identity):
    "Return a dict of {key(item): [items...]} grouping all items in iterable by keys."
    groups = defaultdict(list)
    for item in iterable:
        groups[key(item)].append(item)
    return groups

def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks:
    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"""
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def overlapping(iterable, n):
    """Generate all (overlapping) n-element subsequences of iterable.
    overlapping('ABCDEFG', 3) --> ABC BCD CDE DEF EFG"""
    if isinstance(iterable, abc.Sequence):
        yield from (iterable[i:i + n] for i in range(len(iterable) + 1 - n))
    else:
        result = deque(maxlen=n)
        for x in iterable:
            result.append(x)
            if len(result) == n:
                yield tuple(result)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    return overlapping(iterable, 2)

def join(iterable, sep=''):
    "Join the items in iterable, converting each to a string first."
    return sep.join(map(str, iterable))

def powerset(iterable):
    "Yield all subsets of items."
    items = list(iterable)
    for r in range(len(items) + 1):
        for c in combinations(items, r):
            yield c

def quantify(iterable, pred=bool):
    "Count how many times the predicate is true."
    return sum(map(pred, iterable))

def length(iterable):
    "Same as len(list(iterable)), but without consuming memory."
    return sum(1 for _ in iterable)

def shuffled(iterable):
    "Create a new list out of iterable, and shuffle it."
    new = list(iterable)
    random.shuffle(new)
    return new

flatten = chain.from_iterable

################ Functional programming

def mapt(fn, *args):
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))

def map2d(fn, grid):
    "Apply fn to every element in a 2-dimensional grid."
    return tuple(mapt(fn, row) for row in grid)

################ Making immutable objects

class Set(frozenset):
    "A frozenset, but with a prettier printer."
    def __repr__(self): return '{' + join(sorted(self), ', ') + '}'

def canon(items, typ=None):
    "Canonicalize these order-independent items into a hashable canonical form."
    typ = typ or (cat if isinstance(items, str) else tuple)
    return typ(sorted(items))

################ Math Functions

def transpose(matrix): return tuple(zip(*matrix))

def ints(start, end, step=1):
    "The integers from start to end, inclusive: range(start, end+1)"
    return range(start, end + 1, step)

def floats(start, end, step=1.0):
    "Yield floats from start to end (inclusive), by increments of step."
    m = (1.0 if step >= 0 else -1.0)
    while start * m <= end * m:
        yield start
        start += step

def multiply(numbers):
    "Multiply all the numbers together."
    result = 1
    for n in numbers:
        result *= n
    return result

################ 2-D points implemented using (x, y) tuples

################ Debugging

def grep(pattern, iterable):
    "Print lines from iterable that match pattern."
    for line in iterable:
        if re.search(pattern, line):
            print(line)

################ A* and Breadth-First Search (tracking states, not actions)
