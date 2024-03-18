import math
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' '
]
def ascii_code(m):
    m.lower()
    return letters.index(m)
def Charecter(m):
    return letters[m]
def isprime(num):
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
            else:
                return True

    else:
        return False



def inverse(xx, nn):
  n = max(xx, nn)
  x = min(xx, nn)
  ttxt = "{} ' mod {} = "
  ttxt = ttxt.format(x, n)
  a = []
  b =[]
  c =[]
  d = []
  aa = n
  cc = x
  bb = math.floor(aa/cc)
  dd = aa%cc
  txt = "{} = {}*{} + {} "
  a.append(aa)
  b.append(bb)
  c.append(cc)
  d.append(dd)
  while dd > 0:
    aa = cc
    cc = dd
    bb = math.floor(aa/cc)
    dd = aa%cc
    a.append(aa)
    b.append(bb)
    c.append(cc)
    d.append(dd)
    #print(txt.format(aa,bb,cc,dd))
  s =["1", "0"]
  t = ["0", "1"]
  ss = int(s[0])-(int(s[1]))*(int(b[0]))
  tt = int(t[0])-(int(t[1]))*(int(b[0]))
  s.append(ss)
  t.append(tt)
  #print(ss,tt)
  i = len(a)
  z = 0
  while (i-2)>0:
    ss = int(s[1+z])-(int(s[2+z]))*(int(b[1+z]))
    tt = int(t[1+z])-(int(t[2+z]))*(int(b[1+z]))
    s.append(ss)
    t.append(tt)
    i -= 1
    z += 1
    #print(ss,tt)
  if tt < 0:
    tt = tt+n
  return tt


########################################################
def Generate_key(p, q):
    n = p * q
    phi = (p-1)*(q-1)
    e = find_e(phi)
    d = inverse(e, phi)
    print("Public key is e = " + str(e) + ", n = " + str(n))
    print("Private key is d = " + str(d) + ", n = " + str(n))
    return n, e, phi, d


########################################################
def rsa_encrypt(massage, n, e):
    massage = massage.lower()
    c = list()
    for i in massage:
        m = ascii_code(i)
        c.append(str((m**e) % n))
    c = ' '.join(c)
    return c


########################################################
def rsa_decrypt(ciphertext, n, d):
    m = list()
    ciphertext = ciphertext.split(' ')
    #print(ciphertext)
    for i in ciphertext:
        i = int(i)
        m.append(Charecter((int((i ** d) % n))))
    m = ''.join(m)
    return m

def gcd( a, h):
    while True:
        temp = a%h
        if temp == 0:
          return h
        a = h
        h = temp

def find_e(phi):
    e = 2
    while e<phi:
        d = gcd(e,phi)
        if d == 1:
            break
        else:
            e += 1
    return e
