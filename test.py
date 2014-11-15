#!/usr/bin/env python

class Solution:
    def __init__(self):
        pass
    
    def solve(self):
        pass

# utility function for input
def read_line():
    line = raw_input()
    line = line.strip()
    return line

def read_strs():
    line = read_line()
    strs = line.split(' ')
    return strs

def read_numbers():
    nums = read_strs()
    for i in xrange(len(nums)):
        nums[i] = int(nums[i])
    return nums

def runtest():
    pass

def runtests():
    num_tests = read_numbers()[0]
    for i in xrange(num_tests):
        runtest()

# if __name__ == "__main__":
if __name__ == "__test__":
    runtests()

# if __name__ == "__test__":
if __name__ == "__main__":
    infile = open("in.txt", 'r')
    import sys
    sys.stdin = infile
    runtests()
    infile.close()
    