package Queue;

// Queue is an interface in java
// import java.util.Queue;
// so we use LinkedLists instead as they implement a Queue
import java.util.LinkedList;
import java.util.Queue;

public class queue {

    public static void main(String[] args) {

        Queue<String> queue = new LinkedList<String>();

        // enqueue
        queue.offer("A");
        queue.offer("B");
        queue.offer("C");
        queue.offer("D");
        queue.offer("E");
        System.out.println(queue);
        System.out.println(queue.peek()); // returns the first entry

        // removes first entry
        queue.poll(); // can poll freely
        System.out.println(queue);

        // check if empty
        System.out.println(queue.isEmpty());

        // return size
        System.out.println(queue.size());

        // check for variable
        System.out.println(queue.contains("B"));

    }
}