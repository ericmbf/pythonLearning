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