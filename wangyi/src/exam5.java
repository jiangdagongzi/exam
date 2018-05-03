import java.util.Scanner;

public class exam5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int result = 0;

        for(int x= k; x<n;x++){
            for(int y = k; y<n; y++){
                if(x%y >= k)
                    result++;
            }
        }
        System.out.println(result);
    }
}
