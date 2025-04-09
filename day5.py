# # code to find if given angle can form triangle or not 

a,b,c=map(int,input("Enter three angles :").split())
if a>0 and b>0 and c>0 and (a+b+c==180):
    print("This is a triangle")
else :
    print("This is not a triangle")    

#  finding out if it is loss or profit 

selling_price,cost_price=map(int,input("Enter selling price : than cost price ").split())

if (selling_price>cost_price):
    print("it is",selling_price-cost_price,"$ profit")
elif (cost_price>selling_price):
    print("it is",cost_price-selling_price,"$ loss") 
else :
      print("No loss No Profit")       