################################################################################
# Description: Number of ways one can make n steps with 1, 2, 3 ,...k steps
# Author: Dr. Sandeep Vidyapu <sandy.apj911@gmail.com>
# Last Modified Date: 25.10.2022
###############################################################################

def num_ways(n, k):
    """
    returns the number of ways one can make n steps by taking at most k steps at a time
    """
    n_ways = [0]*(k+1) # for the initial 0, 1, 2, ..., k total steps
    for i in range(n+1): #always sum the last k values in the array to compute the next value
        if i <= 1: #for the first step
            n_ways[i] = i
        elif i <= k:
            n_ways[i] = sum(n_ways[:i])+1
        else:
            n_ways.append(sum(n_ways[i-k:]))
        print(f"Number of ways to make a total of {i} steps by making at most {k} steps is: {n_ways[i]}")


if __name__ == "__main__":
    n = 127 #Total number of steps to make
    k = 3 #maximum number of steps one can make at a time
    num_ways(n, k)
