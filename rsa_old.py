import math
import time
e = input("Give an input for e: ")
n = input("Give an input for n: ")
m = input("Give a message to encrypt or decrypt: ")

start = time.time()
n = int(n)
e = int(e)
m = int(m)

#Encrypt
c = (int(m)**int(e))%int(n)

print("The encrypted message is: " + str(c))

#Decrypt
c = int(m)
p = 1
q = 1

n = int(n)
x = 1
i = 1
primes = []
primes.append(2)
isprime = True
check = True
delete = True

while x <= n:
    if len(primes) > i:
        while primes[i] <= math.sqrt(x) and check:
            if x % primes[i] == 0:
                isprime = False
                check = False
            elif i+1 < len(primes):
                i += 1
            else:
                check = False
        if isprime:
            primes.append(x)
            if delete:
                del primes[0]
                delete = False
    x += 1
    i = 0
    isprime = True
    check = True

u = 0
v = 0
print("There are " + str(len(primes)) + " primes")

while primes[u]*primes[v] != n and u < len(primes)-1:
    u+=1
    v=1
    while (primes[u]*primes[v] != n) and v < len(primes)-1:
        v+=1

p = primes[u]
q = primes[v]
print("p=" + str(p) + " q=" + str(q))

phin = (p-1) * (q-1)

d=1
while (e*d)%phin != 1:
    d+=1

print("d= " + str(d))
m = (c**d)%n
print("The message is: " + str(m))

end = time.time()
print(str(end-start) + " seconds to calculate")
