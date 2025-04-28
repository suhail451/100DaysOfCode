import os

class User :
    def __init__(self,name,log):
        self.name=name
        self.log=log
        

class Workout:
    def __init__(self,type,duration,calories):
        self.type=type
        self.duration=duration
        self.calories=calories




name=input("\tEnter your name please : ")
log=[]
user1=User(name,log)

exit=-1
while(exit==-1):
    
    print("\tCHOSE ONE OF THE FOLLOWING OPERATION ")
    choice=int(input("\t\t1 Add workout \n\t\t2 View Summary \n\t\t3 Exit\n"))
    if(choice==1):
        type=input("\t\tEnter the Workout type : ")
        duration=int(input("\t\tEnter the workout duration in hours : "))
        calories=int(input("\t\tEnter the calories you burned : "))
        mywork=Workout(type,duration,calories)
        log.append(mywork)
        print("\tWORKOUT ADDED THANK YOU")
    
    if(choice==2):
        cal=0
        time=0
        if len(log) == 0:
            print("\tNo workouts recorded yet.")
        else:
            for i in range(len(log)):
                mywork=log[i]
                print("\tWorkout type:", mywork.type)
                print("\tDuration:", mywork.duration, "hours")
                print("\tCalories burned:", mywork.calories)
                cal += mywork.calories
                time += mywork.duration
            print("\tTotal calories:", cal)
            print("\tTotal time:", time, "hours")   

    if(choice==3):
        exit=1 
        print("\tGoodbye, " + name + "!")   
