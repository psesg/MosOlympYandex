import sys
import os
import logging
from collections import deque
fromfile = False
original_stdin = sys.stdin

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)  # DEBUG, CRITICAL

my_input_file = os.path.join(os.getcwd(), "task_E.txt")
if os.path.exists(my_input_file):
    # file exists
    logging.info("will take data from {}".format(my_input_file))
    fin = open(my_input_file, "r")
    sys.stdin = fin
    fromfile = True
else:
    logging.info("will take data from {}".format("stdin"))

nset = int(sys.stdin.readline().strip("\n"))
for cur_set in range(nset):
    ncom = int(sys.stdin.readline().strip("\n"))
    for cur_com in range(ncom):
        com = sys.stdin.readline().strip("\n")
        print(com)
        
if fromfile:
    sys.stdin = original_stdin  # Change the standard output to the file we created.
    fin.close()