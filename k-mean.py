import collections
from idlelib.multicall import r
from collections import Counter
import itertools
from itertools import chain
from itertools import permutations
from random import uniform
from tkinter import *
from itertools import *
import imaplib
import pandas as pd
import numpy as np
import xlrd
import csv
import math
import sys
from random import shuffle, uniform

# The implementation


items = []
items = list(map(int, items))


# Pre-Processing
def ReadData(fileName):
    file = open("Absenteeism_at_work1.csv")
    num_lines = len(file.readlines())
    with open(fileName, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # for header skip
        line = next(csv_reader)
        items.append(line)
    itemFeatures = []
    len(line)
    for j in range(len(line)):
        v = float(line[j])  # Convert feature value to float
        itemFeatures.append(v)  # Add feature value to dict
        items.append(itemFeatures)

    shuffle(items)

    return items


# Auxiliary Function_
def FindColMinMax(items):
    n = len(items[0])
    minima = [sys.maxsize for i in range(n)]
    maxima = [-sys.maxsize - 1 for i in range(n)]

    for item in items:
        for f in range(len(item) - 1):
            if int((item[f])) < minima[f]:
                minima[f] = int(float(item[f]))

            if int(float(item[f])) > maxima[f]:
                maxima[f] = int(float(item[f]))

    return minima, maxima


def EuclideanDistance(x, y):
    S = 0  # The sum of the squared differences of the elements
    for i in range(len(x) - 1):
        S += math.pow(int(x[i]) - y[i], 2)

    return math.sqrt(S)  # The square root of the sum


def InitializeMeans(items, k, cMin, cMax):
    # Initialize means to random numbers between
    # the min and max of each column/feature

    f = len(items[0])  # number of features
    means = [[0 for i in range(f)] for j in range(k)]

    for mean in means:
        for i in range(len(mean)):
            # Set value to a random float
            # (adding +-1 to avoid a wide placement of a mean)
            mean[i] = uniform(cMin[i] + 1, cMax[i] - 1)

    return means


def UpdateMean(n, mean, item):
    for i in range(len(mean) - 1):
        m = mean[i]
        m = (m * (n - 1) + float(item[i])) / float(n)
        mean[i] = round(m, 3)

    return mean


# Core Functions
def FindClusters(means, items):
    clusters = [[] for i in range(len(means))]  # Init clusters

    for item in items:
        # Classify item into a cluster
        index = Classify(means, item)

        # Add item to cluster
        clusters[index].append(item)

    return clusters


def Classify(means, item):
    # Classify item to the mean with minimum distance

    minimum = sys.maxsize
    index = -1

    for i in range(len(means)):
        # Find distance from item to mean
        dis = EuclideanDistance(item, means[i])

        if dis < minimum:
            minimum = dis
            index = i

    return index


def CalculateMeans(k, items, maxIterations=100000):
    # Find the minima and maxima for columns
    cMin, cMax = FindColMinMax(items)

    # Initialize means at random points
    means = InitializeMeans(items, k, cMin, cMax)

    # Initialize clusters, the array to hold
    # the number of items in a class
    clusters = [0 for i in range(len(means))]

    # An array to hold the cluster an item is in
    belongsTo = [0 for i in range(len(items))]

    # Calculate means
    # If no change of cluster occurs, halt
    clusters = [0 for i in range(len(means))]
    for i in range(len(items)):
        item = items[i]
        # Classify item into a cluster and update the
        # corresponding means.
        index = Classify(means, item)

        clusters[index] += 1
        means[index] = UpdateMean(clusters[index], means[index], item)

    return means


item = list(map(int, items))


def main():
    data = ReadData('Absenteeism_at_work1.csv')
    k = 2
    means = CalculateMeans(k, data)
    print("Means = ", means)

    clusters = FindClusters(means, data)
    print("Clusters: ", clusters)


if __name__ == "__main__":
    main()
