#This code has been unused, and can be regarded as test code.


'''

## below are the search parts where data are stored in disk
##
## here we only generate search token. to perform search need
## to run MyContract.js


def search():
	search_word = 'data'
	result = []
	K = 'randomstring'
	sep = '_'
	outputpath_lable = os.path.join(os.getcwd(), 'db') #output path of label
	
	
	outputpath_d = os.path.join(os.getcwd(), 'db') #output path of file id

	
	K1_s_temp = [K,'1',search_word]
	K2_s_temp = [K,'2',search_word]
	K1_s = myTools.CalcSha256(sep.join(K1_s_temp))
	K2_s = myTools.CalcSha256(sep.join(K2_s_temp))
	
	print 'search K1 is:', K1_s
	#then send K1_s to the server
	
'''

'''
	read_path = os.path.join(outputpath_lable, 'lable.json')
#	print 'read path is:', read_path
	
	with open(read_path) as L_lable_file:
		L_lable_raw_content = L_lable_file.read()
	
#	print 'lable read raw content is', L_lable_raw_content
	
	L_lable_spli = L_lable_raw_content.split()
	L_lable_read = list(set(L_lable_spli))

#	print	'lable read list is', L_lable_read
	
	
	L_d_file = open(os.path.join(outputpath_d, 'fileid'))
	L_d_read = L_d_file.read()
	L_d_split = L_d_read.split()
	L_d_read = list(set(L_d_split))
	
	
	
	c = 0
	for lab in L_lable_read:
	
		hash256 = hashlib.sha256()
			
		#compute hash of the concatenation of K1 and string c.
		hash256.update(K1_s)    	
		hash256.update(str(c))
			
		#generate label, which is the result of hash.
		search_lab = hash256.hexdigest() 
	
		if search_lab in L_lable_read: 
			search_fid_loc = L_lable_read.index(search_lab)
			search_fid = int(L_d_read[search_fid_loc],16)^int(myTools.CalcSha256(K2_s),16) #decrypt file id
			result.append(search_fid)
			c += 1
#			print 'c is ', c
	print 'search result is', result
	#, 'lable read list is', L_lable_read
'''

''' 
#run: python index.py  keyword

if __name__ == '__main__':
	print 'argv[0]: ', sys.argv[0]
	print 'argv[1]: ', sys.argv[1]
	rootdir = os.path.join(os.getcwd(), 'db', sys.argv[1])
	index(rootdir)
#	print 'counter is', counter
#	print 'file id is', file_id
	
	search()

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
