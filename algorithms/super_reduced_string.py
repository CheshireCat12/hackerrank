# Super Reduced String

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    tmp_s = None

    while s != tmp_s:
        tmp_s = s
        s = re.sub(r'(\w)\1', r'', s)

    return s or "Empty String"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

