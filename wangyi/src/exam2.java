import java.util.Scanner;

public class exam2 {
    public static void  main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] lengths = new int[n];
        String[] roads = new String [n];

        for( int i = 0; i<n ;i ++){
            lengths[i] = scanner.nextInt();
            roads[i] = scanner.nextLine();
        }

        return;
    }
}

