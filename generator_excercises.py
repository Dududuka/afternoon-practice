#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.

def primes_gen():
    n = 1
    while True:
        n += 1
        for num in range(2, n+1):
            if n == num:
                yield n
            if n % num == 0:
                break

gen = primes_gen()
for _ in range(10):
    print(next(gen), end=' ')
# Expected output
# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------

#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.

def unique_letters(s):
  unique_chars = {}
  for ch in s:
    if ch not in unique_chars:
      unique_chars[ch] = 0
    unique_chars[ch] += 1
  for ch in unique_chars:
    yield ch

for letter in unique_letters('hello'):
    print(letter, end=' ')
# Expected output
# h e l o