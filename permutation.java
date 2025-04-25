import java.util.*;
public class permutation {
    public static void permutation(int n,int n_r){
          
            int permutation=n/(n_r);
                    
            System.out.println(permutation);
          
          }
    
    
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the question");
        String text_input=sc.nextLine();
        int input_digits[]=new int[text_input.length()];
        int digit_index=0;
        
        int asciiValue=0;
//        char digit=0;
        int number=0;
        
         for(int i=0;i<=text_input.length()-1;i++){
             char sentence=text_input.charAt(i);
             if(sentence >='1' && sentence <='9'){
              asciiValue=text_input.charAt(i);
              
              number=asciiValue-'0';
              input_digits[digit_index]=number;
              digit_index++;
                 
               
         }
             
             
         }
          if(digit_index>2){
              System.out.println("Sorry you are giving 3 digit in your question meanwhile we require 2 digit to operate :");}
          else{
//                System.out.println(array[1]);
        
          int n=input_digits[0];
          int r=input_digits[1];
          
          
          
          
          
          int nFactorial=1;
          for(int i=1;i<=input_digits[0];i++){
           nFactorial=nFactorial*i;
          
          } System.out.println("n "+nFactorial);
//         
//  
            
          
          int nMinusR=input_digits[0]-input_digits[1];
           int nMinusRFactorial=1;
          for(int i=1;i<=nMinusR;i++){
           nMinusRFactorial=nMinusRFactorial*i;
          
          } System.out.println("nMinusR"+nMinusRFactorial);
   
         
          
          if(n<r){
              System.out.println("Please make sure you are not giving first number n'Total combination' smaller than r 'at a time'");}
          {permutation(nFactorial,nMinusRFactorial);}  }
          
    }    
    
             
         
         

    
    
     

}
