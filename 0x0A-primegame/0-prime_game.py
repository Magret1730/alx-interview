#!/usr/bin/python3
"""
Prime game
"""

def isWinner(x, nums):
    """
    Function to determine the winner of a prime
    game session with `x` rounds.
    """
    def sieve(n):
        """
        Return a list of primes up to n (inclusive)
        using the Sieve of Eratosthenes
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] is True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def count_moves(n, primes):
        """ Return the number of prime moves possible for n """
        if n < 2:
            return 0
        primes_up_to_n = [p for p in primes if p <= n]
        return len(primes_up_to_n)

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        num_moves = count_moves(n, primes)
        if num_moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
