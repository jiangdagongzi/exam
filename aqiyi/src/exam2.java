import java.util.Scanner;
import java.util.Stack;
import java.util.stream.Stream;

public class exam2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String string = scanner.nextLine();
        Stack<Character> stack = new Stack();
        for (int i = 0; i < string.length(); i++) {
            char temp = string.charAt(i);
            if (temp == '(') {
                stack.push(string.charAt(i));
                continue;
            }
            if (temp == ')') {
                if (!stack.empty() && stack.peek() == '(')
                    stack.pop();
                else stack.push(temp);
                continue;
            } else {
                stack.push(temp);
                continue;
            }
        }
        System.out.println(stack.size());
    }
}
