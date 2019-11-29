import collections
from idlelib.multicall import r
from collections import Counter
import itertools
from itertools import chain
from itertools import permutations
from tkinter import *
from itertools import *
import imaplib
import pandas as pd
import numpy as np
import xlrd
import csv

# The implementation
# df = pd.read_excel(r'D:\CS\projects\k-mean\Absenteeism_at_work.xls')
file = open("Absenteeism_at_work.csv")
percentage = int(input("How many % of records you want to read?"))

num_lines = len(file.readlines())
records = int((percentage / 100) * num_lines)

dataSet = pd.read_csv("Absenteeism_at_work.csv", sep=',', header=0, nrows=records).values
