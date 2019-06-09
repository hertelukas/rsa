p = input("Calculate a random n (and e) under: ")

primes = []

with open('output.txt', 'r') as f:
    for line in f:
        primes.append(int(line))

for z in primes:
    print(z)