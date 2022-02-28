import sys
import os
import logging
from collections import deque

fromfile = False

original_stdin = sys.stdin

logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)  # DEBUG, CRITICAL

tofile = True
if tofile:
    my_output_file = "d1_output.txt"
    original_stdout = sys.stdout  # Save a reference to the original standard output
    fout = open(my_output_file, "w")
    sys.stdout = fout  # Change the standard output to the file we created.

my_input_file = os.path.join(os.getcwd(), "d1.txt")

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
    for i in range(m_ware):
        cntrlst.clear()
        for j in range(n_mag):
            logging.info("cntrlst.append i={} j={} {}+{}".format(i, j, n_delcost[j], cost_m_ware_in_n_mag[i][j]))
            cntrlst.append(n_delcost[j] + cost_m_ware_in_n_mag[i][j])
        logging.info(" voc.update i={} ind={} min={}".format(i, cntrlst.index(min(cntrlst)),min(cntrlst) ))
        voc.update({i: str(cntrlst.index(min(cntrlst))) + " " + str(min(cntrlst))})
    logging.info("len(voc)={}".format(len(voc)))
    tmp0 = 0
    tmp1 = 0
    summa = 0
    pos = ""
    for keys, values in voc.items():
        tmp = values.split(' ')
        tmp0 = int(tmp[0])
        tmp1 = int(tmp[1])
        summa += tmp1
        pos += (str(tmp0+1) + ' ')
        logging.info("keys={}, values={}".format(keys, values))
    print("{}\n{}".format(summa, pos.strip()))

if fromfile:
    sys.stdin = original_stdin  # Change the standard input to the file we created.
    fin.close()

if tofile:
    sys.stdout = original_stdout  # Change the standard output to the file we created.
    fout.close()