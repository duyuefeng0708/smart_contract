
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
#from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import pstats
import io
import numpy as np
import sethash
from collections import Counter, defaultdict


filenum = 300
security = 16


# print('indepenttest coming thorugh!!!!!!!!!!!!!!!')
# print(indepenttest)

K2 = Fernet.generate_key()
# K1 = Fernet.generate_key()
k2 = Fernet(K2)
# k1 = Fernet(K1)

# s = [[] for i in range(10)]
count = 0
# print(cstar)
searchhistorty = []
searchtokens = []
tokenhmac = hmac.new(b'k1')
sethh = []



class Service:
    privateKey = None
    publicKey = None
    fileindex = None
    searchindex = {}
    digestindex = {}
    outdigest ={}
    #postinglist = []

    def __init__(self):

        self.processIndex()

    def processIndex(self):

        
        with open('fileindex-demo.p', 'rb') as handle:
            b = pickle.load(handle)
        #self.fileindex = b
        hasher = hashlib.md5()
        with open('fileindex-demo.p', 'rb') as hashing:
            buf = hashing.read()
            hasher.update(buf)
        hashing.close()
        
        print ("Creating files for index digest and sethash ...")
        with open('indexdigest_peer.json', 'w') as indexa:
            json.dump(hasher.hexdigest(), indexa)
        indexa.close()
        # print("The index digest is:", hasher.hexdigest())
        
        #print(b)

        with open('fid.p', 'rb') as dd:
            filenum = pickle.load(dd)
        dd.close()
        for fid in range(filenum):
            mappin = {}
            cntest = Counter()
            cntest.update([str(fid)])
            mappin = sethash.Verification(cntest)
            hm=sethash.Sethash(mappin.values())
            if(fid!=0):
                sethh.append(hm)
        sethashres = '['+','.join(str(i) for i in sethh)
        sethashres = sethashres+']'
        # print("The set hash is:", sethashres)
        print("Contract function call (Storeindex) input:\n","\""+hasher.hexdigest()+"\","+sethashres)
        with open('sethash_peer.json', 'w') as setg:
            json.dump(sethashres, setg)
        #print(len(sethh))
        setg.close()
        #with open('sethash_peer.json', 'w') as setg:
        #    json.dump(sethh, setg)
        #setg.close()
        #print("The set hash is:", hm)

        #self.fileindex = cstar
        
        # with open('searchindex.p', 'ab') as sr:
        #    lists["aaa"] = "bbbb"
        #    print(lists)
        # sr.write(str(lists))
        #    pickle.dump(lists, sr)
        # sr.close()
        # with open('searchindex.p', 'rb') as di:
        #digestlist[token]  = digest
        #data = json.load(di)
        #data = di.read()
        #name = raw_input("> ")
        # for name in data:
        #    print(data[name])
        #    b = pickle.load(di)
        #    print('--------------', b)
        #    b = pickle.load(di)
        #    print('--------------', b)
        # di.close()

        # if

        # print('ok')

        # print(len(self.fileindex[i]))
    # print(len(self.fileindex[i]))


#if __name__ == '__main__':
#    print 'argv[0]: ', sys.argv[0]
#    print 'argv[1]: ', sys.argv[1]
#    rootdir = os.path.join(os.getcwd(), 'db', sys.argv[1])



#    index(rootdir)
    # print(len(self.fileindex[i]))
    # print(len(self.fileindex[i]))


oo = Service()

