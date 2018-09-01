import sys
import os
import re
import random
import pickle
import myTools
import json
import hashlib
from binascii import unhexlify, hexlify

rows = 300
wordcounter = {}
localdictionary = "localdic.p"
dicpath = os.path.join(os.getcwd(), 'db', 'dic') + localdictionary
# print dicpath
#counter = 0
#keywords_loc = {}
#keywordcount = 0


def dictionary():
    # Fetching local dictionary
    try:
        with open(dicpath, 'rb') as dic:
            while 1:
                try:
                    dic_temp = pickle.load(dic)
                except EOFError:
                    break
        dic.close()
        wordcounter = dic_temp.copy()
        print wordcounter
        print 'Dictionary loaded successfully !'
    except:
        print 'Unable to load the local dictionary... Building...'


def file_index_add(rootdir):
    dictionary()

    #L_label = {}
    file_id = 1000   # separate the add index from the original one
    Ka = 'addstring'
    Km = 'minustring'
    L_label = {}
    #keywords_loc = {}
    # scaning keywords from the new file
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            print filename
            file_path = os.path.join(parent, filename)
            # print(file_path)
            with open(file_path) as newfile:
                raw_content = newfile.read()
            spli = raw_content.split()
           # keywords = None
            keywords = list(set(spli))
            newfile.close()
            print(keywords)

            index_matrix = [[] for row in range(len(keywords))]

# Building index for the new file

            #global counter
            #global keywordcount
            sep = '_'
            countindex = 0  # the number of each keyword in the index
            for word in keywords:
                counter = 0
                K1_temp = [Ka, '1', word]
                K2_temp = [Ka, '2', word]
                Km_temp = [Km, word]

                K1_add = myTools.CalcSha256(sep.join(K1_temp))
                K2_add = myTools.CalcSha256(sep.join(K2_temp))
                Km_del = myTools.CalcSha256(sep.join(Km_temp))
                try:
                    wordcounter.has_key(word)
                    counter = wordcounter[word]
                except:
                    counter = 0
                # print counter
                #keywords_loc[word] = countindex
                #keywordcount +=1

# Building encrypted index

                hash256 = hashlib.sha256()

                hash256.update(K1_add)
                hash256.update(str(counter))

                label = hash256.hexdigest()

# encrypt the file id

                d = file_id
                #L_label[label] = d
                index_matrix[countindex].append(label)
                index_matrix[countindex].append(d)


# Building the revid

                hashminus = hashlib.sha256()

                hashminus.update(Km_del)
                hashminus.update(str(file_id))
                revid = hashminus.hexdigest()
                index_matrix[countindex].append(revid)
                countindex += 1

            print index_matrix
            file_id += 1
            outputpath = os.path.join(os.getcwd(), 'db')
            with open(os.path.join(outputpath, 'labeladd.json'), 'wb') as outputfile:

                # store the dictionary in json format
                json.dump(index_matrix, outputfile)
            outputfile.close()

            # print(K1_add)

            # print(K2_add)
            # print(Km_del)
            # print '=============Keys generated for keywords'

            # if keywords_loc.has_key(word):
            #   loc = keywords_loc[word]
            #   index_matrix[loc].append()

            #print(os.path.join(root, name))
            #filename_sha1 = myTools.CalcSha1(filename)
            # print(filename_sha1)


def file_delete(file_id, file_path_del):
    dictionary()
    Km = 'minustring'
    revidlist = []

    for parent, dirnames, filenames in os.walk(file_path_del):
        for filename in filenames:
            print filename
            file_path = os.path.join(parent, filename)
            # print(file_path)
            with open(file_path) as delfile:
                raw_content = delfile.read()
            spli = raw_content.split()
            keywords = list(set(spli))
            print len(keywords)
            delfile.close()
            sep = '_'
            for word in keywords:
                Km_temp = [Km, word]
                Km_del = myTools.CalcSha256(sep.join(Km_temp))
                hashminus = hashlib.sha256()

                hashminus.update(Km_del)
                hashminus.update(str(file_id))
                revid = hashminus.hexdigest()
                revidlist.append(revid)
            # print revidlist, len(revidlist)
            outputpath = os.path.join(os.getcwd(), 'db')
            with open(os.path.join(outputpath, 'labeldel.json'), 'wb') as outputfile:

                # store the dictionary in json format
                json.dump(revidlist, outputfile)
            outputfile.close()

            # print(keywords)


def hmac(num):
    key = '\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61'
    ipad = '\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36\x36'
    opad = '\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c\x5c'
    #print int(key, 32)
    #l = [ord(a) ^ ord(b) for a,b in zip(key,ipad)]
    #print l
    in32 = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(key,ipad))
    print in32


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
    print result

    out32 = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(key,opad))
    print out32
    
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
    print resultc


def update_local_dic(re):
    dictionary()


if __name__ == '__main__':
    rootdir = os.path.join(os.getcwd(), 'db', 'add')
    hmac(13)
    # print(rootdir)
#    file_index_add(rootdir)
#    file_delete(1, rootdir)
#   file_index_add('\db\1', 1)
