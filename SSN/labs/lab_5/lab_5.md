# Security of Systems and Networks: Lab 5

**Author**: Emil A. Sharifullin 
**Date**:   5 November, 2016  

RSA

### Create a 2048 bit RSA key-pair using openssl. Write your full name in a text file and encrypt it with your public key. Using OpenSSL extract the public modulus and the exponent from the public key. Publish your public key and the encrypted text in your report.

To generate OpenSSL keypair I used this command

```bash
$ openssl genrsa -des3 -out private.pem 2048
Generating RSA private key, 2048 bit long modulus
.+++
...............................................+++
e is 65537 (0x10001)
Enter pass phrase for private.pem:
Verifying - Enter pass phrase for private.pem:
$ cat private.pem 
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,B84196C129642069

AUozNag8wXM8nkHzJTA5OSg8lrZYEpVnvmuYCO9g6ZlpY4NOLwPHgMK3bWFxGh6Q
DGjKugYO7XgPQTWnogV9GI19v52WL+OhVA8wkYnRkPYb9uJxBabjLEIjV7/YHOlM
GhR/dNJQwa5g/R4CXeTCtvEO9E/NL9DzzZt+cuKHi2hKm0/r/8pphRR/TfG0juvn
oFOoi0+1A+p+CVVh4t86SFRvQjcpKjvlTk7BWo+XHIE19KyVur56/KL1hbWEpPQ0
3R73mh7Gi5wcfdp47umxrT91XdfDb1oOO7iYGCi6WN64VcHnkzYy/j21CfKMFVvV
m8uek6iGBkG224et8VDIVDXp3aDE77tDdSmMJ5aa5Jmo7aZR7zaXRaDrveVr6wNX
fIpRyNNe/PRoi2Ca0LDxt4H+rvwiTsBKqLu09ejQVxseW6VZDc9uwhJH1ZWQZFuE
mivdU2zDrMw4oGkz8M3zXG5HvvQLR9HhX5fA8jCZonVyh/mfhLcEWp5DYKDhm6Vi
FOeMa5vgCsHqwNE+rs0K6lIItZxpRlxeoIl+VbmpPwOmbkcLXDGkiXVOUrtfbuAY
ZLLA6oGhs64IHLykFxPzZnwzQOUBQcrzS0QSzyD1sdt41cvbW6eOMQruweEPotyO
u+3c+WW69WqOr84GA74nicRZ11qTLEiMkLSh11l3Lah5g+dqflXXAFQc3UQ2zfs4
dcBJ5wY9S+w3qlPdD0u6bKxYEtFVQCNd2t9v9JBLTOuWVpzrbXupUc1TUdx2OQ3Y
szc4F+X4Yh5C75CqfXS7/sXPfyWn1Xb12fyQp9asXdwS75MELR5gyw+IBb1RyJ3S
Twt+X7XhNNcbtHwFgOFDYAk9nA9TZD+Jg5kKHeuk9ArIDfTeNqu2wmGZ2Z9tPxeh
F/IqVEggsgKnHihU1TzEeQ5oUS4jg9pBQdveyskH2GbXH+uD+qkUbR9JZ8q+Mzza
NXF6Kv+LItnM+xR1d2APHbjfNxTGyOqwF3M/Y3LCppTN5THAySecKkILuS8gPY48
iQAuY3Zwx8NvuZ3sw+0+muwJ5Cj6Kd8B7XubU2zfdCnXsIsGtMA5ZpGnCJbaixWc
dCwJM6hB7io44vLTwOqx9Abk/mf2s9dYxl7eZG+hGyP19Q+xAvtz7bRKNndpGkaz
9GHcgTeQ50lVNPCCFqhTKv9/lurNzawWEgnGi6IKopH8KnWOUGVuYAjLp10xjIUN
NXfebjl15trnBo/lAo5Is9MVX9tD8+QKkO1XcJ9QxXqYPNLiaxZPR4lwPYkyfmOM
WZ5kMKx+WOMyMHMX8SqltinzrZaVi+IhY1MbCCJHyPUHsK7nwY3LOXuZTxLWIunT
qDPoOBGQ5T5GLd7j0g+kkHA1Ckf3cmq/nFrdk9nbXZcYAhgwBFgCEICi6LcRhLqb
5szzOe09kmzsDPEyeEmnoQGDG4r9fSqbUPYnVTozGZN8j05pOv2OVSNZBy8nzhT1
8mOsRN9L9WMkNY82Nwo4AgEe74/to9cLOHorYdcGfWgyoufABBh/tinOi4bMyDJs
EqBQsdA2cGp9egPHGloERhwSf170dxZLKNxifO0eQ47YAe4AF/IfQSEG0hmO2K3O
-----END RSA PRIVATE KEY-----
```

