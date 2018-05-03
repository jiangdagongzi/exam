import sun.security.krb5.SCDynamicStoreConfig;

import javax.print.DocFlavor;
import java.util.Scanner;

class Node{
    String val ;
    Node next;
    Node front;
    public Node (String string){
            val = string;
    }
    public void setNext(Node node){
        next = node;
    }
    public void setFront(Node node){
        front = node;
    }
    public Node getNext(){
        return next;
    }
    public Node getFront(){
        return front;
    }
    public String getVal(){
        return val;
    }
    public static Node createCircle(Node[] nodes){
        Node head = nodes[0];
        Node temp = head;
        for(int i = 1; i < nodes.length;i++){
            temp.setNext(nodes[i]);
            temp.getNext().setFront(temp);
            temp= temp.getNext();
        }
        temp.setNext(head);
        head.setFront(temp);
        return head;
    }
}
public class exam4 {
    public static void main(String[] args){
        String[] strings = {"N","E","S","W"};
        Node[] nodes = new Node[strings.length];
        for(int i = 0; i< strings.length;i++){
            nodes[i] = new Node(strings[i]);
        }
        Node node = Node.createCircle(nodes);
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String string = scanner.next();
        for(int i = 0 ; i < n ; i ++){
            if(string.charAt(i)=='L')
                node = node.getFront();
            else node= node.getNext();
        }
        System.out.println(node.getVal());
    }

}
