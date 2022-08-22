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
