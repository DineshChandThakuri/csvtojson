import csv
import json
from collections import defaultdict

""" Function to create dynamic tree"""
def ctree():
    return defaultdict(ctree)

""" Recursive function to build  custom tree structure"""
def build_leaf(name, leaf):

    res = {"name" :name}

    # add children node if the leaf actually has any children
    if len(leaf.keys()) > 0:
        res["children"] = [build_leaf(k, v) for k, v in leaf.items()]

    return res


def main():

    tree = ctree()
    # NOTE: you need to have test.csv file as neighbor to this file
    with open('trial2.csv') as csvfile:
        reader = csv.reader(csvfile)
        for rid, row in enumerate(reader):

            # skipping top header row
            if rid == 0:
                continue

            # grouping csv values under their parents and creating dynamic structure
            leaf = tree[row[0]]
            for cid in range(1, len(row)):
                leaf = leaf[row[cid]]

    # building a custom tree structure
    res = []
    for name, leaf in tree.items():
        res.append(build_leaf(name, leaf))

    # printing results into the terminal
    
    print(json.dumps((res), indent=4))

main()
