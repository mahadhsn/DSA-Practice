package LinkedList;

import java.util.*;

public class LL {

    public static void main(String[] args) {

        LinkedList<String> ll = new LinkedList<>();

        /* 
        ll.push("A");
        ll.push("B");
        ll.push("C");
        ll.push("D");
        ll.push("F");
        System.out.println(ll);

        ll.pop();
        System.out.println(ll);
        */

        ll.offer("A");
        ll.offer("B");
        ll.offer("C");
        ll.offer("D");
        ll.offer("F");
        //ll.poll();

        ll.add(4, "E");

        System.out.println(ll);

        ll.remove("B");

        System.out.println(ll.indexOf("F"));

        System.out.println(ll.peekFirst());

        System.out.println(ll.peekLast());

        System.out.println(ll);

    }

}