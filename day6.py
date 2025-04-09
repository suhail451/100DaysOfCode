#  Program to find simple intrest when parametes are given 
import math as m

principal_amout=int(input("Enter Principal Amount :"))
rate_intrest=int(input("Enter Rate of Intrest :"))
Time=int(input("Enter Time in Year :"))

def simple_intrest(x,y,z):
    simple_intrest=(x*y*z)/100
    print("Simple Intrest is ",simple_intrest)

simple_intrest(principal_amout,rate_intrest,Time)


#  Program to find the colume of the cylinder and cost of milk can be filled


radius=int(input("Enter the radius of base :"))
height=int(input("Enter the height of cylinder :"))

def volume(a,b):
    volume_cal=m.pi * (a**2) * b
    return volume_cal
    
cylinder_volume=volume(radius,height)
print("Volume of cylinder is : ",cylinder_volume)

pricePerLeter=40

def cost(cylinder_volume,price):
    milk_cost= cylinder_volume * pricePerLeter
    return milk_cost

print("Cost of cylinder is : ",cost(cylinder_volume,pricePerLeter)," $")



