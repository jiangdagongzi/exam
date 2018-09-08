import java.util.*;

public class exam3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        HashSet set = new HashSet();
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
            set.add(arr[i]);
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            int num = 0;
            for (int j = i; j < n; j++) {
                int a = arr[i];
                int b = arr[j];
                num =m(set,a,b);
                result = result > num ? result : num;
            }
        }

        System.out.println(result);
    }
    public static int  m(HashSet set,int a,int b){
        int num =0;
        while (set.contains(a + b)) {
            a = b;
            b = a + b;
            set.remove(a + b);
            num++;
        }
        return num ;
    }
}
