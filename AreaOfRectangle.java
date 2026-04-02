import java.util.Scanner;
public class AreaOfRectangle {
    public static void main(String[] args){
        
        //Area of rectangle
        double width=0;
        double height=0;
        double area=0;
        
        Scanner scanner=new Scanner(System.in);
        
        System.out.println("Enter the width : ");
        width=scanner.nextDouble();

        System.out.println("Enter the height : ");
        height=scanner.nextDouble();

        area =height*width;
        System.out.println("The area of recatngle is : "+area+"cm²");

        scanner.close();
    }
    
}
