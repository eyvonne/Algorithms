#!/usr/bin/python

import sys


def rock_paper_scissors(n):

    if n == 1:
        return ['rock', 'paper', 'scissors']
    elif n % 2 == 0:
        return 'paper'
    elif n % 1 == 0:
        return 'scissors'

    for i in range(n):
        return [rock_paper_scissors(n-1)]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
