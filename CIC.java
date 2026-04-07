import java.util.Scanner;
public class CIC{
    public static void main(String[] args){

        //Compound Interest Calculator

        Scanner scanner=new Scanner(System.in);

        double principal;
        double rate;
        int time;
        int years;
        double amount;

        System.out.println("Enter the principal amount : ");
        principal=scanner.nextDouble();

        System.out.println("Enter the rate of interest : ");
        rate=scanner.nextDouble()/100;

        
        System.out.println("Enter the number of times the interest is compounded per year : ");
        time=scanner.nextInt();

        System.out.println("Enter the number of years : ");
        years=scanner.nextInt();
        
        amount=principal*(Math.pow((1+rate/time),time*years));
        System.out.printf("The amount after  %d years is : %.2f",years,amount);
       
        scanner.close();
    } 
}
