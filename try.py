import csv
import json


with open('data_trial.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    x=0
    y=0
    superparent=[]
    parent = []
    item = []
    for row in reader:
        grp1, grp2 = row
        parent.append(grp2)
        item.append(grp1)
        y=y+1
        if(grp2=='Null'):
            superparent.append(grp1)
            x=x+1
i=0
root = []
while(i<y):
    count=0
    j=i
    while(j<(y-1)):
        if(parent[i]==parent[j+1]):
            count=count+1
        j=j+1
    if(count==0):
        root.append(parent[i])
    i=i+1
    
