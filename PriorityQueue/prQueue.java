package PriorityQueue;

import java.util.*;

public class prQueue {

    public static void main(String[] args) {
        
        Queue<Double> q = new PriorityQueue<>();

        q.offer (3.0); 
        q.offer (2.5); 
        q.offer (4.0); 
        q.offer (1.5); 
        q.offer (2.0);

        while(!q.isEmpty()) {
            System.out.println(q.poll()); // show and remove all values
        }

        Queue<String> qq = new PriorityQueue<>();

        qq.offer("D");
        qq.offer("E");
        qq.offer("O");
        qq.offer("A");

        while(!qq.isEmpty()) {
            System.out.println(qq.poll()); // show and remove all values
        }
    }
}