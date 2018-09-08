import java.util.*;

class myHandler implements Thread.UncaughtExceptionHandler {
    public void uncaughtException(Thread t, Throwable throwable) {
        System.out.println("不被检测的异常发生");
    }
}

class Shape implements Comparable<Shape> {
    int val;

    public int compareTo(Shape shape) {
        if (shape.val > this.val)
            return -1;
        else return 1;
    }
}

class Circle extends Shape {
    int val1;
}

class Square extends Shape {
    int val2;
}0

class myRunnable implements Runnable {
    public void run() {
        try {
            int i = 0;
            if (i < 1) {
                int[] arr = new int[10];
                int a = arr[10];
                Thread.sleep(1000);
                System.out.println(i);

            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class exam1 {
    public static void main(String[] args) {
        int a  = 9;
        int[] arr  = new  int[10];
        for (int i = 0 ; i<10;i++){
            arr[i] = i;
        }
        System.out.println(arr[a--]);
        return;

//        int result = 0;
//        Scanner scanner = new Scanner(System.in);
//        int n = scanner.nextInt();
//
//        result = num(n);
//        System.out.println(result);
//        A[5] a = new A[5];
//        Comparable[] comparables = new Integer[5];
//        comparables[0] = new Integer(1);
//
//        try {
//
//        }catch (ArrayStoreException e){
//            e.printStackTrace();
//        }

//        myRunnable runnable = new myRunnable();
//        int i = 0;
//        while (i < 10) {
//            Thread thread = new Thread(runnable);
//            myHandler handler = new myHandler();
//            thread.setUncaughtExceptionHandler(handler);
//            thread.start();
//            i++;
    }

//        PriorityQueue<GregorianCalendar> priorityQueue = new PriorityQueue();
//        priorityQueue.add(new GregorianCalendar(2017,Calendar.DECEMBER,3));
//        priorityQueue.add(new GregorianCalendar(2017,Calendar.DECEMBER,5));
//        priorityQueue.add(new GregorianCalendar(1999,Calendar.NOVEMBER,15));
//        priorityQueue.add(new GregorianCalendar(2005,Calendar.APRIL,1));
//        for(GregorianCalendar gregorianCalendar : priorityQueue){
//            System.out.println(gregorianCalendar.get(Calendar.YEAR));
//        }
//
//        while(!priorityQueue.isEmpty()){
//            System.out.println(priorityQueue.remove().get(Calendar.YEAR));
//        }
//        Scanner scanner = new Scanner(System.in);
//        int n = scanner.nextInt();
//        int[] arr = new int[n];
//        HashMap<Integer, Integer> hashMap = new HashMap();
//        for (int i = 0; i < n; i++) {
//            arr[i] = scanner.nextInt();
//        }
//        for (int i = 0; i < n; i++) {
//            if (hashMap.containsKey(arr[i]) == false) {
//                hashMap.put(arr[i], 1);
//            } else hashMap.put(arr[i], hashMap.get(arr[i]) + 1);
//        }
//
//        int num = 0;
//        num = hashMap.get(4);
//        hashMap.put(4, 0);
//        num = num + hashMap.get(2) / 2;
//        if (hashMap.get(2) % 2 == 0) {
//            hashMap.put(2, 0);
//        } else {
//            hashMap.put(2, 1);
//        }
//        if (hashMap.get(1) >= hashMap.get(3)) {
//            num = num + hashMap.get(3);
//            hashMap.put(1, hashMap.get(1) - hashMap.get(3));
//            hashMap.put(3, 0);
//        } else {
//            num = num + hashMap.get(1);
//            hashMap.put(3, hashMap.get(3) - hashMap.get(1));
//            hashMap.put(1, 0);
//            num = num + hashMap.get(2) + hashMap.get(3);
//        }
//        if (hashMap.get(1) != 0) {
//            if (hashMap.get(2) != 0) {
//                num++;
//                hashMap.put(2, 0);
//                hashMap.put(1, hashMap.get(1) - 2);
//            }
//            num = num + hashMap.get(1) / 4;
//            if (hashMap.get(1) % 4 != 0) {
//                num++;
//            }
//
////            if (hashMap.get(1) <= 2) {
////                num++;
////            } else {
////                num++;
////                hashMap.put(1, hashMap.get(1) - 2);
////                num = num + hashMap.get(1)/ 4;
////                if (hashMap.get(1) % 4 != 0) {
////                    num ++;
////                }
////            }
//        }
//        System.out.println(num);

    public static int num(int n) {
        int result = 0;
        while (n > 0) {
            if (n == 1) {
                result = 1;
                n = 0;
            } else if (n % 2 == 0) {
                n = n / 2;
            } else {
                result = num(n / 2) + 1;
                break;
            }

        }
        return result;
    }
}

