names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for index in range(len(names)):
    usernames.append(names[index].lower())
    usernames[index] = usernames[index].replace(" ", "_")


print(usernames)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == "<" and token[(len(token) - 1)] == ">":
        count += 1

print(count)

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key, value in basket_items.items():
#if the key is in the list of fruits, add the value (number of fruits) to result
    for fruit in fruits:
        if key == fruit:
            result += value

print(result)

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.


# WRONG WAY **************************************
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
isFruit = False

#Iterate through the dictionary
for key, value in basket_items.items():

    isFruit = False
#if the key is in the list of fruits, add the value (number of fruits) to result
    for fruit in fruits:
        if key == fruit:
            fruit_count += value
            isFruit = True

#if the key is in the list of fruits, add to fruit_count.
    if (not isFruit):
        not_fruit_count += value
    

print(fruit_count, not_fruit_count)

# CORRECT WAY **************************************
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit, count in basket_items.items():
    if fruit in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} items that are not fruits.".format(fruit_count, not_fruit_count))

# number to find the factorial of
number = 6   

# start with our product equal to number
product = number

# write your while loop here
while number > 1:
    # decrement number with each iteration until it reaches 1
    number -= 1
    # multiply the product so far by the current number
    product *= number

# print the factorial of number
print(product)

# number to find the factorial of
number = 6   

# start with our product equal to number
product = number

# write your while loop here
while number > 1:
    # decrement number with each iteration until it reaches 1
    number -= 1
    # multiply the product so far by the current number
    product *= number

# print the factorial of number
print(product)

#*************************************
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here 
for headline in headlines:
    
    news_ticker += headline + " "
    
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)