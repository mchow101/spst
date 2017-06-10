import java.util.scanner;

public class SpeciesDiversity {
    public static void main(String[]args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("How many species? ");
        int species = scan.nextInt();
        int N = 0;
        int[] n = new int[species];
        for(int i = 0; i < species; i++) {
            System.out.print("Enter the number of organisms from species #" + i + " ");
            n[i] = scan.nextInt();
            N += n[i];
        }
        
        int sum = 0;
        for(int i = 0; i < n.length; i++) {
            n[i] = (n[i])*(n[i] - 1);
            sum += n[i];
        }
        
        double index = (double)(sum)/(double)(N*(N - 1));
        System.out.println();
        System.out.println("The Simpson's Diversity Index is " + (1.0 - index));
    }
}
