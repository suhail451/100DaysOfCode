problem=input("enter the problem : ")
for char in problem:
    if(char.isdigit()):
        n=int(char)
        
    


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
    


permutation=factorial(n)
print(permutation)

print("thank you ")