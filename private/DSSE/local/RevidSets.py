import sys
import os
import re
import random
import pickle
import myTools
import json
import hashlib

rows = 300
#global wordcounter
wordcounter = {}
localdictionary = "localdic.p"
dicpath = os.path.join(os.getcwd(), 'db', 'dic', 'localdic.json')
localaddlabel = 'labeladd.json'
deletepath = os.path.join(os.getcwd(), 'db', 'labeladd.json') # delete labeladd.json if it exists
deletepath2 = os.path.join(os.getcwd(), 'db', 'labeldel.json') # delete labeldel.json if it exists
# print dicpath
#counter = 0
#keywords_loc = {}
#keywordcount = 0


def dictionary():
    # Fetching local dictionary
    try:
        with open(dicpath, 'rb') as dic:
            #while 1:
               # try:
            dic_temp = json.load(dic)
                #except EOFError:
                 #   break
        dic.close()
        wordcounter = dic_temp
        print wordcounter
        return wordcounter
        print 'Dictionary loaded successfully !'
    except:
        print 'Unable to load the local dictionary... Building...'



def file_index_add(rootdir):
    wordcounter = dictionary()
    if os.path.isfile(deletepath):
         os.remove(deletepath)

    #L_label = {}
    #index_matrix = [[] for row in range(10000)]
    #file_id = 1001   # separate the add index from the original one
    Ka = 'addstring'
    Km = 'minustring'
    L_label = {}
    #countindex = 0
    #keywords_loc = {}
    # scaning keywords from the new file
    print wordcounter
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            file_id = filename      # Since in our dataset, the filenames are numbers, the value type of file id in the contract can be constructed as uint[].
            file_path = os.path.join(parent, filename)
            # print(file_path)
            with open(file_path) as newfile:
                raw_content = newfile.read()
            spli = raw_content.split()
           # keywords = None
            keywords = list(set(spli))
            newfile.close()
            #print(keywords)

            index_matrix = [[] for row in range(len(keywords))]

# Building index for the new file

            
            #global keywordcount 
            sep = '_'
            
            countindex = 0  # the number of each keyword in the index
            wordini = {} # initialize the local dictionary
            
            for word in keywords:
                #global wordcounter
                
                counter = 0
                K1_temp = [Ka, '1', word]
                K2_temp = [Ka, '2', word]
                Km_temp = [Km, word]
                #K_test = [Ka, '1', 'yesterday']

                K1_add = myTools.HMACSha256(sep.join(K1_temp))
                #K1_test = myTools.HMACSha256(sep.join(K_test))
                #print '----------------'
                #print countindex
                #print K1_add.encode('hex')
                #print myTools.CalcSha256(sep.join(K1_temp))
                K2_add = myTools.HMACSha256(sep.join(K2_temp))
                Km_del = myTools.HMACSha256(sep.join(Km_temp))
                try:
                    #wordcounter.has_key(word)
                    counter = wordcounter[word]
                    #print counter
                    #wordini[word] = counter
                    #print wordini
                except:
                    counter = 0
                    wordini[word] = 0
                # print counter
                #keywords_loc[word] = countindex
                #keywordcount +=1

# Building encrypted index

                #hash256 = hashlib.sha256()

                #hash256.update(K1_add)
                #hash256.update(str(counter))
                label = myTools.hmactest(K1_add, counter)
               # print '------------------------------------****'
               # print myTools.hmactest(K1_test, counter)

                #label = hash256.hexdigest()

# encrypt the file id

                d = file_id
                #L_label[label] = d
                index_matrix[countindex].append(label)
                index_matrix[countindex].append(d)


# Building the revid

                #hashminus = hashlib.sha256()
                revid = myTools.hmactest(Km_del, file_id)

                #hashminus.update(Km_del)
               # print 'file id is  --------------', file_id
                #hashminus.update(str(file_id))
                #revid = hashminus.hexdigest()
                index_matrix[countindex].append(revid)
                countindex += 1
            print index_matrix
            #file_id += 1
            outputpath = os.path.join(os.getcwd(), 'db')
            with open(os.path.join(outputpath, 'labeladd.json'), 'wb') as outputfile:

                # store the dictionary in json format
                json.dump(index_matrix, outputfile)
            outputfile.close()
            
            wordcounter.update(wordini)
            with open(dicpath, 'wb') as jsondic:
            
                json.dump(wordcounter, jsondic)
                
                #jsondic.write(json.dumps(wordini))
            jsondic.close()
            with open(os.path.join(outputpath, 'dic','addedkeywords.json'), 'wb') as outputfile:

                # store the dictionary in json format
                json.dump(keywords, outputfile)
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


def file_delete (file_path_del):
    dictionary()
    Km = 'minustring'
    revidlist = []
    if os.path.isfile(deletepath2):
         os.remove(deletepath2)

    for parent, dirnames, filenames in os.walk(file_path_del):
        for filename in filenames:
            file_id = filename  # ************
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
                Km_del = myTools.HMACSha256(sep.join(Km_temp))
                #Km_del = myTools.CalcSha256(sep.join(Km_temp))
                revid = myTools.hmactest(Km_del, file_id)
                #hashminus = hashlib.sha256()

                #hashminus.update(Km_del)
                #print 'file id is  --------------', file_id
                #print 'file id str is  --------------', int(file_id)
                #hashminus.update(str(file_id))
                #revid = hashminus.hexdigest()
                revidlist.append(revid)
            #print revidlist, len(revidlist)
            outputpath = os.path.join(os.getcwd(), 'db')
            with open(os.path.join(outputpath, 'labeldel.json'), 'wb') as outputfile:

                # store the dictionary in json format
                json.dump(revidlist, outputfile)
            outputfile.close()
            
            
            
            
            
            


            #print(keywords)



def update_local_dic (re):
    dictionary()









if __name__ == '__main__':
    rootdiradd = os.path.join(os.getcwd(), 'db', 'add')
    rootdirdel = os.path.join(os.getcwd(), 'db', 'delete')
    # print(rootdir)

#    file_index_add(rootdiradd)
    file_delete(rootdirdel)
#   file_index_add('\db\1', 1)

