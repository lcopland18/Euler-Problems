#Creating variable that can be used in a while function
number = 1

#So it knows what to print at the end
final = 0

#Because you want every number lower than 1000
while number < 1000:
#If number is dibisible by 3 or 5 and has no remainder (goes into it evenly)
    if number % 3 == 0 or number % 5 == 0:
#So you have the sum of all the numbers divisible by 3 or 5
        final = final + number
#making a new number so it keeps checking numbers up to 1000 (instead of only 1)
        number = number + 1
    else:
#making a new number so it keeps checking numbers up to 1000 (instead of only 1)
        number = number + 1
#printing the final number
print final
