#  Taking the two number input and swapping both numbers 

a=int(input("entr number one :"))
b=int(input("enter number two : "))

temp=a
a=b
b=temp

print(a,"a")
print(b,"b")



# Writing a program that gives sum of three digit 


num=int(input("enter num :"))

last_digit=num%10
middle_digit=(num//10)%10
first_digit=num//100
sum=first_digit+middle_digit+last_digit
print(sum)

