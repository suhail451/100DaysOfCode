
abstract class person{
 String name;
 int id;

abstract void displayInfo();
    


}
class student extends person{
 private double gpa;
 private int cource;
 
// constructor of stduent
 student(String name,int id){
 
 this.name=name;
 this.id=id;
                            }
 
 public double getgpa(){
         return this.gpa;
                       }
 public void setgpa(double gpa){
  this.gpa=gpa;
                               }
 
 public int getcource(){
         return this.cource;
                       }
 public void setcource(int cource){
  this.cource=cource;
                                  }
 
 
 @Override
 void displayInfo(){
    System.out.println(this.name);
    System.out.println(this.id);
    setgpa(2.9);
    System.out.println(getgpa());
    setcource(6);
    System.out.println(getcource());
                  }
 

    } 
class teacher extends person{

 private int salary;
 private int subject;
 
 
// constructor of teacher 
 teacher(String name,int id){
 
 this.name=name;
 this.id=id;
                           }
 
 public int getsalary(){
         return this.salary;
                     }
 public void setsalary(int salary){
  this.salary=salary;
                                   }
 
 public int getsubject(){
         return this.subject;
                       }
 public void setsubject(int subject){
  this.subject=subject;
                                    }
 
@Override
 void displayInfo(){
    System.out.println(this.name);
    System.out.println(this.id);
    setsalary(6000);
    System.out.println(getsalary());   
    setsubject(4);
    System.out.println(getsubject());
                  }

}


public class fourPilars {
    
    
    public static void main(String[] args) {
        System.out.println("THE MAIN CODE EXECUTION START HERE :");
        
        System.out.println("Student");
//        object of student
        student std=new student("suhail",30);
        std.displayInfo();
              
        System.out.println("teacher");
        
//        object of teacher
       teacher th=new teacher("Rizwan",45);
       th.displayInfo();
                
            
    }
    
    
}
