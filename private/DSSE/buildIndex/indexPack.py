#This version of index code is optimized by vertically packing and horizontally partition.


import sys
import os
import re
import random
import pickle
import myTools
import json
import hashlib

rows = 10000
counter = 0
keywords_loc = {}  #map each keyword to each row of index matrix

index_matrix = [[] for row in range(rows)]  #store index matrix: each row store file ids correspond to a keyword


def file_index (parent, filename, file_id):
	file_path = os.path.join(parent, filename)
	
	
#	filename_sha1 = myTools.CalcSha1(filename)
   	with open(file_path) as inputfile:
   		raw_content = inputfile.read()

	spli = raw_content.split()
	keywords = list(set(spli))
# 	print 'keywords: ', keywords
	
	global counter
	for word in keywords:
		if keywords_loc.has_key(word):
			loc = keywords_loc[word]
			index_matrix[loc].append(file_id)
#			print 'keyword is', word
		else :
			keywords_loc[word] = counter
			index_matrix[counter].append(file_id)
			counter += 1
#			print 'counter is', counter, 'file id is', file_id,  'index_matrix', index_matrix[counter]
			


def index(rootdir):

#file id should be counted from 1 instead of 0, or contract will get wrong search result since fileid==0 is the judge condition.

	file_id = 1		
	
#K should be randomly generated, but here we use a fixed string instead.	
	K = 'randomstring'
	
#store label (pointing to each keyword-file pair) and corresponding encrypted file id.
	L_label = {}   
	
	
	 
	
	sep = '_'
	for parent, dirnames, filenames in os.walk(rootdir):
		for filename in filenames:
			file_path = os.path.join(parent, filename)
			file_index (parent, filename, file_id)
			print 'filename is: ', filename, '	file id is: ', file_id

			file_id += 1
	
#For now keyword-file pairs have been already built and stored in index_matrix. 
	print 'amount of keywords is: ', len(keywords_loc)


















#Below we use index_matrix to generate encrypted index and files.

	for word in keywords_loc:
		
		#Used for encrypt counter and generate label.
		K1_temp = [K,'1',word] 
		
		#Used for encrypt file id. though we actually not use it at all.
		K2_temp = [K,'2',word] 


		
		K1 = myTools.CalcSha256(sep.join(K1_temp))
		K2 = myTools.CalcSha256(sep.join(K2_temp))

	#	print 'K1 is :', K1
	
		#c is initialized from 0, this should be kept the same with seachfile function in the contract.
		c = 0
		loc = keywords_loc[word]
		for fid in index_matrix[loc]:
			hash256 = hashlib.sha256()
			
			#Compute hash of the concatenation of K1 and string c.
			hash256.update(K1)    	
			hash256.update(str(c))
			
			#Generate label, which is the result of hash.
			label = hash256.hexdigest() 
			 
		 	#In our scheme, we are not yet encrypt file id.
			d = fid 	
				 
			
			#Store label and corresponding file id
			L_label[label] = d  
			
		 
						
			c += 1
	
	print 'total number of keyword-file pair in label is: ', len(L_label)
	
	#Output path of L_label 
	outputpath = os.path.join(os.getcwd(), 'db')  
	with open(os.path.join(outputpath, 'label.json'), 'wb') as outputfile:
		
		#Store the dictionary in json format
		json.dump(L_label, outputfile)	
	outputfile.close()



 
#run: python index.py db_name (e.g. test)

if __name__ == '__main__':
	print 'argv[0]: ', sys.argv[0]
	print 'argv[1]: ', sys.argv[1]
	rootdir = os.path.join(os.getcwd(), 'db', sys.argv[1])
	index(rootdir)
#	print 'counter is', counter
#	print 'file id is', file_id






'''	
#Next for each row we will pack many plaintexts into one. Before that, we should first append enough dunmmy records, which 
#are set to 0, to each row so that all the rows have the same length.

	
	#At first we find the largest number of files for a given keyword. So that we can decide how many dunmmy records we should append.	
	word_counter = 0
	max_files = 0
	for word in keywords_loc:
		
		loc = keywords_loc[word]
		file_amount =  len(index_matrix[loc])
		
		if(file_amount > max_files):
			max_files = file_amount
		
	#	print 'row in index matrix is: ', word_counter, 'amount of files is: ', file_amount
		
		word_counter += 1
	print 'max number of files for a given keyword is: ', max_files
	
	

	#Below we append dummy records.
	
	number_to_append = 0
	
	for word in keywords_loc:
		
		
		loc = keywords_loc[word]
		file_amount =  len(index_matrix[loc])

		number_to_append = 	max_files - file_amount
		
		for i in range(0,number_to_append):
		#	print 'number to append is: ', number_to_append, 'here i is: ', i
			index_matrix[loc].append(0)
		new_file_amount = len(index_matrix[loc])
		
		#print 'new file amount is: ', new_file_amount
'''





	
'''
	hash1 = hashlib.sha256()
	hash1.update('h')
	hash1.update('12')
	hash_re = hash1.hexdigest()
	print 'hash result is: ', hash_re
'''

'''	for i in range(rows):  
         for j in range(len(index_matrix[i])):  
           	print index_matrix[i][j],
	 print '\n'
'''	
