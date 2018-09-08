
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
import pstats
import io
import sethash
from collections import Counter, defaultdict


#filenum = 1000
security = 16

wlist = [[] for i in range(200000)]
cipher = [[] for i in range(200000)]

 
################################# UPDATED1



#K should be randomly generated, but here we use a fixed string instead.    

    
#store label (pointing to each keyword-file pair) and corresponding encrypted file id.
    #L_label = {}   


def file_index (parent, filename, file_id):
    file_path = os.path.join(parent, filename)
    
    with open(file_path, 'rb') as inputfile:
        raw_content = inputfile.read()

    spli = raw_content.split()
    keywords = list(set(spli))
#   print 'keywords: ', keywords
    
    global counter
    
    #store label (pointing to each keyword-file pair) and corresponding encrypted file id, and random strings.
    #L_label = [[] for row in range(len(keywords))]
    for word in keywords:
        #print(word)
        wlist[file_id].append(word.strip())
#           print 'counter is', counter, 'file id is', file_id,  'index_matrix', index_matrix[counter]
            

def index (rootdir):
    sep = '_'
    filenum = 1
    
    pairnum =0
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            file_index (parent, filename, filenum)
            print ('filename is: ', filename, '  file id is: ', filenum)
            filenum += 1
    return filenum


#################################




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
sethh = []


class Client:
    publicKey = None
    privateKey = None
    checklist = {}

    def __init__(self, num):

        # for i in range(filenum):
        filenum = num
        self.makeToken(filenum)
        # print(len(wlist))
        # print(cstar)
        # indexcomplete.succeed()

        return


    def makeToken(self, filenum):

        #yield env.timeout(randint(10, 30))
        print('Building add token :) ')
        for fid in range(filenum):
            #print(fid)
            x = []
            p = struct.pack('i', fid)
            # h_p = hashlib.md5()
            # h_p.update(p)
            cipher[fid].append(k2.encrypt(p))
            flag =0
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
                if wlist[fid][j] in self.checklist:
                    h = self.checklist[wlist[fid][j]]
                    h = sethash.Sethashadd(h,str(fid))
                    self.checklist[str(wlist[fid][j])] = h
                    #if wlist[fid][j] == b'fee,':
                    #    print ("surpise")
                    #print(h)
                else:
                    mappin = {}
                    cntest = Counter()
                    cntest.update([str(fid)])
                    #print(cntest)
                    #print(cntest)
                    mappin = sethash.Verification(cntest)
                    h=sethash.Sethash(mappin.values())
                    self.checklist[str(wlist[fid][j])] = h
                    if (flag ==0):
                        sethh.append(h)
                        flag =1
                    #if wlist[fid][j] == b'presents':
                    #    print (cntest, fid, h, "ddddddddddddddddddddddddddddddddddddddddddddddddd")
                    #print(h)

                    #h = hashlib.md5()
                    #h.update(wlist[fid][j])
                
                
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
            #print('###############################')
            #print('Token generated !! \o/\o/')
            #\      print(fid)
            #print(token)
            # for i in range(len(self.checklist)):
            # print()
            # testanswer = self.checklist[]

        #indexcomplete.succeed()
        print("File index is built! :)")
        #np.savez('fileindex.npz', cstar)
        with open('fileindex-demo.p', 'wb') as handle:
            pickle.dump(cstar, handle, protocol=pickle.HIGHEST_PROTOCOL)
        handle.close()
        hasher = hashlib.md5()
        with open('fileindex-demo.p', 'rb') as hashing:
            buf = hashing.read()
            hasher.update(buf)
       
        hashing.close()

        with open('indexdigest_client.json', 'w') as indexa:
            json.dump(hasher.hexdigest(), indexa)
        indexa.close()
        sethashres = '['+','.join(str(i) for i in sethh)
        sethashres = sethashres+']'
        print("The set hash is:", sethashres)
        with open('sethash_client.json', 'w') as setg:
            json.dump(sethashres, setg)
        #print(len(sethh))
        setg.close()

        print("The index digest is:", hasher.hexdigest())

        #print("The set hash is:", sethh, sep='')
        #print("The set hash is:", h)
            #pickle.dump(cstar, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('checklist.json', 'w') as ccc:
            json.dump(self.checklist, ccc, indent=4)
        ccc.close()
        


if __name__ == '__main__':
#    print 'argv[0]: ', sys.argv[0]
#    print 'argv[1]: ', sys.argv[1]
    rootdir = os.path.join(os.getcwd(), 'db', sys.argv[1])
    num=index(rootdir)
    with open('fid.p', 'wb') as pid:
        pickle.dump(num, pid)
    pid.close()
    ss = Client(num)
    #print(ss.checklist)
