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
    my_output_file = "e2_output.txt"
    original_stdout = sys.stdout  # Save a reference to the original standard output
    fout = open(my_output_file, "w")
    sys.stdout = fout  # Change the standard output to the file we created.


my_input_file = os.path.join(os.getcwd(), "e2.txt")

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
    is_stack = True
    is_queue = True
    qu = deque()
    st = deque()
    for cur_com in range(ncom):
        com = sys.stdin.readline().strip("\n")
        coms = com.split(sep=" ")
        if coms[0] == "push":
            qu.appendleft(int(coms[1]))
            st.append(int(coms[1]))
        if coms[0] == "pop":
            if qu.pop() != int(coms[1]):
                is_queue = False
            if st.pop() != int(coms[1]):
                is_stack = False
        #print(coms[0], coms[1])
    if is_stack and is_queue:
        print("both")
    elif is_stack:
        print("stack")
    elif is_queue:
        print("queue")
    else:
        print("none")

if fromfile:
    sys.stdin = original_stdin  # Change the standard input to the file we created.
    fin.close()

if tofile:
    sys.stdout = original_stdout  # Change the standard output to the file we created.
    fout.close()