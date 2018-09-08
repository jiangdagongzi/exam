
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

public class exam1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        LinkedList<String> linkedList = new LinkedList<>();
        Stack<Integer> stack = new Stack<>();
        int num = 0;
        while (scanner.hasNext()) {
            linkedList.add(scanner.nextLine());
        }
        for (int i = 0; i < linkedList.size(); i++) {
            String s = linkedList.get(i);
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == '/' && s.charAt(j + 1) == '/') {
                    if(stack.empty() ){
                        num ++;
                    }

                    else if(stack.peek() == 3){
                        continue;
                    }
                }
                if(s.charAt(j)=='/'&&s.charAt(j+1)=='*'){
                    if (stack.empty() ||stack.peek() != 2){
                        stack.push(2);
                    }
                    else if(stack.peek() == 2){
                        stack.pop();
                        num ++;
                    }
                    else if(stack.peek() == 3){
                        continue;
                    }
                }
                if(s.charAt(j) == '"'){
                    if(stack.empty()||stack.peek()!=3){
                        stack.push(3);
                    }
                    else if(stack.peek() ==3){
                        stack.pop();
                    }

                }
            }
        }
    }

}
