# python code for find if given year is leap year or not 
import math
# year=int(input("Enter the year :"))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("It is leap year")
# else :
#     print("it is not an leap year")


# code to find shortest distance in two locatoins

x1,y1=map(int,input("Enter the x 1 and y1 co ordinate").split())
x2,y2=map(int,input("Enter the x 2 and y2 co ordinate").split())

shortest_ditance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("here is the shortest distance :",shortest_ditance)




