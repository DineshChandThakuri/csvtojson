import csv
import json


class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []

    def child(self, cname):
        child_found = [c for c in self.children if c.name == cname]
        if not child_found:
            _child = Node(cname)
            self.children.append(_child)
        else:
            _child = child_found[0]
        return _child

    def as_dict(self):
        res = {'name': self.name}
        res['children'] = [c.as_dict() for c in self.children]
        return res


root = Node('life')

with open('data_trial.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        grp1, grp2 = row
        root.child(grp2).child(grp1)

print (json.dumps(root.as_dict(), indent=4))