And after generation keypair I needed to exptract public key from it 

```bash
$ openssl rsa -in private.pem -outform PEM -pubout -out public.pem
Enter pass phrase for private.pem:
writing RSA key
$ cat public.pem 
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvULsictNS8k01LWSZSsP
h+47PU5XJycAQYNAVO18fjW21hlHd+j+RpGLJanRS7t8DTZHwMZWdhETdBtgWYWp
n9+xZHj+BnLkzhPaad1dmY3QTFj1KRJLaH/pKu/3a4uZjPxKeOL8Va7LhPnD8XQ/
6yvE1y95aHBik9XYkYCFfoySSdy+6UEAHURMp4McKJlzbGmAauIrNpeyxaEZYgiL
bxt4cTFR5SBWZf6xbCBlxETQSRUeRyQZMgWKR8i3R9xnaDjJRAVCl1Id2zb8ADRR
tqckZZ4X6N6vGDQazpzWbmFBlsVf/MVQwoky0YlZeTSKs6EboLjjWFyRNSK0eGhI
oQIDAQAB
```

To extract exponent and modulus I used command

```bash
$  openssl rsa -pubin -in rsa/public.pem -text -noout 
Modulus (2048 bit):
    00:bd:42:ec:89:cb:4d:4b:c9:34:d4:b5:92:65:2b:
    0f:87:ee:3b:3d:4e:57:27:27:00:41:83:40:54:ed:
    7c:7e:35:b6:d6:19:47:77:e8:fe:46:91:8b:25:a9:
    d1:4b:bb:7c:0d:36:47:c0:c6:56:76:11:13:74:1b:
    60:59:85:a9:9f:df:b1:64:78:fe:06:72:e4:ce:13:
    da:69:dd:5d:99:8d:d0:4c:58:f5:29:12:4b:68:7f:
    e9:2a:ef:f7:6b:8b:99:8c:fc:4a:78:e2:fc:55:ae:
    cb:84:f9:c3:f1:74:3f:eb:2b:c4:d7:2f:79:68:70:
    62:93:d5:d8:91:80:85:7e:8c:92:49:dc:be:e9:41:
    00:1d:44:4c:a7:83:1c:28:99:73:6c:69:80:6a:e2:
    2b:36:97:b2:c5:a1:19:62:08:8b:6f:1b:78:71:31:
    51:e5:20:56:65:fe:b1:6c:20:65:c4:44:d0:49:15:
    1e:47:24:19:32:05:8a:47:c8:b7:47:dc:67:68:38:
    c9:44:05:42:97:52:1d:db:36:fc:00:34:51:b6:a7:
    24:65:9e:17:e8:de:af:18:34:1a:ce:9c:d6:6e:61:
    41:96:c5:5f:fc:c5:50:c2:89:32:d1:89:59:79:34:
    8a:b3:a1:1b:a0:b8:e3:58:5c:91:35:22:b4:78:68:
    48:a1
Exponent: 65537 (0x10001)
```

Now to encrypt file with my name I used OpenSSL lib

```bash
$ cat name.txt 
Emil A. Sharifullin
$ openssl rsautl -encrypt -in name.txt -out encrypted_name  -pubin -inkey rsa/public.pem 
```

And I got this encrypted file

