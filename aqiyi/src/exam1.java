import com.sun.org.apache.xalan.internal.xsltc.dom.SimpleResultTreeImpl;

import java.awt.geom.FlatteningPathIterator;
import java.util.Scanner;
import java.util.Stack;

/**
 * Definition for binary tree
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode righ t;
 * TreeNode(int x) { val = x; }
 * }
 */
//class TreeNode {
//    int val;
//    TreeNode left;
//    TreeNode right;
//
//    TreeNode(int x) {
//        val = x;
//    }
//}

public class exam1 {
    //    {
//        System.out.println(1);
//    }
//    public exam1(){
//        System.out.println(2);
//    }
//    static {
//        System.out.println(3);
//    }
    public static void main(String[] args) {
        int[] arr = {2, 5, 4, 3, 9, 1, 0, 8, 1, 1};
        arr = quicksort(arr, 0, arr.length-1);
        for (int i  =0;i<arr.length;i++){
            System.out.println(arr[i]);
        }
//       StringBuilder stringBuilder = new StringBuilder();
//       Stack stack = new Stack();
//        Scanner scanner = new Scanner(System.in);
//        int n = scanner.nextInt();
//        while (n>0){
//            stack.push((char)(n%26+(int)'A'));
//            n = n/26;
//        }
//        while(!stack.empty()){
//            stringBuilder = stringBuilder.append(stack.pop());
//        }
//        System.out.println(stringBuilder);
//        String  string = new String("hello,gorgeous");
//       try {
//           Field field = String.class.getDeclaredField("value");
//           field.setAccessible(true);
////           char[] value = field.get(string).toString().toCharArray();
//           char[] value = (char[]) field.get(string);
//           value[5] = '!';
//       }
//       catch (Exception e){
//
//       }
//       System.out.println(string);

//        Stack<TreeNode> stack = new Stack<>();
//        stack.push(root);
//        TreeNode temp;
//        ArrayList<TreeNode> arrayList = new ArrayList();
//        while (!stack.empty()) {
//            temp = stack.peek();
//            if (temp != null) {
//                stack.push(temp.left);
//                stack.push(temp.right);
//            } else
//                stack.pop();
//            if (stack.peek() == null)
//                arrayList.add(stack.pop());
//        }
//        int n = (int) Math.log((arrayList.size() + 1) / 2);
//        ArrayList<ArrayList<Integer>> arrayLists = new ArrayList<>();
//        int curr =0;
//        for (int i = 0; i < n; i++) {
//            ArrayList arrayList1 = new ArrayList();
//            arrayLists.add(arrayList1);
//            for(int j = 0;j <1<<i;j++){
//                if(arrayList.get(curr) == null)
//                    curr++;
//                else arrayList1.add(arrayList.get(curr).val);
//            }
//        }
//        return arrayLists;
    }

    public static int[] quicksort(int[] arr, int l, int r) {
        int left = l;
        int right = r;
        if(l>=r)
            return arr;
        //数组只有一个数，直接返回
        if (left == right)
            return arr;
        int temp = arr[left];
        //数组只有两个数，如果倒序则swap，否则返回
        if (left == right - 1) {
            if (arr[left] > arr[right]) {
                arr[left] = arr[right];
                arr[right] = temp;
            }
            return arr;
        }
        int flag = arr[left];
        while (left < right) {

            while (arr[right] >= flag && right > left)
                right--;
            while (arr[left] <= flag && right > left)
                left++;
            temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
        }
        int k = left;
        temp = arr[left];
        arr[left] = arr[l];
        arr[l] = temp;
        quicksort(arr, l, k -1);
        quicksort(arr, k + 1, r);
        return arr;
    }
}
//class exam0{
//    {
//        System.out.println(4);
//    }
//    exam0(){
//            System.out.println(5);
//    }
//    static {
//        System.out.println(6);
//    }
//}