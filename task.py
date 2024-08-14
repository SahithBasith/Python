# 1. Add item to the specific place in the list
# Add berry in next to the banana and print the list
# Input:  ["apple", "banana", "cherry"]
# Output:  ["apple", "berry", "banana", "cherry"]


addfruit=["apple","banana","cherry"]
addfruit.insert(1,"berry")
print(addfruit)

# 2. Remove an item from the list
# Remove cherry from the list
# Input:  ["apple", "banana", "cherry", "banana", "kiwi"]
# Output:  ["apple", "banana", "banana", "kiwi"]

removefruit=["apple","banana","cherry","banana","kiwi"]
removefruit.remove("cherry")
print(removefruit)

# 3. copy few items from a list to another list
# copy "kiwi" and "melon" from one list to another an print it 
# Input:  ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Output: ["kiwi", "melon"]

copyTwoItemsFromList=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
result=copyTwoItemsFromList[4:6]
print(result)

# 4. copy few items from a list to another list
# copy "kiwi",  "melon" and "mango" from one list to another an print it 
# Input:  ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Output: ["kiwi", "melon", "mango"]

copyThreeItemsFromList=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
res=copyThreeItemsFromList[4:7]
print(res)

# 5. Replace item in the list
# replace "banana" to "berry"
# I/P: ["apple", "banana", "cherry"]
# O/P: ["apple", "berry", "orange"]

replaceBananaToBerry=["apple", "banana", "cherry"]
replaceBananaToBerry[1]="berry"
print(replaceBananaToBerry)

# 6. Replace item in the list
# replace "cherry" to "orange"
# I/P:  ["apple", "banana", "cherry"]
# O/P:  ["apple", "banana", "orange"]

num5=["apple", "banana", "cherry"]
num5[2]="orange"
print(num5)
