import sys
import os
import logging
from collections import deque

fromfile = False

original_stdin = sys.stdin

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)  # DEBUG, CRITICAL

tofile = True
if tofile:
    my_output_file = "d0_output.txt"
    original_stdout = sys.stdout  # Save a reference to the original standard output
    fout = open(my_output_file, "w")
    sys.stdout = fout  # Change the standard output to the file we created.

my_input_file = os.path.join(os.getcwd(), "d0.txt")

if os.path.exists(my_input_file):
    # file exists
    logging.info("will take data from {}".format(my_input_file))
    fin = open(my_input_file, "r")
    sys.stdin = fin
    fromfile = True
else:
    logging.info("will take data from {}".format("stdin"))

cntrlst = []
voc = {}
nset = int(sys.stdin.readline().strip("\n"))
logging.info("nset={}".format(nset))
for cur_set in range(nset):
    temp = sys.stdin.readline().strip("\n")
    tempar = temp.split(sep=' ')
    n_mag = int(tempar[0])
    m_ware = int(tempar[1])
    logging.info("n_mag={}, m_ware={}".format(n_mag, m_ware))
    temp = sys.stdin.readline().strip("\n")
    temp = temp.strip()
    n_delcost = temp.split(sep=' ', maxsplit=n_mag)
    n_delcost = list(map(int, n_delcost))
    logging.info("n_delcost={}".format(n_delcost))
    cost_m_ware_in_n_mag = []
    for i in range(m_ware):
        temp = sys.stdin.readline().strip("\n")
        temp = temp.strip()
        cost = temp.split(sep=' ', maxsplit=n_mag)
        cost = list(map(int, cost))
        cost_m_ware_in_n_mag.append(cost)
    logging.info("cost_m_ware_in_n_mag={}".format(cost_m_ware_in_n_mag))

    voc.clear()
    for i in range(n_mag):
        cntrlst.clear()
        for j in range(m_ware):
            logging.info("cntrlst.append i={} j={} {}+{}".format(i, j, n_delcost[i], cost_m_ware_in_n_mag[j][i]))
            cntrlst.append(n_delcost[i] + cost_m_ware_in_n_mag[j][i])
        logging.info(" voc.update ind={} min={}".format(cntrlst.index(min(cntrlst)),min(cntrlst) ))
        voc.update({cntrlst.index(min(cntrlst)): min(cntrlst)})
    for keys, values in voc.items():
        logging.info("keys={}, values={}".format(keys, values))

if fromfile:
    sys.stdin = original_stdin  # Change the standard input to the file we created.
    fin.close()

if tofile:
    sys.stdout = original_stdout  # Change the standard output to the file we created.
    fout.close()