import java.util.Scanner;

public class exam1 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String string = scanner.nextLine();
        for(int i = 0 ; i <string.length();i ++){
            if(string.charAt(i) <= 90&&string.charAt(i)>=65)
                System.out.print((char)(string.charAt(i) + 1));
            else if (string.charAt(i)>= 97&&string.charAt(i)<= 122)
                System.out.print((char)(string.charAt(i) + 1));
            else
                System.out.print(string.charAt(i));
        }
        return;
    }
}
