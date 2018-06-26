print "This is Python programming!" + "\n"

# variable in python
greenApple = 2 
redApple = 3 # data type: integer

totalApple = greenApple + redApple

# print information to console
print ('The total number of apples: ' + str(totalApple) + "\n")




# declare a function using the keyword 'def'
def totalApplePrice(totalGreenApple, totalRedApple):
    greenUnitPrice = 0.15 # this data type is know as 'float'
    redUnitPrice = 0.12

    totalPrice = (totalGreenApple * greenUnitPrice) + (totalRedApple * redUnitPrice)
    return ("The total price is: " + str(totalPrice) + "\n")

print totalApplePrice(greenApple, redApple)