```
00000000:  5eaf ed1a 2602 7739 8df0 d983 3ee8 c735  :^...&.w9....>..5
00000010:  0538 afee 2bb3 71a4 8a3e b0a0 8885 78f3  :.8..+.q..>....x.
00000020:  ca5f 6714 27c0 f437 791e 85e6 9040 0e43  :._g.'..7y....@.C
00000030:  ab75 80f7 7d8f 9a2b 642f 3ee2 d972 8658  :.u..}..+d/>..r.X
00000040:  5a0d 25a8 4be2 6ac4 7892 6ce8 d294 b899  :Z.%.K.j.x.l.....
00000050:  3b55 a908 303d 3d3c 6d63 1610 7921 766d  :;U..0==<mc..y!vm
00000060:  b88c 64d3 89f2 5073 02e4 d4ef 089b 655e  :..d...Ps......e^
00000070:  d46e a245 89e3 d8d2 fd70 55bb ba91 007f  :.n.E.....pU.....
00000080:  0c06 e471 a42f 440e ad72 3c89 f8f9 2a5a  :...q./D..r<...*Z
00000090:  c67a de09 2ea7 9174 e24f 71ab a140 e2d8  :.z.....t.Oq..@..
000000a0:  ad46 ef8b 86bd 44f1 5a85 a3b8 63f3 0e3c  :.F....D.Z...c..<
000000b0:  ddbc e801 a8bf 4365 2230 d69f 0917 37cc  :......Ce"0....7.
000000c0:  c6a7 7870 bc21 bc9b 1a56 b73f 5ee3 5b4a  :..xp.!...V.?^.[J
000000d0:  1694 f208 2f55 ab29 29e9 2910 1ba0 0323  :..../U.)).)....#
000000e0:  6d4f eac1 95a0 1e46 5f94 2043 44c5 d897  :mO.....F_. CD...
000000f0:  7f33 99f2 38cf c94b c015 2418 8bfb 3f9f  :.3..8..K..$...?.
```



### Assuming that you are generating a 1024 bit RSA key and the prime factors have a 512bit length, what is the probability of picking the same prime factor twice ? Explain your answer. Hint: How many primes with length 512bit or less exist?

There is exists approximation to count number of prime numbers and it's
$$
\pi(n) = \frac{n}{\ln n}
$$
And according to this approximation $ \pi(2^{512}-1) = 1.3407807929942597e+154)$

```python
In [4]: 2**512-1/math.log(2**512-1, math.e)
Out[4]: 1.3407807929942597e+154
```

So probability is $P(A) = \frac{1}{1.3407807929942597e+154}$

### Explain why using a good RNG is crucial for the security of RSA. Provide one reference to a realworld case where a poor RNG lead to a security vulnerability.

With bad random number generator intruders can assume next generated p or q according to previous values of RNG. This can perform to comprometation of sensitive data.

### Here you can find the modulus (public information) of two related 1024bit RSA keys. Your keys are numbered using the list at http://188.130.155.61/ssn/Instructions.txt. Your task is to factor them i.e. retrieve p an q. You may use any tools for this. Explain your approach. Hints: study the RSA algorithm. What private information can two keys share? What practical attacks exist? You may have to write code or use existing code for simple arithmetic operations.

The modulos is a $n=pq$. If two keys are relative then they have one mutual p or q. To find this number we need to find GCD of keys

```python
from math import gcd
a = int('0x8459191b7ab5710e3d3d5a901ea4859032a0017d182049a37f643cb9e8a7700218aca2713512fed3a0591e32e97aa8b13cc6a08afbaca0a9dde77f808c15cba563466125910dda0c77c5a2f849c7245b54de02f31f31806743b71d4b0a2ca1d74631b09169ac8ee1b538a6f5356cd3b60d3e791326ddbcca546163c197365469', 16)
b = int('0xa8ce1d2c9cb72c50877a0b3c0a00eb5ba8d9871812acf61ef53af2e77dd7e1befd63ea2dd5b4c740a7cc83c8cbe7b59b0ccffa1ccf70e3ee8fcb6 b89dbe3b4fb4f5c5e046c3b8678075ff573fc34a4b5409e0f1b4b1a8b792abd1ff8a3f92260c9a8ae176e799c37ad0fa5105c2a38f06c92baf5190917b2ed21187792f141eb', 16)
gcd(a, b)
9594425659998056478309883943809061195083011864919537185550456855079985417816802975107872277560873098912167001528573985392980328726454437911178054657661797
```

And with known p we can find q for both keys

```python
In [17]: int(a/p)
Out[17]: 9686661516614391354318193460962571279340087464047355624829351181505663174132301882515483393522634363750181291908207894755972257473434370581852105652305920
In [16]: int(b/p)
Out[16]: 12354986067943916663888382472863061902512906350645978708318901688178670423776340945723212419284847204312187131990859180238078768448293559138208888360271872
```

### Now that you have the p and q for both keys, recreate the first public and private key using this script. Encrypt your name with the private key and post the public key and the base64 encrypted data in your report

