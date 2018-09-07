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
testanswer = []



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
        self.fileindex = b
        print(len(self.fileindex))
        #print(b)
        #print(b)

        with open('searchtoken.p', 'rb') as dd:
            srtoken = pickle.load(dd)
        o = 0

        #self.fileindex = cstar
        for y in range(1):
            #### input the keyword to be queried
            query = b'Date:'
            #query = b'ft'
            try:
                #query = b'phi'
                with open('searchindex.p', 'rb') as di:
                    while 1:
                        try:
                            b = pickle.load(di)
                        except EOFError:
                            break
                di.close()
                with open('digestindex.p', 'rb') as dit:
                    while 1:
                        try:
                            p = pickle.load(dit)
                        except EOFError:
                            break
                dit.close()
                try:
                    self.searchindex = b.copy()
                    self.digestindex = p.copy()
                except:
                    o = 3
            except:
                o += 1
                print(o)
            self.exeutesearch(srtoken, y)
            # print('!!!!!!!!!!yyyyyyyyyyyyyyyyyyyyy')
        # print(self.fileindex[0][1])
       

    def exeutesearch(self, srtoken, count):

        #pick = randint(0, len(indepentwlist) - 1)

        #query = indepentwlist[pick]
        #print('^^^^^^^^^^ Searching for %s ^^^^^^^^^^^^^^^^^^^' % str(query))
        #p = struct.pack('s', query)
        #searchgen = tokenhmac.copy()
        #sr = searchgen.update(query)
        #srtoken = searchgen.digest()
        postinglist = []

        # srtoken = k1.encrypt(p)
        # srtoken2 = k1.encrypt(p)
        # print(srtoken)
        # print(srtoken2)
        # plain = k1.decrypt(srtoken)
        # print(plain)
        with open('searchtoken.json', 'r') as indexa:
            token1 = json.load(indexa)
        indexa.close()
        print("The search token is:", token1)
        try:
            postinglist = self.searchindex[srtoken]
            hm = self.digestindex[srtoken]
            print('The result it retrieved optimally from search index!')
        except:
        #if (1):
            checki = hmac.new(srtoken)
            has =0
            for i in range(len(self.fileindex)):
                if len(self.fileindex[i]) != 0:
                    for j in range(1, len(self.fileindex[i]), 2):
                        # print(self.fileindex[i][j])
                        #print('#######################################', count)
                        # check = hmac.new(srtoken)
                        checkhere = checki.copy()
                        # print(checkhere)
                        # print('compare')
                        q = struct.pack('s', self.fileindex[i][j])
                        # print(q)
                        checkhere.update(q)
                        # print()
                        up2 = checkhere.hexdigest()
                        # print(up2)
                        #print('comparing ooooooooooooooooo !!! with', up2)
                        compare = hmac.compare_digest(
                            self.fileindex[i][j - 1], up2)
                        #print('complete !!!!!!!!!!!!!!!!!!!!!!!    result:', compare)
                        if compare == True:
                            #print('Finding one matching id: %s' % i)
                            
                            postinglist.append(i)
                            count = count +1
                            #print(has)
                            if has != 0:
                                hm =sethash.Sethashadd(hm, str(i))
                                #print(hm)
                            if has ==0:
                                mappin = {}
                                cntest = Counter()
                                cntest.update([str(i)])
                                mappin = sethash.Verification(cntest)
                                hm=sethash.Sethash(mappin.values())
                                #print(cntest,hm)
                                has = 1
            self.output(srtoken, postinglist, hm)
                            #has = 1
                        #if compare == True && has == 1:
                            #h =sethash.Sethashadd(h,wlist[fid][j])
            #hm = hmm.hexdigest()
            # print(hm)
            
            # with open('searchindex.json', 'a') as sr:
            #    json.dump(self.searchindex, sr)
            # sr.close()
            # with open('searchindex.json', 'r') as rr:
            #    data = json.load(rr)
            #    print(data)

        # print(self.searchindex[query])
        
        print('The query answer is :   ', postinglist)
        print('The digest is :  ', hm)
        print(
            '****************************************************************************')
        #self.output(srtoken, postinglist, hm)

    def output(self, token, plist, digest):
        lists = {}
        digestlist = {}
        with open('searchindex.p', 'ab') as sr:
            lists[token] = plist
            # print(lists)
            # sr.write(str(lists))
            pickle.dump(lists, sr)
        sr.close()
        with open('digestindex.p', 'ab') as digl:
            # print(
            #    'oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
            digestlist[token] = digest
            pickle.dump(digestlist, digl)
        digl.close()
        hasher = hashlib.md5()
        with open('fileindex-demo.p', 'rb') as hashing:
            buf = hashing.read()
            hasher.update(buf)
        hashing.close()
        with open('indexdigest_peer.json', 'w') as indexa:
            json.dump(hasher.hexdigest(), indexa)
        indexa.close()
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

