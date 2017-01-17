__author__ = 'cdumitru'

from Crypto.PublicKey import RSA
from Crypto import Random
import gmpy
import base64


#tup (tuple) - A tuple of long integers, with at least 2 and no more than 6 items. The items come in the following order:
#RSA modulus (n).
#Public exponent (e).
#Private exponent (d)
#First factor of n (p).
#Second factor of n (q)

n = 0
p = 9594425659998056478309883943809061195083011864919537185550456855079985417816802975107872277560873098912167001528573985392980328726454437911178054657661797
q = 9686661516614391354318193460962571279340087464047355624829351181505663174132301882515483393522634363750181291908207894755972257473434370581852105652305920
e = 65537

string_to_be_encrypted="Emil A. Sharifullin"

phi = (p - 1) * (q - 1)
d = int(gmpy.invert(e, phi))

tup = (n ,e, d, p, q )
key = RSA.construct(tup)

random_generator = Random.new().read
data = key.encrypt(string_to_be_encrypted,random_generator)


print(key.exportKey('PEM'))
print(key.publickey().exportKey())
print(base64.b64encode(data[0]))
