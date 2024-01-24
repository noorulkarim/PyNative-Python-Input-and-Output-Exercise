# Exercise 4: Display float number with 2 decimal places using print()

num = float(input("Enter a number:"))
str_num = str(num)

for i in range(len(str_num)):
    if str_num[i] == ".":
        print(str_num[0 : i + 3])
