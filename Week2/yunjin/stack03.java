import java.util.*;

class stack03 {
    boolean solution(String s) {
        Stack<Character> st = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                st.push('(');
            } else if (c == ')') {
                if (st.isEmpty()) {
                    return false;
                } else {
                    st.pop();
                }

            }
        }

        if (st.size() == 0) {
            return true;
        } else {
            return false;
        }
    }
}