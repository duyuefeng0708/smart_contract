#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import re
import pickle
import datetime
import os
from binascii import unhexlify, hexlify

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
	
def HMACSha256(word):
    shaobj = hashlib.sha256()
    shaobj.update(word)
    hash1 = shaobj.digest()
    #print shaobj.digest_size
    return hash1
	


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
        print 'Unable to open mydata.pickle!'
    return data_dict


def GetUserName():
    data_dict = GetDataDict()

    return data_dict.get('username', 'Unset')



def SetUserName(username):
    data_dict = GetDataDict()

    data_dict['username'] = username

    with open('mydata.pickle', 'wb') as output:
        pickle.dump(data_dict, output)

def hmactest(key, num):
    #print num
    #num = 13
    #key = '\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61'
    ipad = '\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36'
    opad = '\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c'
    #print int(key, 32)
    #l = [ord(a) ^ ord(b) for a,b in zip(key,ipad)]
    #print l
    in32 = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(key,ipad))
    #print in32.encode('hex')


    #result1 = int(key, 16) ^ int(ipad, 16) # convert to integers and xor them
    #in32_str = hex(result1)
    #print '-----' 
    #print result1
    #in32 = '{:x}'.format(result1)
    #print in32
    #in32 = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(key[-len(ipad):]), unhexlify(ipad))))
    #print '------'
    #print '{:x}'.format(in32)

    #in32 = key ^ ipad

    hash1 = hashlib.sha256()
    hash1.update(str(in32))
    hash1.update(str(num))
    #print str(num)
    result = hash1.hexdigest()
    #print result

    out32 = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(key,opad))
    #print out32.encode('hex')
    
    #hash3 = hashlib.sha256()
    #hash3.update('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
    #hash3.update(str(12))
    #print '211111!!!!' + hash3.hexdigest()



    #resulto = int(key, 16) ^ int(opad, 16) # convert to integers and xor them
    #print '======'
    #print resulto
    #out32 = '{:x}'.format(resulto)

    #out32 = key ^ opad
    #print out32
    #print out32

    hash2 = hashlib.sha256(out32)
    #hash2.update(str(out32))
    hash2.update(result.decode('hex'))
    resultc = hash2.hexdigest()
    return resultc

def hmactest10(key1, key2):
    #print num
    #num = 13
    #key = '\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61'
    ipad = '\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36'
    opad = '\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c'
    #print int(key, 32)
    #l = [ord(a) ^ ord(b) for a,b in zip(key,ipad)]
    #print l
    in32 = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(key1,ipad))
    #print in32.encode('hex')


    #result1 = int(key, 16) ^ int(ipad, 16) # convert to integers and xor them
    #in32_str = hex(result1)
    #print '-----' 
    #print result1
    #in32 = '{:x}'.format(result1)
    #print in32
    #in32 = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(key[-len(ipad):]), unhexlify(ipad))))
    #print '------'
    #print '{:x}'.format(in32)

    #in32 = key ^ ipad

    hash1 = hashlib.sha256()
    hash1.update(str(in32))
    hash1.update(str(key2))
    #print str(num)
    result = hash1.hexdigest()
    #print result

    out32 = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(key1,opad))
    #print out32.encode('hex')
    
    #hash3 = hashlib.sha256()
    #hash3.update('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
    #hash3.update(str(12))
    #print '211111!!!!' + hash3.hexdigest()



    #resulto = int(key, 16) ^ int(opad, 16) # convert to integers and xor them
    #print '======'
    #print resulto
    #out32 = '{:x}'.format(resulto)

    #out32 = key ^ opad
    #print out32
    #print out32

    hash2 = hashlib.sha256(out32)
    #hash2.update(str(out32))
    hash2.update(result.decode('hex'))
    resultc = hash2.digest()
    return resultc

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
