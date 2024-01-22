# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
# Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.


def combine_string(words):
    for i in words:
        if i == words[-1]:
            print(i, end="")
            break
        print(i, end="**")


words = []
n = ""

while n != "end":
    n = input("Enter a word:")
    words.append(n)

words.pop(-1)
combine_string(words)
