import sys
import os
import logging
from collections import deque

fromfile = False

original_stdin = sys.stdin

logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)  # DEBUG, CRITICAL

tofile = True
if tofile:
    my_output_file = "b2_output.txt"
    original_stdout = sys.stdout  # Save a reference to the original standard output
    fout = open(my_output_file, "w")
    sys.stdout = fout  # Change the standard output to the file we created.

my_input_file = os.path.join(os.getcwd(), "b2.txt")

if os.path.exists(my_input_file):
    # file exists
    logging.info("will take data from {}".format(my_input_file))
    fin = open(my_input_file, "r")
    sys.stdin = fin
    fromfile = True
else:
    logging.info("will take data from {}".format("stdin"))


ncount = int(sys.stdin.readline().strip("\n"))
for cur_set in range(ncount):
    temp = sys.stdin.readline().strip("\n")
    logging.info("temp = {}".format(temp))
    tempar = temp.split(sep='\t')
    cost = int(tempar[0])
    deliverycost = int(tempar[1])
    freedelivery = int(tempar[2])
    if cost >= deliverycost + freedelivery:
        print(cost)
    elif freedelivery > cost + deliverycost:
        print(cost + deliverycost)
    elif cost < deliverycost + freedelivery:
        print(deliverycost + freedelivery - 1)
    else:
        print(cost + deliverycost - 1)
if fromfile:
    sys.stdin = original_stdin  # Change the standard input to the file we created.
    fin.close()

if tofile:
    sys.stdout = original_stdout  # Change the standard output to the file we created.
    fout.close()