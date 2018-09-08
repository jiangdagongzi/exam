import java.util.*;

class graph {
    PriorityQueue<edge> priorityQueue = new PriorityQueue<>(new Comparator<edge>() {
        @Override
        public int compare(edge o1, edge o2) {
            if (o1.val < o2.val)
                    return -1;
                else if (o1.val == o2.val)
                    return 0;
                else return 1;
        }
    });
    int size;

    public graph(int size) {
        this.size = size;
    }

    public int kruskal() {
        edge result = priorityQueue.peek();
        int[] flags = new int[size ];

//        Collections.sort(linkedList, new Comparator<edge>() {
//            @Override
//            public int compare(edge o1, edge o2) {
//                if (o1.val < o2.val)
//                    return -1;
//                else if (o1.val == o2.val)
//                    return 0;
//                else return 1;
//            }
//        });
        int num = 0;
        while (num < size) {
            result= priorityQueue.peek();
                if(flags[result.left -1] == 0){
                    flags[result.left -1] =1;
                    num++;
                    if(flags[result.right-1] == 0){
                        flags[result.right-1 ] =1;
                        num++;
                    }
                    result = priorityQueue.poll();
                    continue;
                }
                if(flags[priorityQueue.peek().right-1] ==0){
                    flags[priorityQueue.peek().right-1]=1;
                    num++;
                    result = priorityQueue.poll();
                    continue;
                }

        }
//            if (flags[linkedList.get(temp).left - 1] == 0) {
//                flags[linkedList.get(temp).left - 1] = 1;
//                num++;
//                if (flags[linkedList.get(temp).right - 1] == 0) {
//                    flags[linkedList.get(temp).right - 1] = 1;
//                    num++;
//                }
//
//                temp++;
//                continue;
//            }
//            if (flags[linkedList.get(temp).right - 1] == 0) {
//                flags[linkedList.get(temp).right - 1] = 1;
//                num++;
//                temp++;
//                continue;
//            }
//            if (num == size - 1)
//                break;
//        }
//        return linkedList.get(temp - 1).val;
        return result.val;
    }
}

class edge {
    int left;
    int right;
    int val;

    public edge(int left, int right, int val) {
        this.left = left;
        this.right = right;
        this.val = val;
    }
}

public class exam2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        graph graph = new graph(n);
        for (int i = 0; i < m; i++) {
            int val1 = scanner.nextInt();
            int val2 = scanner.nextInt();
            int edgeval = scanner.nextInt();
            graph.priorityQueue.add(new edge(val1, val2, edgeval));
        }
        System.out.println(graph.kruskal());
    }
}
