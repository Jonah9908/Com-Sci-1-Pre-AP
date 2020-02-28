Python 3.7.6rc1 (tags/v3.7.6rc1:bd18254b91, Dec 11 2019, 20:31:07) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Jonah Sims
#Summing Digits
    #Enter a num
    num = int(input("Enter a number: "))

    sum = 0

while(num > 0):

    sum = sum + (num % 10)
    num = int(num / 10)

    
print(int(sum))