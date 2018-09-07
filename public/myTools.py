#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import re
import pickle
import datetime
import os
import sys

enc_pattern = re.compile(r'.*\.enc$')
dec_pattern = re.compile(r'.*\.dec$')
pickle_pattern = re.compile(r'.*\.dec$')


def CalcSha1(word):
    sha1obj = hashlib.sha1()
    sha1obj.update(word)
    hash = sha1obj.hexdigest()
    return hash

def CalcSha256(word):
    sha256obj = hashlib.sha256()
    sha256obj.update(word)
    hash = sha256obj.hexdigest()
    return hash
	


def CalcMD5(word):
    md5obj = hashlib.md5()
    md5obj.update(word)
    hash = md5obj.hexdigest()
    return hash


def sxor(s1, s2):
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(s1, s2))


def GetDataDict():
    try:
        with open('mydata.pickle', 'rb') as input:
            data_dict = pickle.load(input)
    except:
        data_dict = {}
        print ('Unable to open mydata.pickle!')
    return data_dict


def GetUserName():
    data_dict = GetDataDict()

    return data_dict.get('username', 'Unset')


def SetUserName(username):
    data_dict = GetDataDict()

    data_dict['username'] = username

    with open('mydata.pickle', 'wb') as output:
        pickle.dump(data_dict, output)


def GetLastGenTime():
    data_dict = GetDataDict()
    return data_dict.get('last_gen_time', 'never gen')


def SetLastGenTime(last_gen_time):
    data_dict = GetDataDict()

    data_dict['last_gen_time'] = last_gen_time

    with open('mydata.pickle', 'wb') as output:
        pickle.dump(data_dict, output)


def GetNowString():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')



if len(sys.argv) == 2:
    print("\n#################################")
    print("# Cyclic Group Generator Finder #")
    print("#################################\n")
    print("Usage  : " + sys.argv[0] + " debug (optional) [group list] (required)")
    print("Usage  : " + sys.argv[0] + " debug (optional) [Z order] (required)\n")
    print("Example: " + sys.argv[0] + " debug 1 2 3 4")
    print("Example: " + sys.argv[0] + " debug 5\n")
    # sys.exit(0)

# init
'''
def checkIfNumberIsGenerator(cyclicGroup,number):
    # if showLogs:
        # print ("testing number: " + str(number))
    accum = int(number)
    for cycle in range(1, len(cyclicGroup) + 1):
        # if showLogs:
            # print ("    ("+ str(cycle) +") accum: " + str(accum))
        accum = (int(accum) * int(number)) % (len(cyclicGroup) + 1)
        auxCyclicGroup.append(accum)
        # if showLogs:
            # print ("    cic: " + str(auxCyclicGroup))
    auxCyclicGroup.sort()
    return collections.Counter(cyclicGroup) == collections.Counter(auxCyclicGroup)

for number in cyclicGroup:
    auxCyclicGroup = []
    if checkIfNumberIsGenerator(number):
        print ("  Number " + str(number) + " is generator!")
'''
