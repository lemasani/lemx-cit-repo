from typing import Counter


age = 18
#your_age = int(input("Enter your age: "))
#if your_age >= age:
    #print("pls proceed")
#else:
   # print("below the age requirement setted")
    
#for loops session
fruits = ["apple", "banana", "cherry"]
for  fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)
    
print(list(range(5)))

#starting_point, stopping_point, step_number
for num in range(0, 21, 2):
    print(num)
    
#for odd numbers
for num in range(1, 21, 2):
    print(num)
    
for i in range(len(fruits)):
    print("current fruit : ", fruits[1])
    
digits = [0, 1, 2, 4]
for digit in digits:
    print(digit)
else:
    print("noo items left")
    

#
student_name = "brian"
marks = {'james': 90, 'jules': 92}
for student in marks:
    if student == student_name:
        print("thanks ")
        break
else:
    print("repeat again")
    


#while loop

#initialize sum and counter
sum = 0
counter = 1

n = int(input("Enter n: "))
#calculate sum of the first n natural numbers
while counter <= n:
    sum = sum + counter
    counter = counter + 1
#display sum
print("the sum is : ", sum)

counter_1 = 0

while counter_1 < 4:
    print("inside loop")
    counter_1 = counter_1 + 1
    break
    print("inside")
    
# Use of break statement inside the loop

for val in "Python":
    if val == "h":
        break
    print("mmh give space", val)

# Use of continue statement inside the loop

for val in "Python":
    if val == "h":
        continue
    print(val)