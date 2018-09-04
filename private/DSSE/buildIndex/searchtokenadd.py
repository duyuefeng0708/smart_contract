
## Below are the search parts where data are stored in disk
##
## here we only generate search token. to perform search need
## to run MyContract.js

import myTools
import json
import sys
import os
import hashlib



def search(search_word):
#	search_word = 'data'
	result = []
	K = 'addstring'
	Km = 'minustring'
	sep = '_'
	outputpath_lable = os.path.join(os.getcwd(), 'db') #output path of label
	
#	print 'label path is ', outputpath_lable
	
	outputpath_d = os.path.join(os.getcwd(), 'db') #output path of file id

	temp = []
	K1_temp = [K,'1',search_word]
	Km_temp = [Km, search_word]
#	K2_temp = [K,'2',search_word]

	K1 = myTools.HMACSha256(sep.join(K1_temp))
	K_minus = myTools.CalcSha256(sep.join(Km_temp))
	temp.append(K1.encode('hex'))
	temp.append(K_minus)
	
#	K2 = myTools.CalcSha256(sep.join(K2_temp))
	
#	print 'search token K1 is:', K1
	#then send K1 to the server









	
	#output path of search token K_add and K_minus
	outputpath = os.path.join(os.getcwd(), 'db')  
	with open(os.path.join(outputpath, 'searchtokenadd.json'), 'wb') as outputfile:
		
		#store the dictionary in json format
		json.dump(temp, outputfile)	
	outputfile.close()

	
	
#Below are search part written in python. They have been tested and passed.	

'''	
	
	
	
#	L_label = {}
	
	
	#output path of L_label 
	outputpath = os.path.join(os.getcwd(), 'db')  
	with open(os.path.join(outputpath, 'label.json'), 'r') as outputfile:
		
		#store the dictionary in json format
		L_label = json.load(outputfile)	
	outputfile.close()



	
#	print 'label are:', L_label





	c = 0
	flag = 1
	while(flag):
	
		hash256 = hashlib.sha256()
			
		#compute hash of the concatenation of K1 and string c.
		hash256.update(K1)    	
		hash256.update(str(c))
			
		#generate label, which is the result of hash.
		search_lab = hash256.hexdigest() 
	
		if search_lab in L_label: 
			search_fid = L_label[search_lab]
#			search_fid = int(L_d_read[search_fid_loc],16)^int(myTools.CalcSha256(K2_s),16) #decrypt file id
			result.append(search_fid)
			c += 1
			 
		else:
			flag = 0
#			print 'c is ', c
	print 'search result of file ids are', result
	#, 'lable read list is', L_lable_read
'''


 
#run: python index.py  keyword

if __name__ == '__main__':
	print 'argv[0]: ', sys.argv[0]
	print 'search keyword is: ', sys.argv[1]
	
	search(sys.argv[1])

'''
	hash1 = hashlib.sha256()
	hash1.update('h')
	hash1.update('12')
	hash_re = hash1.hexdigest()
	print 'hash result is: ', hash_re
'''
