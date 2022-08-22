from re import X


name = "lemasani"
age =  23
weight = 80.5

print("My name is " + name + ", I am " + str(age) + " I weigh " + str(weight) + " kg.")

#loops assignment

# 1. print first 10 natural number
i = 1
while(i<=10):
    print(i)
    i += 1
    
# 2. calculate the sum of all numbers from 1 to a given number
sum = 1
j = 1
n = int(input("Enter N: "))
while(j<=n):
    sum = sum + j
    j += 1
    
print("the sum is: ", sum)

# 3. A program that prints muiltplication table of a given number
table = int(input("Enter the number:"))
k = 1
while(k<=11):
    product = table * k
    print(product)
    k += 1
# Write a program to display only those numbers from a list that satisfy the following conditions
 # - The number must be divisible by five
  #- If the number is greater than 150, then skip it and move to the next number
  #- If the number is greater than 500, then stop the loop
# given `numbers = [12, 75, 150, 180, 145, 525, 50]`
print("new line ")
given = [12, 75, 150, 180, 145, 525, 50]
for number in given:
    if ((number > 500) and (number % 5 ==0)):
        break
    if ((number > 150) and (number % 5 ==0)):
        
        continue
    if ((number % 5 ==0) and (number >= 12)):
        print(number)
        
# 5.  Write a program to count the total number of digits in a number using a while loop. given number `4673453`
# `4673453`
print("qn 5")
m = 4673453
while m > 0:
    print(len(str(m)))
    break

# 6. Display numbers from -10 to -1 using while loop
b = -10
while b <= -1:
    print(b)
    b += 1