import java.util.*;

class MyCompare implements Comparator<Map.Entry<Character, Integer>> {
    public static Comparator<Map.Entry<Character, Integer>> testCom = new MyCompare();

    @Override
    public int compare(Map.Entry<Character, Integer> e1, Map.Entry<Character, Integer> e2) {
        if (e1.getValue() < e2.getValue())
            return -1;
        else if (e1.getValue().hashCode() == e2.getValue().hashCode()) {
            if (e1.getKey() < e2.getKey())
                return -1;
            else
                return 1;
        } else return 0;
    }
}

public class exam1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = new String(scanner.next());
        HashMap<Character, Integer> hashMap = new HashMap();
        for (int i = 0; i < str.length(); i++) {
            if (!hashMap.containsKey(str.charAt(i)))
                hashMap.put(str.charAt(i), 1);
            else hashMap.put(str.charAt(i), Integer.valueOf(hashMap.get(str.charAt(i)).toString()) + 1);
        }
        LinkedList<Map.Entry> linkedList = new LinkedList(hashMap.entrySet());
        Collections.sort(linkedList, MyCompare.testCom);
        LinkedHashMap linkedHashMap = new LinkedHashMap();
        for (Map.Entry entry : linkedList) {
            System.out.println(entry.getKey());
        }

        return;
    }
}