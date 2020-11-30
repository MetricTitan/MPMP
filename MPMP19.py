"""
Optimisation buffers
"""

#Storage buffers to keep track of current primes and prime sqaure sums
primeDatabase = [False, True] #Indexes Zero and One are skipped used in the puzzle
primeSqrSumDatabase = [0]

# %%

"""
Function: Determine whether n is prime (return True)
"""
def isPrime(n):
    #Start at 2 (ignore zero and one)
    i = 2
    
    #While n is larger than the number compared to it (comparison from 0->n)
    while(n > i):
        #If the index i is greater than half of n, no perfect divisors found, n is prime, return True
        if(n < i * 2):
            return(True)
        #If a perfect divisor is found, n is not prime, return False
        if(not(n % i)):
            return(False)
        #No perfect divisor found, increment index
        i += 1
    #No perfect divisors found, return True for prime
    return(True)

"""
Function: Find the sum of the first m squared primes
"""
def addPrimeSquares(m):
    #Start index at the end of the database
    j = len(primeDatabase)
    
    #Loop until a prime is found
    while(1):
        #Check and store in database numbers until a prime is found
        primeDatabase.append(isPrime(j))
        
        if(primeDatabase[j]):
            #Append new square prime sum to the end of primeSqrSumDatabase
            primeSqrSumDatabase.append(primeSqrSumDatabase[len(primeSqrSumDatabase)-1] + j ** 2)
            #Return this value
            return(primeSqrSumDatabase[len(primeSqrSumDatabase) - 1])
        
        #Increment index if no prime is found
        j += 1

# %%

"""
Run analysis
"""

#Analyse upto and including this number
analysisCeiling = 5000

#Create result array to store solutions
result = []

#Run analysis from 1 to analysisCeiling (inclusive)
for k in range(1, analysisCeiling + 1):
    #Check if the first n prime squares sum to a multiple of n
    if(not(addPrimeSquares(k) % k)):
        #Append result if found
        result.append(k)
    #Print incremental progress towards analysis ceiling - comment out to run analysis faster (accumulative based on analysisCeiling)
    if(not(k % 500)):
        print(k)

"""
Print Result
"""

print(result)
