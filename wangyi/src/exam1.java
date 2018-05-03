import java.util.*;

class MyComparator implements Comparator<Map.Entry<Integer, Integer>> {

    public static int getFlag() {
        return flag;
    }

    public void setFlag(int flag) {
        this.flag = flag;
    }

    public static int flag = 0;

        @Override
        public int compare(Map.Entry<Integer, Integer> entry1, Map.Entry<Integer, Integer> entry2) {
            if(entry1.getKey()>flag&&entry2.getKey()>flag){
                    if(entry1.getKey()>entry2.getKey())return 1;
                    else return -1;
            }
            else if(entry1.getKey()<=flag&& entry2.getKey()>flag)
                return -1;
            else if(entry1.getKey()>flag&&entry2.getKey()<= flag)
                return 1;
            else if(entry1.getValue()>entry2.getValue())
                return -1;
            else return 1;
    }
}

public class exam1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        HashMap hashMap = new HashMap();
        for (int i = 0; i < n; i++) {
            hashMap.put(scanner.nextInt(), scanner.nextInt());
        }
        int[] arr = new int[m];
        for (int i = 0; i < m; i++) {
            arr[i] = scanner.nextInt();
        }
        LinkedList<Map.Entry<Integer, Integer>> linkedList = new LinkedList(hashMap.entrySet());
        for(int i = 0 ; i <n;i++){
            MyComparator testComparator = new MyComparator();
            testComparator.setFlag(arr[i]);
            Collections.sort(linkedList, testComparator);
            System.out.println(linkedList.get(0).getValue());
        }
        return;
    }
}

