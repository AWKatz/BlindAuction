# Day 9 of 100 for the Udemy Python Bootcamp

# Dictionary intro
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "New Item": "This is a new keypair item in the dictionary."
}
# Retrieve from the dictionary
print(programming_dictionary["New Item"])

# Add item into the dictionary
NewKey = input("Enter the new item: ")
KeyDesc = input("Enter the item description: ")
programming_dictionary[NewKey] = KeyDesc

print(programming_dictionary)

# Edit an item into the dictionary
programming_dictionary["Bug"] = ""

# Loop through items in the dictionary get the key, and then the value associated
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])