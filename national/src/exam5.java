public class exam5 {
    String str = new String ("hello");
    char[] chars = {'a','b','c'};
    public static void main(String[] args){
        exam5 exam5 = new exam5();
        change(exam5.str,exam5.chars);
        System.out.print(exam5.str+"and");
        System.out.print(exam5.chars);
    }
    public static void change(String str,char[] chars){
        str = new String("world");
        chars[0] = 'g';
    }
}
