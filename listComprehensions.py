names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# [x**2 for x in range(9) if x % 2 == 0 else x + 3]
first_names = [name.split(" ", 1)[0].lower() for name in names] # write your list comprehension here
print(first_names)

multiples_3 = [n*3 for n in range(21) if n*3 >= 3]# write your list comprehension here
print(multiples_3)

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]  # write your list comprehension here
print(passed)