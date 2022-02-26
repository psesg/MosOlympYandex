import sys
import os
import logging
from collections import deque

fromfile = False
tofile = False
original_stdin = sys.stdin

logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)  # DEBUG, CRITICAL

tofile = False
if tofile:
    my_output_file = "a_output.txt"
    original_stdout = sys.stdout  # Save a reference to the original standard output
    fout = open(my_output_file, "w")
    sys.stdout = fout  # Change the standard output to the file we created.

my_input_file = os.path.join(os.getcwd(), "a_in.txt")

if os.path.exists(my_input_file):
    # file exists
    logging.info("will take data from {}".format(my_input_file))
    fin = open(my_input_file, "r")
    sys.stdin = fin
    fromfile = True
else:
    logging.info("will take data from {}".format("stdin"))


def getremain(r):
    a = [4, 5, 2, 3, 3, 1, 5, 4, 1, 2]
    return sum(a[:r])

def getcount(number):
    count = 0
    div = 10
    deep = 1
    while number // div >= 1:
        print("- ", deep, div, number // div)
        div *= 10
        deep += 1


ncount = int(sys.stdin.readline().strip("\n"))
for cur_set in range(ncount):
    count = int(sys.stdin.readline().strip("\n"))
    if count == 0:
        print(0)
    elif count > 0 and count < 10:
        print(getremain(count))
    else:
        print(getcount(count))

if fromfile:
    sys.stdin = original_stdin  # Change the standard input to the file we created.
    fin.close()

if tofile:
    sys.stdout = original_stdout  # Change the standard output to the file we created.
    fout.close()
