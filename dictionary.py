elements = {"Cristiano Ronaldo": 99, "Messi": 96, "Neymar": 93}
print(elements["Neymar"])

# Check test is element from dictonary
print(elements.get("Dybala"))

# Assign new value to element
elements["Neymar"] = 92

player = "Neymar"
print("{} get value: {}".format(player, elements[player]))

player = "Messi"
print("{} in {}: {}".format(player, elements, player in elements))

player = "Iniesta"
print("{} not in {}: {}".format(player, elements, player in elements))

#Using Identity Operators
exist = elements.get(player)
print("Check if {} is None: {}".format(player, exist is None))
print("Check if {} is not None: {}".format(player, exist is not None))

elements = {"Cristiano Ronaldo": 99, "Messi": 96, "Neymar": 93}
players = elements
suplents = {"Cristiano Ronaldo": 99, "Messi": 96, "Neymar": 93}

print("Check elements == players, using Equality: {}".format(elements == players))
print("Check elements is players, using Identity: {}".format(elements is players))
print("Check suplents == players, using Equality: {}".format(suplents == players))
print("Check suplents is players, using Identity: {}".format(suplents is players))