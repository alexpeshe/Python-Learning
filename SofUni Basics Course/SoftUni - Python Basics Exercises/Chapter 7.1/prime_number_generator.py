# Advanced Prime Generator with Optimization

# Class Definition
class PrimeGenerator:
    """
    Comprehensive Prime Number Generator with multiple methods
    """
    # Constructor Method
    def __init__(self, limit=None):
        # Initialize the limit (optional parameter)
        # If no limit is provided, it defaults to None
        self.limit = limit
        
        # Create an empty list to store prime numbers (if needed)
        # The underscore suggests this is a private/internal list
        self._primes = []
    
    # Prime Checking Method
    def is_prime(self, n):
        """
        Optimized prime checking
        """
        # If number is less than 2, it's not prime
        if n < 2:
            return False
        
        # 2 and 3 are prime numbers
        if n == 2 or n == 3:
            return True
        
        # Quickly eliminate even numbers and multiples of 3
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        # Optimized prime checking algorithm
        # Start checking from 5, increment by 6
        # This is based on the 6k ± 1 optimization
        i = 5
        
        # Check up to the square root of the number
        while i * i <= n:
            # Check if number is divisible by current number or next number
            if n % i == 0 or n % (i + 2) == 0:
                # If divisible, it's not prime
                return False
            
            # Jump to next potential prime candidate
            # This skips many unnecessary checks
            i += 6
        
        # If no divisors found, the number is prime
        return True
    
    # Method to generate primes in a specific range
    def generate_primes_range(self, start, end):
        """
        Generate primes within a specific range
        """
        # List comprehension to generate primes
        # max(2, start) ensures we start from at least 2
        # end + 1 to include the end number
        # Uses is_prime method to check each number
        return [num for num in range(max(2, start), end + 1) if self.is_prime(num)]
    
    # Method to generate first n prime numbers
    def generate_first_n_primes(self, n):
        """
        Generate first n prime numbers
        """
        # Empty list to store prime numbers
        primes = []
        
        # Start checking from 2
        num = 2
        
        # Continue until we find n prime numbers
        while len(primes) < n:
            # Check if current number is prime
            if self.is_prime(num):
                # If prime, add to the list
                primes.append(num)
            
            # Move to next number
            num += 1
        
        # Return the list of first n primes
        return primes
    
    # Infinite prime number generator
    def infinite_prime_generator(self):
        """
        Infinite prime number generator
        """
        # Start from 2
        num = 2
        
        # Infinite loop
        while True:
            # If number is prime
            if self.is_prime(num):
                # Yield the prime number
                # 'yield' makes this a generator function
                yield num
            
            # Move to next number
            num += 1

# Example Usage Section

# Create an instance of PrimeGenerator
prime_gen = PrimeGenerator()

# Generate and print primes between 10 and 50
print("Primes between 10 and 50:", prime_gen.generate_primes_range(10, 50))

# Generate and print first 10 prime numbers
print("First 10 primes:", prime_gen.generate_first_n_primes(10))

# Create an infinite prime generator
infinite_primes = prime_gen.infinite_prime_generator()

# Print first 10 primes from infinite generator
print("Infinite Prime Generator:")
for _ in range(10):
    # 'next()' gets the next prime from the generator
    print(next(infinite_primes), end=' ')
# alternatives

'''
Key Concepts Explained:

Class Structure
Defines a comprehensive prime number generator
Multiple methods for different prime generation scenarios
is_prime Method
Optimized prime checking algorithm
Uses 6k ± 1 optimization for efficiency
Checks divisibility up to square root
Range Generation Method
Uses list comprehension
Generates primes within a specified range
First N Primes Method
Finds first n prime numbers
Uses a while loop for generation
Infinite Generator
Uses 'yield' to create a generator
Can generate primes indefinitely
Optimization Techniques
Skips even numbers
Skips multiples of 3
Checks only up to square root
6k ± 1 optimization
Recommended Improvements:

Add input validation
Handle edge cases
Implement caching for repeated calls
Add type hinting
Create more robust error handling
'''
'''
1. Basic Prime Number Generator (Simple Method)

def is_prime(n):
    """
    Check if a number is prime
    Time Complexity: O(√n)
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes_simple(limit):
    """
    Generate prime numbers up to a given limit
    """
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
print(generate_primes_simple(50))
'''

'''
2. Sieve of Eratosthenes (Most Efficient for Large Ranges)

def sieve_of_eratosthenes(limit):
    """
    Efficient prime number generator
    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    """
    # Create a boolean array "is_prime[0..limit]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve algorithm
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    # Collect prime numbers
    primes = [num for num in range(2, limit + 1) if is_prime[num]]
    return primes

# Example usage
print(sieve_of_eratosthenes(50))
'''

'''
3. Generator Function (Memory Efficient)

This approach is useful when dealing with large ranges and you want to generate prime numbers on the fly.

def prime_generator(limit):
    """
    Generator function for prime numbers
    Yields primes one at a time
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while num <= limit:
        if is_prime(num):
            yield num
        num += 1

# Example usage
for prime in prime_generator(50):
    print(prime, end=' ')
'''

'''
5. Miller-Rabin Primality Test (For Large Numbers)

import random

def miller_rabin(n, k=5):
    """
    Probabilistic primality test
    Highly accurate for large numbers
    """
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    
    # Write n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Example usage
def generate_large_primes(count, min_value=10**6, max_value=10**7):
    primes = []
    while len(primes) < count:
        candidate = random.randint(min_value, max_value)
        if miller_rabin(candidate):
            primes.append(candidate)
    return primes

print("Large Primes:", generate_large_primes(5))

'''

'''
Comprehensive Comparison:

Simple Method
Pros: Easy to understand
Cons: Inefficient for large numbers
Best for: Small ranges, learning
Sieve of Eratosthenes
Pros: Very efficient for medium ranges
Cons: High memory usage
Best for: Generating primes up to 10^6
Generator Function
Pros: Memory efficient, lazy evaluation
Cons: Slower for large ranges
Best for: Iterative processing
Advanced Generator
Pros: Multiple generation methods
Cons: More complex
Best for: Flexible prime number generation
Miller-Rabin
Pros: Accurate for large numbers
Cons: Probabilistic (small chance of error)
Best for: Cryptography, large number testing
Recommendations:

Choose method based on use case
Consider performance needs
Validate input ranges
Use appropriate optimization techniques
Key Considerations:

Time complexity
Space complexity
Accuracy
Specific use case requirements
'''