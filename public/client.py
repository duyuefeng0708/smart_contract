import simpy
import json
#import cPickle as pickle
import pickle
from random import seed, randint
#import socket
import sys
from cryptography.fernet import Fernet
import cryptography.hazmat.primitives.asymmetric.rsa as crypt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
import hashlib
import time
# from hashlib import blake2b
import hmac
#from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
#from cryptography.hazmat.primitives.kdf.hkdf import HKDF
#from threading import Thread
import binascii
import struct
import os
import numpy as np
#from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import cProfile
import pstats
import io


filenum = 1000
security = 16

wlist = [[] for i in range(filenum)]
cipher = [[] for i in range(filenum)]

wlist[0] = [b'This', b'You', b'Me', b'OK', b'Jack']
wlist[1] = [b'This', b'Me', b'David', b'OK', b'PP', b"bye"]
indepentwlist = [b'This', b'Me', b'David',
                 b'OK', b'PP', b"bye", b'You', b'Jack', b'David']
indepenttest = []
indepenttestdb = []
filename = 'keywords.txt'
with open(filename, 'rb') as f:
    content = f.readlines()
content = [x.strip() for x in content]
# print(content)
for i in range(len(content)):
    indepenttest.append(content[i])
# print('indepenttest coming thorugh!!!!!!!!!!!!!!!')
# print(indepenttest)
f.close()

filename1 = '30wdb.txt'
with open(filename1, 'rb') as testf:
    line = testf.readlines()
    # print(line)
#    contentf = testf.readlines()
line = [x.strip() for x in line]
# print(line)
count = 0
for i in range(2, filenum, 1):
    for j in range(1000):
        if count == 300 * 1000 -1: 
            count = 0
        wlist[i].append(line[count])
        count = count + 1

K2 = Fernet.generate_key()
# K1 = Fernet.generate_key()
k2 = Fernet(K2)
# k1 = Fernet(K1)
cstar = [[] for i in range(30000)]
# s = [[] for i in range(10)]
count = 0
# print(cstar)
searchhistorty = []
searchtokens = []
tokenhmac = hmac.new(b'k1')
testanswer = []


class Client:
    publicKey = None
    privateKey = None
    checklist = {}

    def __init__(self):

        # for i in range(filenum):
        self.makeToken()
        # print(len(wlist))
        # print(cstar)
        # indexcomplete.succeed()

        return

    def makeToken(self):

        #yield env.timeout(randint(10, 30))
        print('Building add token :) ')
        for fid in range(filenum):
            x = []
            p = struct.pack('i', fid)
            # h_p = hashlib.md5()
            # h_p.update(p)
            cipher[fid].append(k2.encrypt(p))
            for j in range(len(wlist[fid])):
                # print(fid, j, len(wlist[fid]),os.urandom(security))
                # s = [None]*len(wlist[fid])
                Si = os.urandom(security)
                # s[fid].append(Si)
                # print(Si)
                #p = struct.pack('s', wlist[fid][j])
                # stoken = k1.encrypt(p)
                tokenhamgen = tokenhmac.copy()
                to = tokenhamgen.update(wlist[fid][j])
                stoken = tokenhamgen.digest()
                try:
                    h = self.checklist[stoken]
                    h.update(wlist[fid][j])
                except:
                    h = hashlib.md5()
                    h.update(wlist[fid][j])
                self.checklist[stoken] = h
                # print(self.checklist)

                # print(stoken)
                # L = blake2b(key = stoken, digest_size = 10)
                l = hmac.new(stoken)
                # print(l)
                q = struct.pack('s', Si)
                # print(q)
                l.update(q)
                # print(l.digest())
                # l.update(b'Hello')
                # print(l.digest())
                u = l.hexdigest()
                cstar[fid].append(u)
                cstar[fid].append(Si)
                # print(cstar)
                # global count
                # cstar[j][0].append(l)
                # cstar[count][1].append(s[j])
                # count += 1
            token = []
            token.append(fid)
            token.append(cstar[fid])
            print('###############################')
            print('Token generated !! \o/\o/')
            #\      print(fid)
            #print(token)
            # for i in range(len(self.checklist)):
            # print()
            # testanswer = self.checklist[]

        #indexcomplete.succeed()
        #np.savez('fileindex.npz', cstar)
        with open('fileindex100.p', 'wb') as handle:
            pickle.dump(cstar, handle, protocol=pickle.HIGHEST_PROTOCOL)




pr = cProfile.Profile()
pr.enable()
ss = Client()
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
