import java.util.Random;
public class RandomNumbers {
    public static void main(String[] args){

        Random random = new Random();
        //Random Integer
        int number1;
        int number2;
        int number3;
        
        number1=random.nextInt(18,33);
        number2=random.nextInt(7,45);
        number3=random.nextInt(10,93);
        
        System.out.println(number1);
        System.out.println(number2);
        System.out.println(number3);

        System.out.print("\n");

        //Random Double

        double number4;

        number4=random.nextDouble(3,7);

        System.out.print(number4);
        
        System.out.print("\n");
        System.out.print("\n");


        //Random Boolean

        Boolean isHeads;

        isHeads=random.nextBoolean();

        System.out.print(isHeads);
        System.out.print("\n");
        System.out.print("\n");
        
        if(isHeads){
            System.out.println("HEADS");
        }
        else{
            System.out.println("TAILS");
        }


    }
    
}
