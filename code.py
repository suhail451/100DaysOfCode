# problem one Finding the greatest Number in three

one=int(input("entr the input one"))
two=int(input("Enter the input two "))
three=int(input("enter the third input"))

if one >two and one>three:
    print(one,"is the greteast") 
if  two >one and two>three: 
    print(two,"is the greater") 
if  three >one and three>two: 
    print(three,"is the greater")     


#  problem two  Celcius to farenhight conversion
print("celcius to farenhight converter")

celcius=int(input("enter the celcius temprature"))
farenhight=(celcius* 9/5)+32 
print(celcius," is ",farenhight)