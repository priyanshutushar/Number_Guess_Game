# Import Libraries
import math # Used for doing mathematical operations
import random # Generates random number

# Taking inputs from user
lower_bound = int(input("Enter lower bound = "))
upper_bound = int(input("Enter upper bound = "))

#Generating random number between the lower bound and upper bound
x = random.randint(lower_bound,upper_bound)
print("You have only {} chances to guess !!".format(round(math.log(upper_bound-lower_bound+1,2))))

#Initializing the number of guesses
count = 0

#Guessing minimum number depending upon range
while count < math.log(upper_bound-lower_bound+1,2):
    count +=1 #count = count + 1
    
    #Taking guessing number from user as input
    guess = int(input("Enter guessing number = "))
    
    #Applying conditions 
    if x == guess:
        print("Congratulations you did it in {} chances".format(count))
        break
    elif x > guess:
        print("You guessed smaller number")
    elif x < guess:
        print("You guessed larger number")
    
    
if count >= math.log(upper_bound-lower_bound+1,2):
    print("The number is",x)
    print("Better Luck Next Time")
    
    
