import subprocess
try:
    import cPickle as pickle
except ImportError:  # python 3.x
    import pickle

contents = []
with open("./outcome") as f:
    for i,line in enumerate(f):
        if i >= 2 and i <= 51:
            raw = line.strip().split('\'')[1][2:]
            half = raw[:len(raw) // 2]
            for idx in range(16):
                contents.append(int(half[2*idx:2*idx+2], 16))
stop = 0
for i, elem in enumerate(contents):
    if elem == 0:
        stop = i
        break
contents = contents[:stop]
with open("fileid.p", 'rb') as fp:
    data = pickle.load(fp)
for elem in contents:
    print data[elem]
    # bashCommand = "open ./DSSE/buildIndex/db/finance10/$elem"
    # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()

