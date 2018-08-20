# Car size
vehicleSize = 20

smallCarSize = 5
normalCarSize = 10
BigCarSize = 20

fareNormalCar = 15
fareBigCar = 18.9
fareSmallCar = 10

fareValue = 0

if vehicleSize <= smallCarSize:
    fareValue = fareSmallCar
elif vehicleSize > smallCarSize & vehicleSize <= normalCarSize:
    fareValue = fareNormalCar
else:
    fareValue = fareBigCar

print("The fare car is {} to {} car size!".format(fareValue, vehicleSize))

points = 0

points = 200  # use this input to make your submission
prize = ""

# write your if statement here
if points <= 50:
    prize = "wooden rabbit"
elif points > 50 and points <= 150:
    result = "Oh dear, no prize this time."
elif points > 150 and points <= 180:
    prize = "wafet-thin mint"
elif points > 180:
    prize = "penguin"
    
if(prize != ""):
    result = "Congratulations! You won a {}!".format(prize)

print(result)