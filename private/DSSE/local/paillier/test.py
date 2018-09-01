from paillier import *

print "Generating keypair..."
priv, pub = generate_keypair(1024)

print 'private key is: ', priv

x = 3
print "x =", x
print "Encrypting x..."
cx = encrypt(pub, x)
print "cx =", cx

