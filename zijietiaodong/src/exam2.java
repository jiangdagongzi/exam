import java.util.Scanner;

class circle {
    node head;
    node tail;

    public circle(int n) {
        node node = new node(0);
        add(node);
        for (int i = 1; i < n; i++) {
            add(new node(i));
        }
    }

    public void add(node node) {
        if (head == null) {
            head = node;
            tail = node;
            tail.next = head;
        } else {
            tail.next = node;
            tail = node;
            tail.next = head;
        }
    }

    public node remove(node flag, int Am) {
        node temp = flag;
        if (Am == 1) {
                while (temp.next != flag)
                    temp = temp.next;
        } else {
            for (int i = 0; i < Am - 2; i++) {
                temp = temp.next;
            }

        }
        node del = temp.next;
        if (temp.next == tail) {
            tail = temp;
        }
        if (temp == tail) {
            head = temp.next.next;
        }
        temp.next = del.next;
        del.next = null;
        return temp.next;
    }
}

class node {
    int val;
    node next;

    public node(int val) {
        this.val = val;
    }

    public node(int val, node next) {
        this.val = val;
        this.next = next;
    }
}

public class exam2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        for (int i = 0; i < N; i++) {
            int n = scanner.nextInt();
            circle circle = new circle(n);
            int m = scanner.nextInt();
            int[] arr = new int[m];
            for (int j = 0; j < m; j++) {
                arr[j] = scanner.nextInt();
            }
            node flag = circle.head;
            int index = 0;
            while (circle.head != circle.tail) {
                flag = circle.remove(flag, arr[index % arr.length]);
                index++;
            }
            System.out.println(circle.head.val);
        }

    }
}
