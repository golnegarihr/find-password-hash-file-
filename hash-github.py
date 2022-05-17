"""
Created on Sat May  7 22:13:06 2022
 
    load from hash file a list of users and their hash password 
    then create  a dictionary of hash pf numbers from 0000 to 9999
    so finaly compare hash of users by hash of dict after that show 
    of users password that  were entered
@author: @golnegarihr (github)
"""

import csv
import hashlib


dicthash = dict()

for i in range(0, 9999):

    toencode = ('b'+str(i)).encode('utf-8')
    dicthash[i] = hashlib.sha256(toencode).hexdigest()

with open('C:\\Users\\98939\\Desktop\\hashfile.csv') as file:
    read_hash_file = list(csv.reader(file))
    name = list()
    hashcode = list()
    hashans = list()
    j = 0
    for i in read_hash_file:
        name.append((i[0]))
        hashcode.append((i[1]))
        hashans.append((i[2]))
        j += 1

for i in range(len(hashcode)):

    for j in range(0, len(dicthash)):
        a = hashcode[i].strip()
        b = dicthash[j]
        if a == b:
            print(name[j], ' your password is :', j)
