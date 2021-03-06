import sys
import os
import re
import random
import pickle
import myTools
import json
import hashlib
import struct

rows = 10000000
counter = 0
keywords_loc = {}  #map each keyword to each row of index matrix
random = []  # initialize the random string array random[].

index_matrix = [
	[] for row in range(rows)
]  #store index matrix: each row store file ids corresponds to a keyword


def file_index(parent, filename, file_id):
	file_path = os.path.join(parent, filename)

	filename_sha1 = myTools.CalcSha1(filename)
	with open(file_path) as inputfile:
		raw_content = inputfile.read()

	spli = raw_content.split()
	keywords = list(set(spli))
	# 	print 'keywords: ', keywords

	global counter

	#store label (pointing to each keyword-file pair) and corresponding encrypted file id, and random strings.
	#L_label = [[] for row in range(len(keywords))]
	for word in keywords:
		if keywords_loc.has_key(word):
			loc = keywords_loc[word]
			index_matrix[loc].append(file_id)
#			print 'keyword is', word
		else:
			keywords_loc[word] = counter
			index_matrix[counter].append(file_id)
			counter += 1


#			print 'counter is', counter, 'file id is', file_id,  'index_matrix', index_matrix[counter]


def index_pack(loc, lp):
	# pack 16 ids at a time for the rest ids in index_matrix[loc].
	u = b'0'
	if len(index_matrix[loc]) == 1:
		d = index_matrix[loc][0]
		d = struct.pack('BBBBBBBBBBBBBBBB', d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
						0, 0, 0, 0)
		dt = d.encode('hex')
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, d))
	if len(index_matrix[loc]) == 2:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], 0, 0, 0, 0, 0, 0, 0,
						0, 0, 0, 0, 0, 0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 3:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], 0, 0, 0, 0, 0,
						0, 0, 0, 0, 0, 0, 0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 4:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], 0, 0, 0,
						0, 0, 0, 0, 0, 0, 0, 0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 5:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4], 0,
						0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 6:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4],
						d[5], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 7:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4],
						d[5], d[6], 0, 0, 0, 0, 0, 0, 0, 0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 8:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4],
						d[5], d[6], d[7], 0, 0, 0, 0, 0, 0, 0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 9:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4],
						d[5], d[6], d[7], d[8], 0, 0, 0, 0, 0, 0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 10:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4],
						d[5], d[6], d[7], d[8], d[9], 0, 0, 0, 0, 0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 11:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4],
						d[5], d[6], d[7], d[8], d[9], d[10], 0, 0, 0, 0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 12:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4],
						d[5], d[6], d[7], d[8], d[9], d[10], d[11], 0, 0, 0,
						0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 13:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4],
						d[5], d[6], d[7], d[8], d[9], d[10], d[11], d[12], 0,
						0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 14:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4],
						d[5], d[6], d[7], d[8], d[9], d[10], d[11], d[12],
						d[13], 0, 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 15:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4],
						d[5], d[6], d[7], d[8], d[9], d[10], d[11], d[12],
						d[13], d[14], 0)
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	if len(index_matrix[loc]) == 16:
		d = []
		for fid in index_matrix[loc]:
			d.append(fid)
		out = struct.pack('BBBBBBBBBBBBBBBB', d[0], d[1], d[2], d[3], d[4],
						d[5], d[6], d[7], d[8], d[9], d[10], d[11], d[12],
						d[13], d[14], d[15])
		u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
	#print u.encode('hex'),len(index_matrix[loc])
	return u.encode('hex')


