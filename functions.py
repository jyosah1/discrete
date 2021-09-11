from math import *
import matplotlib.pyplot as plt

# defining empty array to store domain, range and inverse range values.
domainVal = []
rangeVal = []
inverseRangeVal = []

# function for calculation function
def calculateSomething(anyVal):
    calculatedVal = 1/(anyVal ** 2)
    return calculatedVal

# function for calculating inverse of the function
def caculateInverseOfSomething(anyVal):
    calculatedVal = 1/sqrt(anyVal)
    return calculatedVal

# loop to go through the loop of predefined range
for i in range(1, 100):
    domainVal.append(i)
    rangeVal.append(calculateSomething(i))
    inverseRangeVal.append(caculateInverseOfSomething(i))

# function to check if a function is one to one from the given array of domain and range
def isOnetoOneFunction(domain, range):
    uniqueValues = set(range)
    if (len(uniqueValues) == len(domain)):
        print("Is one to one function")
        return true
    print("Not one to one function")
    return false

# function to check if a function is onto from the given array of domain and range
def isOntoFunction(domain, range):
    uniqueValues = set(range)
    if (len(uniqueValues) <= len(domain)):
        print("Is onto function")
        return true
    print("Not onto function")
    return false

def isBijective(domain, range):
    if (isOntoFunction(domain, range) and isOnetoOneFunction(domain, range)):
        print ("Is Bijective")
        return true
    print("Not Bijective")
    return false

# Checking if the function is one to one, onto and bijective
isOntoFunction(domainVal, rangeVal)
isOntoFunction(domainVal, rangeVal)
isBijective(domainVal, rangeVal)

# plotting the range and inverse of the range\
plt.plot(domainVal, rangeVal)
plt.plot(domainVal, inverseRangeVal)
plt.xlabel('domain')
plt.ylabel('range')

plt.show()