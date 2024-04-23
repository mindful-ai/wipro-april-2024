
# sorting by number of vowels
fruits = ["Apple", "Banana", "Cherry", "Melon", "Strawberry", "Orange"]
 
def count_vowels(word):
    count = 0
    for char in word:
        if char.lower() in "aeiou":
            count += 1
    return count
 
sorted_fruits = sorted(fruits, key=count_vowels)
 
print("Sorted fruits by the number of vowels:", sorted_fruits)


