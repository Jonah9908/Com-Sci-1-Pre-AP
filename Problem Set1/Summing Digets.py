#Jonah Sims
#Summing Digits





num = int(input("Enter a number: "))

sum = 0

while(num > 0):

    sum = sum + (num % 10)
    num = int(num / 10)

    
print(int(sum))            