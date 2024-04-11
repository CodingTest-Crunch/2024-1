import java.util.*;

class stack02 {
    public int[] solution(int[] progress, int[] speed) {
        int[] arr;
        Stack<Integer> st = new Stack<>();
        arr = new int[progress.length];
        for (int i = 0; i < progress.length; i++) {
            if ((100 - progress[i]) % speed[i] != 0) {
                arr[i] = (100 - progress[i]) / speed[i] + 1;
            } else {
                arr[i] = ((100 - progress[i]) / speed[i]);
            }
        }
        int max = arr[0];
        int cnt = 1;
        for (int i = 1; i < arr.length; i++) {
            if (max >= arr[i]) {
                cnt++;
            } else {
                st.push(cnt);
                cnt = 1;
                max = arr[i];
            }
        }
        st.push(cnt);
        int answer[] = new int[st.size()];
        for (int i = st.size() - 1; i >= 0; i--) {
            answer[i] = st.pop();
        }
        return answer;
    }
}