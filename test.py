import os
import pprint
from csv2json import csv2json

DATADIR = ""
DATAFILE = "beatles-diskography.csv"
DATAFILE1 = "test1.csv"
DATAFILE2 = "test2.csv"
DATAFILE3 = "test3.csv"
DATAFILE4 = "test4.csv"

print "---------------DATAFILE1---------------"
datafile = os.path.join(DATADIR, DATAFILE)
d = csv2json(datafile)
pprint.pprint(d)
print "---------------DATAFILE1---------------"
datafile = os.path.join(DATADIR, DATAFILE1)
d = csv2json(datafile)
pprint.pprint(d)
print "---------------DATAFILE2---------------"
datafile = os.path.join(DATADIR, DATAFILE2)
d = csv2json(datafile)
pprint.pprint(d)
print "---------------DATAFILE3---------------"
datafile = os.path.join(DATADIR, DATAFILE3)
d = csv2json(datafile)
pprint.pprint(d)
print "---------------DATAFILE4---------------"
datafile = os.path.join(DATADIR, DATAFILE4)
d = csv2json(datafile)
pprint.pprint(d)
print "------------------------------"
