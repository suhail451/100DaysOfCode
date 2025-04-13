print("Prime number filter ")

my_list=[2,3,4,6,7,8,9,12,324,56,78,34,]

def filter (list):
    for num in list:
        if num<2:
            continue
        for i in range(2,num):
                if num%i==0:
                 break
        else :
            print(num)


filter(my_list)


