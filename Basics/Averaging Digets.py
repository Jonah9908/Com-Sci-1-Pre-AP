#Jonah Sims
#Averaging Digets




num = int(input("Enter a number: "))

num1 = num

num2 = num
sum = 0
count = 0
average = 0
while(num > 0):

    sum = sum + (num % 10)
    num = int(num / 10)
  

while (num1 > 0):
  num1 = num1//10
  count = count + 1

average = sum / count

print("The average of "+ str(num2) + " is " + str(average))






    
         