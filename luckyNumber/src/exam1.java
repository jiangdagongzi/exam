import java.util.LinkedList;
import java.util.Scanner;
class  A{
    public String show(D d){return ("AD");}
    public String show(A a){return ("AA");}
}

class B extends A{
    public String show(B b){return ("BB");}
    public String show(A a){return ("BA");}
}

class C extends B{}

class D extends B{}



public class exam1 {
    public static void main(String[] args) {

    }
//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        int n = scanner.nextInt();
//        int i = 1;
//        int result = 0;
//        LinkedList linkedList = new LinkedList();
//        linkedList.add("A");
//        linkedList.add(0,"B");
//        String s = (String)linkedList.get(1);
//        System.out.println(s);
//        while (i < n) {
//            if (f(i) == g(i)) {
//                result++;
//                System.out.println(i);
//                System.out.println(f(i));
//                System.out.println(g(i));
//            }
//            i++;
//        }
//        System.out.println(result);
    }

//    public static int f(int n) {
//        int result = 0;
//        while (n >= 10) {
//            result = n % 10 + result;
//            n = n / 10;
//        }
//        result = result + n;
//        return result;
//    }
//
//    public static int g(int n) {
//        String string = Integer.toBinaryString(n);
//        int result = 0;
//        for (int i = 0; i < string.length(); i++) {
//            if (string.charAt(i) == '1')
//                result++;
//        }
//        return result;
//    }

//}
