#  Program to find simple intrest when parametes are given 

principal_amout=int(input("Enter Principal Amount :"))
rate_intrest=int(input("Enter Rate of Intrest :"))
Time=int(input("Enter Time in Year :"))

def simple_intrest(x,y,z):
    simple_intrest=x+y+z/100
    print("Simple Intrest is ",simple_intrest)

simple_intrest(principal_amout,rate_intrest,Time)
