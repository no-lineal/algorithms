# anagram search

import numpy as np

def prime(i, primes):

    for prime in primes:
        if not (i == prime or i % prime):
            return False

    primes.append(i)

    return i

def historic_primes( n ):

    primes = []

    i, p = 2, 0

    while True:

        if prime(i, primes):
            p += 1
            if p== n:
                return primes
        i += 1

alphabet = 'abcdefghijklmnñopqrstuvwxyz'

n = len( alphabet )

primes = historic_primes( n )

letter_map = {}
for i, j in zip( alphabet, primes ):

    letter_map[i] = j

string_a = 'riesgo'
string_b = 'sergio'

print(f'\nstring a: {string_a}')
print(f'string b: {string_b}\n')

string_a = [ *map(letter_map.get, string_a) ]
string_b = [ *map(letter_map.get, string_b) ]

string_a = np.prod( string_a )
string_b = np.prod( string_b )

print(string_a, string_b)

print(f'anagrama: { string_a == string_b } ')
