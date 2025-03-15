#  Program to find simple intrest when parametes are given 
import math as m

principal_amout=int(input("Enter Principal Amount :"))
rate_intrest=int(input("Enter Rate of Intrest :"))
Time=int(input("Enter Time in Year :"))

def simple_intrest(x,y,z):
    simple_intrest=x+y+z/100
    print("Simple Intrest is ",simple_intrest)

simple_intrest(principal_amout,rate_intrest,Time)


#  Program to find the colume of the cylinder and cost of milk can be filled


radius=int(input("Enter the radius of base :"))
height=int(input("Enter the height of cylinder :"))

def volume(a,b,c):
    volume=a*(b**2)*c
    print("volume of cylinder is ",volume)

price=40
def cost(v,price):
    cost=volume * price
    print("cost is",cost)

volume(radius,m.pi,height)

cost(volume,price)