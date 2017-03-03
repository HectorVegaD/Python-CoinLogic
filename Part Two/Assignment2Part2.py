#Hector De La Vega
#Assignment 2 Part 2
#CECS 424
import math

myNumList = []

##Is prime will check to see if a given value is a prime
##number or not. We will check possible divisor numbers for a given
##value starting at 3 and ending at the floor(sqrt(value)). This is
##done to speed up our loop that iterates through and checks the
##possible divisors. It works because there will be no possible number
##x that is greator than the floor(sqrt(value)) and that will give us
##value%x == 0.
def is_prime(value):
    maxDivisor = math.floor(math.sqrt(value))
    if(value == 2 or value == 3):
        return True
    if(value % 2 == 0):
        return False
    numberIndex = 3
    
    while(numberIndex <= maxDivisor):
        if(value % numberIndex == 0):
            return False
        #because we don't check even numbers, the numbers
        #checked will be odd, and thus we start at 3 and increment by 2
        numberIndex += 2

    #If we overshoot the maxDivisor by one:
    #or if we are dealing with value of 1 (not prime) This check can
    #break func if value is 3, so have a base case and return True if value is 3.
    if(value % maxDivisor == 0):
        return False

    return True

##This function will generate all the prime numbers that exist starting
##at the given value and ending at the value of 2000000. Those values
##will be saved in a myNumList List.
def get_primes(startValue):
    global myNumList
    while(startValue < 2000000):
        if(is_prime(startValue)):
            myNumList.append(startValue)
        startValue += 1

##This function will iterate through the myNumList generated and add up
##all the prime numbers that were generated, Then it will print the result.
def sum_primes():
    global myNumList
    totalValue = 0
    for value in myNumList:
        totalValue += value

    print(totalValue)

##This is the main, user input for the starting value will be done here,
##then the remainder of the functions will be called from here.
def main():
    startValue = -1
    while(startValue < 0 or startValue > 2000000):
        print('Please input the starting value from 0 to 2000000')
        startValue = int(input(''))
    print('Calculating...')
    get_primes(int(startValue))
    sum_primes()
    print('Press \'Enter\' to exit...')
    input('')
    
##Define the main function.
if __name__ == '__main__':
          main()
