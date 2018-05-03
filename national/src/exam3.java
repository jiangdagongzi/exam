import java.util.Arrays;
import java.util.Scanner;

public class exam3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int s = scanner.nextInt();
        int[] p = new int[n];
        for (int i = 0; i < n; i++) {
            p[i] = scanner.nextInt();
        }
        Arrays.sort(p);
        int sum = 0;
        int num = 0;
        int temp = 0;
        while (sum < s) {
            sum = sum + p[temp];
            temp++;
            num++;
        }
        for (int i = temp; i >= 0; i--) {
            if (sum - p[i] >= s) {
                num  --;
                sum = sum -p[i];
            }
            else continue;
        }

        System.out.print(num);
        return;
    }
}
