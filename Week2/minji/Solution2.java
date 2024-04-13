import java.util.*;

public class Solution2 {
    public int[] solution(int []arr) {
        List<Integer> answer = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        
        for(int i=0; i<arr.length; i++)
        {
            if (stack.contains(arr[i]))
            {
                continue;
            }
            else
            {
                if(!stack.empty()){
                 stack.pop();   
                }
                stack.add(arr[i]);
                answer.add(arr[i]);
            }
        }
        
        return answer.stream()
                .mapToInt(i -> i)
                .toArray();
    }
}
