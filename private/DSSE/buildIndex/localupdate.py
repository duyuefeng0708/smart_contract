import sys
import os
import re
import random
import pickle
import myTools
import json
import hashlib

rows = 300
isaddc = []
isadd = []
#temp1 = []
#temp2 = []

update = {}
#temp = []
keys = []
localdictionary = "localdic.json"
dicjspath = os.path.join(os.getcwd(), 'db', 'dic', 'localdicjs.json')
dicpath = os.path.join(os.getcwd(), 'db', 'dic', 'localdic.json')
keywordpath = os.path.join(os.getcwd(), 'db', 'dic', 'addedkeywords.json')
localaddlabel = 'labeladd.json'
#deletepath = os.path.join(os.getcwd(), 'db', 'labeladd.json') # delete labeladd.json if it exists
#deletepath2 = os.path.join(os.getcwd(), 'db', 'labeldel.json') # delete labeldel.json if it exists
# print dicpath
#counter = 0
#keywords_loc = {}
#keywordcount = 0


def renew_worddic (rootdir):
    #dictionary()
    #if os.path.isfile(deletepath):
    #     os.remove(deletepath)

    #L_label = {}
    #index_matrix = [[] for row in range(10000)]
    #file_id = 1001   # separate the add index from the original one
    #Ka = 'addstring'
    #Km = 'minustring'
    #L_label = {}
    #countindex = 0
    #keywords_loc = {}
    # scaning keywords from the new file
    #for parent, dirnames, filenames in os.walk(rootdir):
    try:
        with open(dicjspath, 'rb') as dic:
            #while 1:
               # try:
            dic_temp = json.load(dic)
                #except EOFError:
                 #   break
        dic.close()
        isaddc = dic_temp
        isadd = sum(isaddc, [])
        #i=0
        #temp1 = []
        #temp2 = []
        #isadd = isaddc[0]
        #temp1 = isaddc[0]
        #print temp1
        #print isaddc[1]
        #for i in len(isaddc):
        #     temp2 = temp1.extend(isaddc[i])
        #     print temp2
        #     temp1 = temp2
             #temp = isadd
        #     i+=1
             # isadd = isaddc[0]+isaddc[1]

        #isadd.copy(temp2)
        #isadd = temp2
        print isadd
        print 'Contract Response loaded successfully ! Updating local dictionary!'
    except:
        print 'Unable to load the local dictionary... '
        
    #if (isadd == 0):
    #{
    
    #}
    try:
        with open(keywordpath, 'rb') as dic:
            #while 1:
               # try:
            dic_temp = json.load(dic)
                #except EOFError:
                 #   break
        dic.close()
        keys = dic_temp
        print keys
        print 'Local Dictionary loaded successfully ! Updating!'
    except:
        print 'Unable to load the local dictionary... '
    

    try:
        with open(dicpath, 'rb') as dic:
            #while 1:
               # try:
            dic_temp = json.load(dic)
                #except EOFError:
                 #   break
        dic.close()
        update = dic_temp
        print update
        print 'Local Dictionary loaded successfully ! Updating!'
    except:
        print 'Unable to load the local dictionary... '    
    #keys = update
    #print keys
    
    j = 0
    while(j<len(keys)):
         if(isadd[j] == '0'):
             temp = update[keys[j]] +1
             #print temp
             update[keys[j]] = temp
         j+=1
    
    
    print update
    
    try:
        with open(dicpath, 'wb') as dic:
            #while 1:
               # try:
            json.dump(update, dic)
                #except EOFError:
                 #   break
        dic.close()
        #update = dic_temp
        print update
        print 'Local Dictionary Updated successfully !!'
    except:
        print 'Unable to load the local dictionary... '






if __name__ == '__main__':
    rootdiradd = os.path.join(os.getcwd(), 'db', 'add')
    rootdirdel = os.path.join(os.getcwd(), 'db', 'delete')
    rootdirdic = os.path.join(os.getcwd(), 'db', 'dic')
    # print(rootdir)
    renew_worddic (rootdirdic)

#    file_index_add(rootdiradd)
#    file_delete(rootdirdel)
#   file_index_add('\db\1', 1)

