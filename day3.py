# Num to check if odd or even 

num=int(input("Enter th enumber "))

if(num%2==0):
    print(num," is even")
elif(num%2!=2)    :
    print(num," is odd")



#Take three digit input and reverse it also check if it is correc are not  

num=int(input("enter four digit number "))
last_digit=num%10
middle_digit=(num//10)%10
first_digit=num//100
reversed_num=(last_digit*100)+(middle_digit*10)+first_digit
print(reversed_num)
num2=str(num)
num3=num2[::-1]
reversed_num2=str(reversed_num)
print(num3)
if(num3==reversed_num2):
    print("yes num is reversed correctly")
else :
    print("no they are not equal ") 