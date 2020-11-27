#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):

    # lines 15 - 17 I wrote
    person = s.split(" ")
    proper_name = [name.capitalize() for name in person]
    return " ".join(proper_name)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