def index(rootdir):

	#file id should be counted from 1 instead of 0, or contract will get wrong search result since fileid==0 is the judge condition.

	file_id = 1

	#K should be randomly generated, but here we use a fixed string instead.
	K = 'randomstring'

	#store label (pointing to each keyword-file pair) and corresponding encrypted file id.
	#L_label = {}

	sep = '_'
	pairnum = 0
	d = {}
	with open(os.path.join(os.getcwd(), 'db', sys.argv[1], 'fileid.txt'), 'wb') as out:	
		for parent, dirnames, filenames in os.walk(rootdir):
			for filename in filenames:
				if not filename[0].isdigit():
					continue
				file_path = os.path.join(parent, filename)
				file_index(parent, filename, file_id)
				d[file_id] = filename
				out.write('filename is: ' + str(filename) + '\n' + ' -> file id is: '+ str(file_id) + '\n')
				file_id += 1
	out.close()

	with open(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'fileid.p'), 'wb') as fp:
		pickle.dump(d, fp, protocol=pickle.HIGHEST_PROTOCOL)

	#store label (pointing to each keyword-file pair) and corresponding encrypted file id, and random strings.
	# print (len(keywords_loc))

	L_label = []
	countindex = 0

	##for now keyword-file pairs have been already built and stored in index_matrix. next generate encrypted index and files.

	#random = []
	#countindex = 0
	#pairnum = 0
	for word in keywords_loc:
		#used for encrypt counter and generate label.
		K1_temp = [K, '1', word]

		#used for encrypt file id. though we actually not use it at all.
		K2_temp = [K, '2', word]

		K1 = myTools.HMACSha256(sep.join(K1_temp))
		K2 = myTools.HMACSha256(sep.join(K2_temp))

		#	print 'K1 is :', K1

		#c is initialized from 0, this should be kept the same with seachfile function in the contract.
		c = 0
		#countindex = 0
		loc = keywords_loc[word]
		pairnum = pairnum + len(index_matrix[loc])
		if len(index_matrix[loc]) <= 16:
			#print '11111111111111111'
			it = (os.urandom(16)).encode(
				'hex')  # the random string used for encryption\
			lp = myTools.hmactest10(K2, it)
			label = myTools.hmactest(K1, c)
			cipher = index_pack(loc, lp)
			addlist = [label, cipher, it]
			L_label.append(addlist)
			#L_label[countindex].append(label)
			#L_label[countindex].append(cipher)
			#L_label[countindex].append(it)
			countindex += 1
		else:
			# print word
			#it = (os.urandom(16)).encode('hex') # the random string used for encryption\
			#lp = myTools.hmactest10(K2, it)
			#label = myTools.hmactest(K1, c)
			ut = len(index_matrix[loc])
			d = [0 for i in range(ut + 16)]
			# print ut
			j = 0
			for fid in index_matrix[loc]:
				#i = 0
				d[j] = fid
				j += 1
			# print d
			c = 0
			#out = []
			for i in range(ut / 16 + 1):
				# print i
				it = (os.urandom(16)).encode(
					'hex')  # the random string used for encryption\
				#print it
				lp = myTools.hmactest10(K2, it)
				label = myTools.hmactest(K1, c)
				#print lp, label
				out = struct.pack(
					'BBBBBBBBBBBBBBBB', d[16 * i], d[(16 * i) + 1],
					d[(16 * i) + 2], d[(16 * i) + 3], d[(16 * i) + 4],
					d[(16 * i) + 5], d[(16 * i) + 6], d[(16 * i) + 7],
					d[(16 * i) + 8], d[(16 * i) + 9], d[(16 * i) + 10],
					d[(16 * i) + 11], d[(16 * i) + 12], d[(16 * i) + 13],
					d[(16 * i) + 14], d[(16 * i) + 15])
				# print out.encode('hex')
				u = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(lp, out))
				cipher = u.encode('hex')
				#print cipher
				addlist = [label, cipher, it]
				L_label.append(addlist)
				#L_label[countindex].append(cipher)
				#L_label[countindex].append(it)
				c += 1
				#countindex +=1

	outputpath = os.path.join(os.getcwd(), 'db')
	# print pairnum
	with open(os.path.join(outputpath, 'label'+sys.argv[1]+'.json'), 'wb') as outputfile:

		#store the dictionary in json format
		outputfile.write(json.dumps(L_label, indent=4))
		#json.dump(L_label, outputfile)
	outputfile.close()

if __name__ == '__main__':
	# print 'argv[0]: ', sys.argv[0]
	# print 'argv[1]: ', sys.argv[1]
	rootdir = os.path.join(os.getcwd(), 'db', sys.argv[1])
	index(rootdir)
#	print 'counter is', counter
#	print 'file id is', file_id
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
