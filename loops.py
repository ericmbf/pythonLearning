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