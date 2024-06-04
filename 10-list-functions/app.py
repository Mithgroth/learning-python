lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print(friends.count("Jim"))
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.sort()
print(friends)

lucky_numbers.sort(reverse=True)
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends.extend(lucky_numbers)
print(friends)

# Remove the last element
friends.pop()
print(friends)

print(friends.index("Kevin"))

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)