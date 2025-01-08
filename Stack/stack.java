package Stack;
import java.util.Stack;

public class stack {
    
    public static void main(String[] args) {
        Stack<String> stack = new Stack<String>();

        // push
        stack.push("Minecraft");
        stack.push("COD");
        stack.push("FH5");
        stack.push("Rocket League");

        System.out.println(stack);
        // peek
        System.out.println(stack.peek());
        
        // pop
        stack.pop();
        System.out.println(stack.peek());
        
        // search
        System.out.println(stack.search("Minecraft"));
    }

}