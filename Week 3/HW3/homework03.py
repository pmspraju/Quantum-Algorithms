# imports {{{1
from random import randrange
#---------------------------------------------------------------------------}}}1

def primes(n): # {{{
  P = []
  for k in range(2, n+1):
    k_is_prime = True
    for d in P:
      if d > k**0.5:
        break
      if k % d == 0:
        k_is_prime = False
        break
    if k_is_prime:
      P.append(k)
  return P
#----------------------------------------------------------------------------}}}

def is_prime_MR(q): # {{{
  # Fill in each step (as outlined in class or the textbook) below the relevant
  # comment.
  #
  # At Step 3, you will need to produce a random element of {1, ..., q-1}. Use
  # randrange() to do this: a = randrange(1, q). Note that modulus in python is
  # positive, so -1 should be represented as q-1.

  if q <= 1:
    return False

  # Step 1

  # Step 2

  # Step 3

  # Step 4

  # Test 1

  # Test 2

#----------------------------------------------------------------------------}}}
