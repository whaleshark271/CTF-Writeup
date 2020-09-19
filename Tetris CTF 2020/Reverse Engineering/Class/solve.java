public class HelloWorld{

     public static void main(String []args){
        int[] arrayOfInt = { 
        172, 171, 157, 163, 152, 158, 178, 159, 152, 154, 
        159, 160, 170, 167, 160, 165, 150, 159, 152, 154, 
        159, 160, 174, 160, 165, 180 };
        
        for (int b = 0; b < 26; b++) {
            System.out.print((char)(arrayOfInt[b]-55));
        }
     }  
}