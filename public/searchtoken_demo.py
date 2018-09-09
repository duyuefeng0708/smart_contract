
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





def token (query):
    searchgen = tokenhmac.copy()
    sr = searchgen.update(query)
    srtoken = searchgen.digest()
    print('The query keyword is :    ', str(query))
    print('The search token is:      ', "\""+searchgen.hexdigest()+"\"")
    print("Contract function call (Search) input:\n","\""+searchgen.hexdigest()+"\""+",0")
    with open('searchtoken.p', 'wb') as sr:
        #lists[token] = plist
        # print(lists)
        # sr.write(str(lists))
        pickle.dump(srtoken, sr)
    sr.close()
    print ("Creating a file for the search token ...")
    with open('searchtoken.json', 'w') as indexa:
            json.dump(searchgen.hexdigest(), indexa)
    indexa.close()



if __name__ == '__main__':
    #print 'argv[0]: ', sys.argv[0]
    #print 'argv[1]: ', sys.argv[1]
    token(sys.argv[1].encode('utf-8'))



#    index(rootdir)
    # print(len(self.fileindex[i]))
    # print(len(self.fileindex[i]))

