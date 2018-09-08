import java.util.Scanner;

public class exam1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int c = 1000000007;
        int i = 0;
        int result = 100001;
        int pos;
        while (i < 3) {
            pos = a;
            for (int j = 0; j < i; j++) {
                pos = 4 * pos + 3;
                if (pos % c == 0) {
                    result = result > i ? i : result;
                    break;
                }
            }

            int j;
            for (j = 1; j < 100001 - i; j++) {
                pos = 8 * pos + 7;
                if (pos % c == 0) {
                    result = result > (i + j) ? i + j : result;
                    break;
                }
                pos = pos % c;
            }
            i++;
        }
        System.out.println(result);
    }
}
