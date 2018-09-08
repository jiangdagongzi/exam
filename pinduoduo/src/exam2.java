import java.util.LinkedList;
import java.util.Scanner;

public class exam2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        LinkedList linkedList = new LinkedList();
        LinkedList linkedList1 = new LinkedList<>();
        String string = scanner.nextLine();
        for (int i = 0; i < string.length(); i++) {
            linkedList.add(string.charAt(i));
            linkedList1.add(string.charAt(i));
        }
        int result = scanner.nextInt();
        int m = m(linkedList);
        int l = l(linkedList1);
        if (result == m) {
            if (result == l)
                System.out.println("U");
            else System.out.println("M");
        } else if (result == l) {
            System.out.println("L");
        } else {
            System.out.println("I");
        }
        return;
    }

    public static int l(LinkedList<Character> linkedList) {
        int result = 0;
        while (!linkedList.isEmpty()) {
            if (linkedList.peek() >= 48 && linkedList.peek() <= 57) {
                result = linkedList.peek() - 48;
                linkedList.poll();
                if (linkedList.peek() >= 48 && linkedList.peek() <= 57) {
                    result = result * 10 + linkedList.peek() - 48;
                    continue;
                }
            }
            if (linkedList.peek() == '+') {
                int temp = 0;
                linkedList.poll();
                while (!linkedList.isEmpty() && linkedList.peek() >= 48 && linkedList.peek() <= 57) {
                    temp = temp * 10 + linkedList.peek() - 48;
                    linkedList.poll();
                }
                result = result + temp;
                continue;
            }
            if (linkedList.peek() == '*') {
                int temp = 0;
                linkedList.poll();
                while (!linkedList.isEmpty() && linkedList.peek() >= 48 && linkedList.peek() <= 57) {
                    temp = temp * 10 + linkedList.peek() - 48;
                    linkedList.poll();
                }
                result = result * temp;
                continue;
            }
        }
        return result;
    }

    public static int m(LinkedList<Character> linkedlist) {
        int result = 0;
        int right = 0;
        while (!linkedlist.isEmpty()) {
            if (linkedlist.peek() >= 48 && linkedlist.peek() <= 57) {
                result = linkedlist.peek() - 48;
                linkedlist.poll();
                if (linkedlist.peek() >= 48 && linkedlist.peek() <= 57) {
                    result = result * 10 + linkedlist.peek() - 48;
                }
                continue;
            }
            if (linkedlist.peek() == '+') {
                int temp = 0;
                linkedlist.poll();
                while (!linkedlist.isEmpty() && linkedlist.peek() >= 48 && linkedlist.peek() <= 57) {
                    temp = temp * 10 + linkedlist.peek() - 48;
                    linkedlist.poll();
                }
                result = result + temp;
                right = temp;
                continue;
            }
            if (linkedlist.peek() == '*') {
                int temp = 0;
                linkedlist.poll();
                while (!linkedlist.isEmpty() && linkedlist.peek() >= 48 && linkedlist.peek() <= 57) {
                    temp = temp * 10 + linkedlist.peek() - 48;
                    linkedlist.poll();
                }
                result = (result - right) + right * temp;
                right = right * temp;
                continue;
            }
        }
        return result;
    }
}
